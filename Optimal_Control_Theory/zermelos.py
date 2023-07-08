""" --------------------------------------------------------------------------
            Optimal Control Problem: Numerical Analysis & Functions for Solving
                                     Zermelo's Problem. Maximizing Upstream 
                                     Distance Travelled for a Default River 
                                     Current
                                                                        
            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import math
import pickle
import numpy as np

from scipy.integrate import solve_ivp
from scipy.optimize import fsolve

class boat(object):

    def __init__(self,initial_guess):
        """
        initial_guess:
            Parameter requires the initial state vector to have the following format:
            [x_position,y_position,lambda_1]

            Lambda_2 assumed to be -1 and constant for this setup and is accounted for
            within these functions

        """

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.num_sol_picklefile = "zermelos_sol.pickle"        

        # Meta Data
        # --------------------------------------------------------------------------------   
        self.linebreak = "-"*70
        self.figure_comment = ""

        # Get and Set Initial Condition
        # --------------------------------------------------------------------------------   
        self.initial_position = initial_guess[:2]
        self.initial_lambda_guess = initial_guess[2]
        self.initial_delta = np.arctan2(1,-1*self.initial_lambda_guess)
   
        # Set Target State
        # --------------------------------------------------------------------------------   
        # Default x(t_f) target
        self.x_target = 100 # meters
    
        # Numerical Analysis Setup
        # --------------------------------------------------------------------------------
        self.initial_guess = initial_guess

        # Default tolerance values
        self.absTol = 1e-10
        self.relTol = 1e-10
        self.xTol = 1e-10

        # Default shooting method scales
        # --------------------------------------------------------------------------------
        self.pos_shooting_scale = 10
        # self.hamiltonian_shooting_scale = 10

        # Initiate shooting method trajectory history
        # --------------------------------------------------------------------------------
        self.trajectory_history = []

    def current(self,x,y):
        """
        Default definition of river current U(x,y) used for docs example
        """

        ux = 0
        uy = 2*np.sin((np.pi*x)/100)

        return [ux,uy]

    def differential_equations(self,t,state):

        x = state[0]
        y = state[1]
        boat_velocity = self.boat_velocity # Assumes constant boat velocity

        lambda_1 = state[2]
        # From natural bound condition See zermelos_problem.html#numerical-river-example
        lambda_2 = -1 

        # Control
        # delta = np.arctan2(-1,lambda_1)

        # Get current at given state
        ux,uy = self.current(x,y)

        # Differential equations
        x_dot = -1*(boat_velocity*lambda_1)/(math.sqrt(lambda_1*lambda_1+1)) + ux
        y_dot = -1*(boat_velocity*lambda_2)/(math.sqrt(lambda_1*lambda_1+1)) + uy

        lambda_dot = (np.pi/50)*np.cos((np.pi*x)/100)

        # Return d/dt vector of 
        # [x, y, lambda_1]
        return np.array([x_dot,y_dot,lambda_dot])        

    def solve_initial_value_problem(self):

        # It is important that ivp has the following setup
        # [x, y, lambda_1]
        ivp = self.initial_value_problem
        
        self.num_sol = solve_ivp(self.differential_equations,
                                [self.time[0],self.time[-1]],ivp,
                                 t_eval=self.time,rtol=self.relTol,atol=self.absTol)

        # Check if solver reached interval end or a termintion event occured 
        print("Solver Success: ", self.num_sol.success)
        if not self.num_sol.success:
            print("Solver termination status:  ", self.num_sol.status)
        
        # Numerical Results
        self.all_numerical = self.num_sol.y.T
        self.final_state = self.all_numerical[-1,:]

        # Extract Position, and Control Parameter for use upstream
        self.position_numerical = self.num_sol.y[:2,:].T
        self.lambda_numerical = self.num_sol.y[2,:].T
        self.control = [np.arctan2(1,-l) for l in self.lambda_numerical]

        # Calculate Velocity Using Diff Eqs. Solution
        velocity_temp = []
        for v_indx in range(len(self.all_numerical)):
            # Time isn't used in self.differential_equations() using t=0
            velocity_temp.append(self.differential_equations(0,self.all_numerical[v_indx])[:2])
        self.velocity_calculated = np.array(velocity_temp)


        return

    def get_dH_du(self):
        """
        Calculates the partial of the Hamiltonian wrt control (dH/du)
        See Equation zermelos_problem.html#control
        dH/du = -l1*V*sin(𝛿) + l2*V*cos(𝛿) 

        """

        boat_velocity = self.boat_velocity # Assumes constant boat velocity
        control_history = self.control
        l1_sol = self.lambda_numerical
        l2_sol = -1 # From natural bound condition 
        
        dH_du = []
        for indx,delta in enumerate(control_history):
            dH_du.append(-1*l1_sol[indx]*boat_velocity*np.sin(delta) +
                          l2_sol*boat_velocity*np.cos(delta))
        self.dH_du = dH_du

        return

    def shooting_method(self,lambda_analysis):
        """
        Simple shooting method using solve_ivp methods to solve trajectory 
        and satify constratin ∆x(t_f) = x_f - X = 0

        Returns lambda 1 
        """

        # Allow solver to only change lambda, keep initial position as is
        self.initial_value_problem = self.initial_position + lambda_analysis.tolist()
        self.solve_initial_value_problem()

        # NOTE: fsolve requires input and output len to match
        root_target = [self.pos_shooting_scale*abs(self.final_state[0] - self.x_target)] # ∆x(t_f)               
  
        # Keep track of iterations
        self.trajectory_history.append(self.position_numerical)

        return root_target

    def solve_trajectory(self):

        root = fsolve(self.shooting_method,self.initial_lambda_guess ,xtol=self.xTol)

        self.lambda_solution = root

        return