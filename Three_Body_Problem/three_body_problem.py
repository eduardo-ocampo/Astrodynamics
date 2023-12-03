""" --------------------------------------------------------------------------
            Three Body Problem: Numerical Analysis & Functions for the 
                                Non-Dimensional Circular Restricted 
                                Three-Body Problem (CR3BP)
                                                                        
            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import math
import pickle
import numpy as np
from numpy.linalg import norm
from scipy.integrate import solve_ivp

class cr3bp(object):

    def __init__(self,posVector,velVector):

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.num_sol_picklefile = "cr3bp.pickle"        

        # Meta Data
        # --------------------------------------------------------------------------------   
        self.linebreak = "-"*70

        # Set CR3BP Primary Bodies Mass Ratio
        # --------------------------------------------------------------------------------   
        # Default Set to Earth-Moon System
        self.mu = 0.012150515586657583

        # Set Position and Velocity Vector
        # --------------------------------------------------------------------------------   
        # Assumed input is in SI units (km, sec)    
        self.position = posVector
        self.velocity = velVector

        self.positionMag = norm(posVector)
        self.velocityMag = norm(velVector)

        # Numerical Analysis Setup
        # --------------------------------------------------------------------------------
        self.initial_value_problem = posVector + velVector
        # Default tolerance values
        self.absTol = 1e-10
        self.relTol = 1e-10

    def differential_equations(self,t,state):

        x,y,z, vx,vy,vz = state
        
        # Compute Differential Equation Constants:
        # Position to Primary Bodies
        r1 = math.sqrt((x+self.mu)**2 + y**2 + z**2)
        r2 = math.sqrt((x-1+self.mu)**2 + y**2 + z**2)

        # Differential Equations: ddot is a second derivative
        x_ddot =  2*vy + x - (1-self.mu)*(x+self.mu)/r1**3 - self.mu*(self.mu+x-1)/r2**3
        y_ddot = -2*vx + y - y*(1-self.mu)/r1**3 - self.mu*y/r2**3
        z_ddot =  -z*(1-self.mu)/r1**3 - self.mu*z/r2**3

        # Return d/dt vector of
        # [x, y, z, vx, vy, vx]
        return np.concatenate(([vx,vy,vz],[x_ddot,y_ddot,z_ddot]))

    def solve_threeBody_trajectory(self,saveAnalysis=False):

        # Here it is important that ivp has the following setup
        # [x, y, z, vx, vy, vx]
        ivp = self.initial_value_problem

        self.num_sol = solve_ivp(self.differential_equations,
                                [self.time[0],self.time[-1]],
                                 ivp,t_eval=self.time,rtol=self.relTol,atol=self.absTol)

        # Check if solver reached interval end or a termintion event occured 
        print("Solver Success:  ", self.num_sol.success)
        if not self.num_sol.success:
            print("Solver termination status:  ", self.num_sol.status)

        # Extract Position and Velocity Results
        self.position_numerical = self.num_sol.y[:3,:].T
        self.velocity_numerical = self.num_sol.y[3:,:].T

        # Allow user to save numerical anlaysis
        if saveAnalysis:
            with open(self.num_sol_picklefile, 'wb') as handle:
                pickle.dump(self, handle)

    def differential_equations_jacobian(self,t,state):

        x,y,z, vx,vy,vz, *phi = state

        # State Transition Matrix
        phi_matrix = np.reshape(phi,(4,4))

        # Compute Differential Equation Constants:
        # Position to Primary Bodies
        r1 = math.sqrt((x+self.mu)**2 + y**2 + z**2)
        r2 = math.sqrt((x-1+self.mu)**2 + y**2 + z**2)

        # Differential Equations of Motions: ddot is a second derivative
        x_ddot =  2*vy + x - (1-self.mu)*(x+self.mu)/r1**3 - self.mu*(self.mu+x-1)/r2**3
        y_ddot = -2*vx + y - y*(1-self.mu)/r1**3 - self.mu*y/r2**3
        z_ddot =  -z*(1-self.mu)/r1**3 - self.mu*z/r2**3

        # Jacobian Partials
        x1 = -self.mu
        x2 = 1-self.mu
        omega_xx = 1 - ((1-self.mu)/(r1**3))*(1-3*((x-x1)**2)/r1**2) - (self.mu/r2**3)*(1 - (3*(x-x2)**2)/r2**2)
        omega_yy = 1 - ((1-self.mu)/(r1**3))*(1-3*(y**2)/r1**2) - (self.mu/r2**3)*(1 - (3*(y**2))/r2**2)
        omega_xy = 3*y*((1-self.mu)*(x-x1)/(r1**5) + self.mu*(x-x2)/r2**5)
        
        # Jacobian in Matrix form
        a = np.array([[       0,        0,    1,    0],
                      [       0,        0,    0,    1],
                      [omega_xx, omega_xy,    0,    2],
                      [omega_xy, omega_yy,   -2,    0]])

        # STM Differentail Equations
        phi_dot = a@phi_matrix

        return np.concatenate(([vx,vy,vz],[x_ddot,y_ddot,z_ddot],np.reshape(phi_dot, 16)))

    def get_jacobi(self,pos,vel):

        x,y,z = pos
        vx,vy,vz = vel
        
        # Set Constants
        r1 = math.sqrt((x+self.mu)**2 + y**2 + z**2)
        r2 = math.sqrt((x-1+self.mu)**2 + y**2 + z**2)

        v_potent = (0.5)*(x**2+y**2+z**2) + (1-self.mu)/r1 + self.mu/r2

        # Compute Non-Dimensional Jacobi Constant
        j = (0.5)*(vx**2+vy**2+vz**2)-v_potent

        return j

class cr3bp_stability_analysis(object):

    def __init__(self,posVector):

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.num_sol_picklefile = "cr3bp.pickle"        

        # # Meta Data
        # # --------------------------------------------------------------------------------   
        # self.linebreak = "-"*70

        # Set CR3BP Primary Bodies Mass Ratio
        # --------------------------------------------------------------------------------   
        # Default Set to Earth-Moon System
        self.mu = 0.012150515586657583

        # Set Position and Velocity Vector
        # --------------------------------------------------------------------------------   
        # Assumed input is in SI units (km, sec)    
        self.initial_position = posVector
        self.initial_positionMag = norm(posVector)
        # self.initial_velocity = velVector
        # self.initial_velocityMag = norm(velVector)

        # # Set State Transition Matrix
        # # --------------------------------------------------------------------------------   
        # # Assumed this analysis if for planar trajector
        # if initialPhis.ndim > 1:
        #     initialPhis = initialPhis.reshape(16)
        # self.initial_phis = initialPhis


        # # Numerical Analysis Setup
        # # --------------------------------------------------------------------------------
        # self.initial_value_problem = posVector + velVector + list(initialPhis)
        # # Default tolerance values
        # self.absTol = 1e-10
        # self.relTol = 1e-10


    def jacobian_matrix(self,state):

        x,y,z, = state

        # Position to Primary Bodies
        r1 = math.sqrt((x+self.mu)**2 + y**2 + z**2)
        r2 = math.sqrt((x-1+self.mu)**2 + y**2 + z**2)

        # Jacobian Partials
        x1 = -self.mu
        x2 = 1-self.mu
        omega_xx = 1 - ((1-self.mu)/(r1**3))*(1-3*((x-x1)**2)/r1**2) - (self.mu/r2**3)*(1 - (3*(x-x2)**2)/r2**2)
        omega_yy = 1 - ((1-self.mu)/(r1**3))*(1-3*(y**2)/r1**2) - (self.mu/r2**3)*(1 - (3*(y**2))/r2**2)
        omega_xy = 3*y*((1-self.mu)*(x-x1)/(r1**5) + self.mu*(x-x2)/r2**5)
        
        # Jacobian in Matrix form
        jm = np.array([[       0,        0,    1,    0],
                       [       0,        0,    0,    1],
                       [omega_xx, omega_xy,    0,    2],
                       [omega_xy, omega_yy,   -2,    0]])

        return jm