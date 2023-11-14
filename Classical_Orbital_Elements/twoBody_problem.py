""" --------------------------------------------------------------------------
            Two-Body Problem: Numerical Trajectory Analysis & Functions for
                              Computing the Classical Orbit Elements 
                                                                        
            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import math
import pickle
import numpy as np
from numpy.linalg import norm
from scipy.integrate import solve_ivp

class twoBody(object):

    def __init__(self,pos_vector:"km", vel_vector:"km/sec"):

        # Set Gravitational Constant
        # --------------------------------------------------------------------------------   
        # Default Set to Earth
        self.mu = 3.986004418E+05 # km^3/sec^2

        # Set Position and Velocity Vector
        # --------------------------------------------------------------------------------   
        # Assumed input is in SI units (km, sec)    
        self.position = pos_vector
        self.velocity = vel_vector

        self.positionMag = norm(pos_vector)
        self.velocityMag = norm(vel_vector)

        # Initialize Orbit Element Dictionary
        # --------------------------------------------------------------------------------           
        self.orbit_elements = {"Position Magnitude":{"value": norm(pos_vector),
                                                     "units": "km"},
                               "Velocity Magnitude":{"value": norm(vel_vector),
                                                     "units": "km/sec"}}

        # Numerical Analysis Setup
        # --------------------------------------------------------------------------------
        self.initialValueProblem = pos_vector + vel_vector
        # Default tolerance values
        self.absTol = 1e-10
        self.relTol = 1e-10

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.resultsOut = "orbitElements.txt"
        self.num_sol_picklefile = "twoBody_trajectory.pickle"        

        # Meta Data
        # --------------------------------------------------------------------------------   
        self.linebreak = "-"*70

    def get_state_elements(self) -> None:

        v = self.velocityMag
        r = self.positionMag

        # Specific Energy
        # --------------------------------------------------------------------------------   
        energy = v**2/2 - self.mu/r # Vis-Viva Equation
        self.orbit_elements["Specific Energy"] = {"value": energy, 
                                                  "units": "km^2/sec^2"}

        # Specific Angular Momentum Vector
        # --------------------------------------------------------------------------------   
        ang_momentum = np.cross(self.position,self.velocity)
        self.orbit_elements["Specific Angular Momentum"] = {"value": norm(ang_momentum), 
                                                            "units": "km^2/sec"}


        # Eccentricity Vector
        # --------------------------------------------------------------------------------   
        eccentricity = (1/self.mu)*(np.cross(self.velocity,ang_momentum))-self.position/r
        self.orbit_elements["Eccentricity"] = {"value": norm(eccentricity), 
                                               "units": " "}

        # Inclination
        # --------------------------------------------------------------------------------   
        incl = np.arccos(np.dot([0,0,1],ang_momentum)/norm(ang_momentum))
        self.orbit_elements["Inclination"] = {"value": np.degrees(incl), 
                                              "units": "degrees"}

        # Ascending Node Vector 
        # --------------------------------------------------------------------------------   
        node_vec = np.cross([0,0,1],ang_momentum)
        # self.orbit_elements["Ascend. Node Magnitude"] = {"value": norm(node_vec), 
        #                                                  "units": "km^2/sec"}

        # Longitude of Ascending Node (Ω)
        # --------------------------------------------------------------------------------   
        long_ascend_node = np.arccos(np.dot([1,0,0],node_vec)/norm(node_vec))

        if node_vec[1] >= 0.0:
            lan =  np.degrees(norm(long_ascend_node))
        elif node_vec[1] < 0.0:
            lan = np.degrees(2*np.pi - norm(long_ascend_node))
        self.orbit_elements["Long. of Ascend. Node (Ω)"] = {
                            "value": lan, 
                            "units": "degrees"}

        # Argument of Perigee (ω)
        # --------------------------------------------------------------------------------   
        arg_peri = np.arccos(np.dot(node_vec,eccentricity) / 
                            (norm(eccentricity)*norm(node_vec)))
        # Check ecc_zcomp
        if eccentricity[-1] < 0:
            arg_peri = 2*np.pi - arg_peri
        self.orbit_elements["Argument of Perigee (ω)"] = {"value": np.degrees(arg_peri), 
                                                          "units": "degrees"}

        # Semi-latus Rectum
        # --------------------------------------------------------------------------------   
        p = norm(ang_momentum)*norm(ang_momentum)/self.mu
        # self.orbit_elements["Semi-Latus Rectum"] = {"value": p, 
        #                                             "units": "km"}

        # Semi-major Axis
        # --------------------------------------------------------------------------------   
        # a = p/self.mu*(1-norm(eccentricity)*norm(eccentricity))
        a = -self.mu/(2*energy)
        self.orbit_elements["Semi-Major Axis"] = {"value": a, 
                                                  "units": "km"}

        # Mean Motion
        # --------------------------------------------------------------------------------   
        try:
            n = math.sqrt(self.mu/(a**3))
        except ValueError as e:
            n = np.nan
        self.orbit_elements["Mean Motion"] = {"value": n, 
                                              "units": "rad/sec"}

        # True Anomaly
        # --------------------------------------------------------------------------------   
        # f = np.arccos((p-r)/(r*norm(eccentricity)))
        f = np.arccos(np.dot(eccentricity,self.position) / 
                      (norm(eccentricity)*norm(self.positionMag)))
        # Check orientation of True Anomaly
        if np.dot(self.position,self.velocity) < 0:
            f = 2*np.pi - f
        self.orbit_elements["True Anomaly"] = {"value": np.degrees(f), 
                                               "units": "degrees"}

        # Eccentric Anomaly
        # --------------------------------------------------------------------------------   
        ecc_anomaly = np.arccos((norm(eccentricity) + 
                      np.cos(f))/(1+norm(eccentricity)*np.cos(f)))
        self.orbit_elements["Eccentric Anomaly"] = {"value": np.degrees(ecc_anomaly), 
                                                    "units": "degrees"}

        # Mean Anomaly
        # --------------------------------------------------------------------------------   
        mean_anomaly = ecc_anomaly - norm(eccentricity)*np.sin(ecc_anomaly)
        self.orbit_elements["Mean Anomaly"] = {"value": np.degrees(mean_anomaly), 
                                               "units": "degrees"}

        # Period
        # --------------------------------------------------------------------------------   
        period = 2*np.pi / n
        self.orbit_elements["Period"] = {"value": (period)/(3600), 
                                         "units": "hours"}
 
    def get_energy_history(self) -> list:
        """
        Gets Specific Energy using numerical solution
        """

        time_indx = range(len(self.time))

        # Specific Energy as Array
        # -------------------------------------------------------------------------------- 
        # Vis-Viva Equation
        energy = [norm(self.vel_Numerical[t])**2/2 - self.mu/norm(self.pos_Numerical[t]) 
                  for t in time_indx]
            
        return energy

    def get_angular_momentum_history(self) -> list:
        """
        Gets Angular Momentum using numerical solution
        """

        time_indx = range(len(self.time))

        # Specific Angular Momentum as Array
        # --------------------------------------------------------------------------------   
        ang_momentum = [np.cross(self.pos_Numerical[t],self.vel_Numerical[t]) 
                        for t in time_indx]
    
        return ang_momentum

    def differential_equations(self,t,state:list) -> np.ndarray:

        pos = state[0:3]
        vel = state[3:]

        # Compute Differential Equation Constants   
        constant = -self.mu/(norm(pos)**3)

        # Differential Equations
        accel = np.dot(constant,pos)

        # Return d/dt vector of
        # [x, y, z, vx, vy, vx]
        return np.concatenate((vel,accel))

    def solve_twoBody_trajectory(self,saveAnalysis=False) -> None:
        # Here it is important that ivp has the following setup
        # [x, y, z, vx, vy, vx]
        ivp = self.initialValueProblem

        self.num_sol = solve_ivp(self.differential_equations,[self.time[0],self.time[-1]],
                                 ivp,t_eval=self.time,rtol=self.relTol,atol=self.absTol)

        # Extract Position and Velocity Results
        self.pos_Numerical = self.num_sol.y[:3,:].T
        self.vel_Numerical = self.num_sol.y[3::,:].T

        # Check if solver reached interval end or a termintion event occured 
        print("Solver Success:  ", self.num_sol.success)
        if not self.num_sol.success:
            print("Solver termination status:  ", self.num_sol.status)

        # Allow user to save numerical anlaysis
        if saveAnalysis:
            with open(self.num_sol_picklefile, 'wb') as handle:
                pickle.dump(self, handle)

    def write_state_results(self):
        
        elements = self.orbit_elements
        
        # Robust method for spacing out output table
        max_name_width = len(max(elements.keys(),key=len)) + 4
        max_unit_width = len(max([elements[k]["units"] for k in elements.keys()],key=len)) + 4

        # Table Header
        header = ["{:<{nwidth}} {:>10} {:>{uwidth}}\n".format("Element", 
                                                              "Value", 
                                                              "Units",nwidth=max_name_width,
                                                                      uwidth=max_unit_width),
                  '-'*(max_name_width+12+max_unit_width)+'\n']

        # Setup Element Output
        lines = ["{:<{nwidth}} {:10.5g} {:>{uwidth}}\n".format(k, elements[k]["value"],
                                                                  elements[k]["units"],
                                                                  nwidth=max_name_width,
                                                                  uwidth=max_unit_width) 
                                                                  for k in elements]

        f = open(self.resultsOut,"w")
        f.write("Initial State Vectors:\n")
        f.write("-"*40+"\n")
        f.write('Position = {} km\n'.format(self.position))
        f.write('Velocity = {} km/sec\n\n\n'.format(self.velocity))
        f.write("Computed Results\n")
        f.writelines(header)
        f.writelines(lines)
        f.close()

        print("Saved Calculated Orbit Elements to File: ",self.resultsOut)

class twoBodySTM(object):
    
    def __init__(self,pos_vector:"km",vel_vector:"km/s",initialPhis):

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.num_sol_picklefile = "twoBody_STM.pickle"        

        # Set Gravitational Constant
        # --------------------------------------------------------------------------------   
        self.mu = 398600 # km^3/sec^2

        # Set Position and Velocity Vector
        # --------------------------------------------------------------------------------   
        # Assumed input is in SI units (km, sec)    
        self.initial_position = pos_vector
        self.initial_velocity = vel_vector

        # Set State Transition Matrix
        # --------------------------------------------------------------------------------   
        # Reshape for planar case
        # if initialPhis.ndim > 1:
            # initialPhis = initialPhis.reshape(16)
        self.initial_phis = initialPhis

        self.initial_positionMag = norm(pos_vector)
        self.initial_velocityMag = norm(vel_vector)

        # Numerical Analysis Setup
        # --------------------------------------------------------------------------------
        self.initial_value_problem = pos_vector + vel_vector + list(initialPhis)
        # Default tolerance values
        self.absTol = 1e-12
        self.relTol = 1e-12

    def differential_equations_STM(self,t,state:list) -> np.ndarray:

        x,y,z, vx,vy,vz, *phi = state
        pos = [x,y,z]

        # State Transition Matrix, for 3 Dimensions
        phi_matrix = np.reshape(phi,(6,6))

        # Compute Differential Equation Constants:
        # Distance between Two Bodies
        r = math.sqrt(x**2 + y**2 + z**2)

        # Compute Differential Equation Constants   
        constant = -self.mu/(norm(pos)**3)

        # Differential Equations
        accel = np.dot(constant,pos)

        # Jacobian Partials
        axx = -(self.mu/r**3) + (3*self.mu*x*x)/r**5
        ayy = -(self.mu/r**3) + (3*self.mu*y*y)/r**5
        azz = -(self.mu/r**3) + (3*self.mu*z*z)/r**5

        axy = 3*self.mu*x*y/r**5
        axz = 3*self.mu*x*z/r**5
        ayz = 3*self.mu*y*z/r**5

        # Jacobian in Matrix form for 3 Dimensional
        # Note axy = ayx, axz = azx, ayz = azy
        a = np.array([[   0,   0,   0,   1,   0,   0],
                      [   0,   0,   0,   0,   1,   0],
                      [   0,   0,   0,   0,   0,   1],
                      [ axx, axy, axz,   0,   0,   0],
                      [ axy, ayy, ayz,   0,   0,   0],
                      [ axz, ayz, azz,   0,   0,   0]])

        # STM Differentail Equations
        phi_dot = a@phi_matrix
        
        return np.concatenate(([vx,vy,vz],accel,np.reshape(phi_dot, 36)))

    def solve_twoBody_problem(self,saveAnalysis=False) -> None:

        # Here it is important that ivp has the following setup
        # [x, y, z, vx, vy, vx, phi11, phi12, phi13, phi21, ...]
        ivp = self.initial_value_problem
        
        self.num_sol = solve_ivp(self.differential_equations_STM,
                                    [self.time[0],self.time[-1]],ivp,
                                    t_eval=self.time,
                                    rtol=self.relTol,atol=self.absTol)

        # Check if solver reached interval end or a termintion event occured 
        print("Solver Success:  ", self.num_sol.success)
        if not self.num_sol.success:
            print("Solver termination status:  ", self.num_sol.status)

        # Extract Position, Velocity, and STM Results
        self.position_numerical = self.num_sol.y[:3,:].T
        self.velocity_numerical = self.num_sol.y[3:6,:].T
        self.phis_numerical = self.num_sol.y[6:,:].T

        # Allow user to save numerical anlaysis
        if saveAnalysis:
            with open(self.num_sol_picklefile, 'wb') as handle:
                pickle.dump(self, handle)    
