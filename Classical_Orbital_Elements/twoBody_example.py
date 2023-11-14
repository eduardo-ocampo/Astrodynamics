""" --------------------------------------------------------------------------
            Example of Solving the Two-Body Problem

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import numpy as np
import twoBody_problem

# Initial State Vectors
# --------------------------------------------------------------------------------
position = [5000, 100, 0] # km
velocity = [1, 10, 5] # km/s

# Instantiate Object: For this example consider a spacecraft oribiting Earth
# --------------------------------------------------------------------------------
# Earth Gravitation Constant
mu = 398600 # km^3/sec^2

satellite = twoBody_problem.twoBody(position,velocity)
satellite.mu = mu

# Get Initial State Elements
# --------------------------------------------------------------------------------
satellite.get_state_elements()
# Determine orbital period
period = satellite.orbit_elements["Period"]["value"] # Hours
satellite.period = period
print("Period: ",period, " hours")

# Numerical Analysis Setup
# --------------------------------------------------------------------------------
# Set upper time bond of 20 orbital periods
time_ub = 20*period*3600 # convert hrs to seconds 
# Take 10 minute steps
time_step= 15*60 # convert mins to seconds 
satellite.time = np.arange(0, time_ub, time_step)

# Run Numerical Analysis: scipy.integrate methods
# --------------------------------------------------------------------------------
# Set up tolerances, relative & absolute
satellite.relTol = 1e-10
satellite.absTol = 1e-12

# Run scipy analysis 
# --------------------------------------
satellite.solve_twoBody_trajectory()

pos_Numerical = satellite.pos_Numerical
vel_Numerical = satellite.vel_Numerical

# Calculate Specific Energy History
# --------------------------------------------------------------------------------   
satellite.energyHistory = satellite.get_energy_history()

# Calculate Specific Angular Momentum History
# --------------------------------------------------------------------------------   
satellite.ang_momentumHistory = satellite.get_angular_momentum_history()

# Calculate Allitude and Veloctiy at Periapsis & Apoapsis
# -------------------------------------------------------------------------------- 
# Get relavent orbital parameters
a = satellite.orbit_elements["Semi-Major Axis"]["value"]
e = satellite.orbit_elements["Eccentricity"]["value"] 
h = satellite.orbit_elements["Specific Angular Momentum"]["value"]

# Allitudes
rp = a*(1-e)
ra = a*(1+e)

# Velocities
# va = h/ra, vp = h/rp
vp = np.sqrt((mu/a)*((1+e)/(1-e)))
va = np.sqrt((mu/a)*((1-e)/(1+e)))