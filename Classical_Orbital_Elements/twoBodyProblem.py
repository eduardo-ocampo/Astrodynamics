import math
import numpy as np
from numpy.linalg import norm

class orbitElements(object):

    def __init__(self,posVector,velVector):
        # Set Gravitational Constant
        # --------------------------------------------------------------------------------   
        # Default Set to Earth
        self.mu = 398600 # km^3/sec^2

        # Set Position and Velocity Vector
        # --------------------------------------------------------------------------------   
        # Assumed input is in SI units (km, sec)    
        self.position = posVector
        self.velocity = velVector

        self.positionMag = norm(posVector)
        self.velocityMag = norm(velVector)

        # Initialize Orbit Element Dictionary
        # --------------------------------------------------------------------------------           
        self.orbit_elements = {"Position Magnitude":{"value": norm(posVector),
                                                     "units": "km"},
                               "Velocity Magnitude":{"value": norm(velVector),
                                                     "units": "km/sec"}}

        # Set File Names
        # --------------------------------------------------------------------------------   
        self.resultsOut = "orbitElements.txt"

        # Meta Data
        # --------------------------------------------------------------------------------   
        self.linebreak = "-"*70

    def getElements(self):

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
        print(mean_anomaly)
        self.orbit_elements["Mean Anomaly"] = {"value": np.degrees(mean_anomaly), 
                                               "units": "degrees"}

        # Period
        # --------------------------------------------------------------------------------   
        period = 2*np.pi / n
        print(period)
        self.orbit_elements["Period"] = {"value": (period)/(3600), 
                                         "units": "hours"}


        return

    def writeResults(self):
        
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

        return
