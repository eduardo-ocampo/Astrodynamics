import math
from twoBodyProblem import orbitElements

mu = 398600

# Initial Position and Velocity Vectors
position = [5000, 100, 0] # km

vy = math.sqrt(mu/position[0])+1
velocity = [1, vy, 1] # km/s

# Instantiate orbitElements Class
orbitElements = orbitElements(position,velocity)
orbitElements.resultsOut = "Example.results"

# Calculate Orbital Elements and Save Results Out
orbitElements.getElements()
orbitElements.writeResults()