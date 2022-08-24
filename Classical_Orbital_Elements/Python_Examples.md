# Python Examples


## Calculating Orbital Elements

Provide some intro, what position and velocity vector we'll be using. As Elements are shown consider writing out outputs and then summarizing at the end of them all. Talk about what units are assume (SI) km/s etc. 

Consider a statelitte orbiting earth. Let's assume we have recieved the following data about it's position and velocity vector at some time $t$. 


```
Postion:  [10000, 1000, 0] km

Velocity: [1, 6.324555, 1] km/sec

```


In the inertial coorindate frame this can be written as:

:::{math}
\mathbf{r} = 10000 \space \mathbf{\hat{i}} + 1000 \space \mathbf{\hat{j}} + 0.0 \space \mathbf{\hat{k}} \space \space {km}
:::

:::{math}
\mathbf{v} = 1.0 \space \mathbf{\hat{i}} + 6.324555 \space \mathbf{\hat{j}} + 1.0 \space \space \mathbf{\hat{k}} \space \space \frac{km}{s}
:::

Let's determine the Sat's Orbital Elements using Python package twoBodyProblem.py


Begin by importing moduel twoBodyProblem and defining the postion and state vector. Module twoBodyProblem.py requires an output file to be assigned as attribute `resultsOut`. Calling getElements() will calculate Orbital Elements of your State Vector while writeResults() will write out the results. 

### Script Setup

```python
import math
from twoBodyProblem import orbitElements

# Initial Position and Velocity Vectors
position = [10000, 1000, 0] # km
velocity = [1, 6.324555, 1] # km/s

# Instantiate orbitElements Class
orbitElements = orbitElements(position,velocity)
orbitElements.resultsOut = "Example.results"

# Calculate Orbital Elements and Save Results Out
orbitElements.getElements()
orbitElements.writeResults()
```

**Exampl.results File Contents**

```
Initial State Vectors:
----------------------------------------
Position = [10000, 1000, 0] km
Velocity = [1, 6.324555, 1] km/sec


Computed Results
Element                            Value          Units
-------------------------------------------------------
Position Magnitude                 10050             km
Velocity Magnitude                6.4807         km/sec
Energy                           -18.662     km^2/sec^2
Angular Momentum                   63052       km^2/sec
Eccentricity                     0.25706               
Inclination                       9.1716        degrees
Long. of Ascend. Node (Ω)         5.7106        degrees
Argument of Perigee (ω)           268.31        degrees
Semi-Major Axis                    10679             km
Mean Motion                   0.00057207        rad/sec
True Anomaly                       91.69        degrees
Eccentric Anomaly                 76.744        degrees
Mean Anomaly                      62.408        degrees
Period                            3.0509          hours

```



All code blocks below are refereenced from Class orbitElements() in `twoBodyProblem.orbitElements()`. 

Their magnitudes are calulcated in twoBodyProblem.py using ```from numpy.linalg import norm```

```python
from numpy.linalg import norm
v = norm(posVector)
r = norm(velVector)
```

### Anguluar Momentum 

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

Utilizes [NumPy](https://numpy.org/) packages to perfrom cross product. 

```python

# Specific Angular Momentum Vector
# --------------------------------------------------------------------------------  
ang_momentum = np.cross(self.position,self.velocity)
self.orbit_elements["Angular Momentum"] = {"value": norm(ang_momentum), 
                                           "units": "km^2/sec"}

```

### Inclination


:::{math}
i = \cos^{-1}\left(\frac{\mathbf{\hat{z}}}{\mathbf{\hat{h}}}\right)
:::

Utilizes [NumPy](https://numpy.org/) packages to perfrom inverser trigometric functions and dot product. np.arccos() returns the angle of the ray intersecting the unit circle at the given x-coordinate in radians (0, $\pi$).

```python

# Inclination
# --------------------------------------------------------------------------------
incl = np.arccos(np.dot([0,0,1],ang_momentum)/norm(ang_momentum))
self.orbit_elements["Inclination"] = {"value": np.degrees(incl), 
                                      "units": "degrees"}
```

### Ascending Node Vector 

Maybe add this?


### Longitude of Ascending Node


:::{math}
\mathbf{\Omega} = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} < 0^{\circ}
\end{cases}
:::

```python

# Longitude of Ascending Node (Ω)
# --------------------------------------------------------------------------------   
long_ascend_node = np.arccos(np.dot([1,0,0],node_vec)/norm(node_vec))

if node_vec[1] >= 0.0:
    lan = np.degrees(norm(long_ascend_node))
elif node_vec[1] < 0.0:
    lan = np.degrees(2*np.pi - norm(long_ascend_node))
self.orbit_elements["Long. of Ascend. Node (Ω)"] = {
                    "value": lan, 
                    "units": "degrees"}
```

### Specific Energy 

:::{math}
\varepsilon = \frac{v^2}{2} - \frac{\mu}{r}
:::

```python 
# Specific Energy
# --------------------------------------------------------------------------------   
energy = v**2/2 - self.mu/r 
self.orbit_elements["Energy"] = {"value": energy, 
                                 "units": "km^2/sec^2"}
```

### Eccentricity Vector

:::{math}
\mathbf{e} = \frac{1}{\mu}\left(\mathbf{v}\times\mathbf{h}\right) - \frac{\mathbf{r}}{r}
:::

```python 
# Eccentricity Vector
# --------------------------------------------------------------------------------   
eccentricity = (1/self.mu)*(np.cross(self.velocity,ang_momentum))-self.position/r
self.orbit_elements["Eccentricity"] = {"value": norm(eccentricity), 
                                        "units": " "}
```

### Argument of Perigee 


```python
# Argument of Perigee (ω)
# --------------------------------------------------------------------------------   
arg_peri = np.arccos(np.dot(node_vec,eccentricity) / 
                    (norm(eccentricity)*norm(node_vec)))
# Check ecc_zcomp
if eccentricity[-1] < 0:
    arg_peri = 2*np.pi - arg_peri
self.orbit_elements["Argument of Perigee (ω)"] = {"value": np.degrees(arg_peri), 
                                                    "units": "degrees"}
```
