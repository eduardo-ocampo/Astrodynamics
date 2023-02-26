""" --------------------------------------------------------------------------
            Example of Solving the Non-Dimensional Circular Restricted 
            Three-Body Problem (CR3BP)

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """


import numpy as np
import three_body_problem as three_body_problem

import plots_dev as plt

# Initial State Vectors
# --------------------------------------------------------------------------------
initial_pos = [0.50, 0.50, 0.0]
initial_vel = [0.01, 0.01, 0.0]

# Instantiate CR3BP Object:
# --------------------------------------------------------Æ------------------------
# Set Earth-Moon Mass Ratio
mu = 0.012150515586657583
sc = three_body_problem.cr3bp(initial_pos,initial_vel)
sc.mu = mu

# Numerical Analysis Setup
# --------------------------------------------------------------------------------
sc.time = np.linspace(0, 2*np.pi*4, 10000)

# Run Numerical Analysis: scipy.integrate methods
# --------------------------------------------------------------------------------
# Set up tolerances, relative & absolute
sc.relTol = 1e-12
sc.absTol = 1e-13

# Run scipy solver 
# --------------------------------------
sc.solve_threeBody_trajectory(saveAnalysis=False)

# Extract Results
position_numerical = sc.position_numerical
velocity_numerical = sc.velocity_numerical

# Generate Plots
# --------------------------------------------------------------------------------
plt.plot_cr3bp_example(sc)
