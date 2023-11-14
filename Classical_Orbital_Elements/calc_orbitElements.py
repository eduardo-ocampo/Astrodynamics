import math
from twoBody_problem import twoBody

mu = 398600

# Initial Position and Velocity Vectors
position = [5000, 100, 0] # km

vy = math.sqrt(mu/position[0])+1
velocity = [1, vy, 1] # km/s

# Instantiate orbitElements Class
orbitElements = twoBody(position,velocity)
orbitElements.resultsOut = "example.results"

# Calculate Orbital Elements and Save Results Out
orbitElements.get_state_elements()
orbitElements.write_state_results()