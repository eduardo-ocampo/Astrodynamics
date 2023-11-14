# Calculating Orbit Elements with Python

TODO: Rerun this using new twoBody_problem.py scripts

Consider the Two-Body Problem:

:::{math}
:label: eq:Two_Body_EOM
\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}
:::

In this example we will compute the follow orbit properties:

1. [Classical Orbit Elements](Classical_Orbit_Elements.md)
2. [Specific Energy](Integrals_Of_Motion.md#4-specific-energy)
3. [Specific Angular Momentum](Integrals_Of_Motion.md#1-magnitude-of-angular-momentum)
4. Period
5. True Anomaly

## Example

Let us assume we have the following information about a spacecraft's position and velocity at some time $t_0$ orbiting Earth ($\mu = 398,600 \frac{km^3}{sec^2}$). 

In the relative coorindate frame the position and velocity vectors are:

:::{math}
:label:
\mathbf{r}(t_0) = 
\begin{bmatrix}
5000 \\
100  \\
0
\end{bmatrix} km
::: 

:::{math}
:label:
\mathbf{v}(t_0) = 
\begin{bmatrix}
1 \\
\sqrt{\frac{\mu}{x_0}} + 1  \\
1
\end{bmatrix} \frac{km}{sec}
::: 

Determine the spacecraft's orbital properties using Python package [twoBodyProblem.py](https://github.com/thatguyeddieo/Astrodynamics-Workspace/blob/main/Classical_Orbital_Elements/twoBodyProblem.py)

Begin by importing module ``twoBodyProblem`` and defining the postion and velocity vector. Instantiate class ``orbitElements()`` with the initial state vector. Calling method ``orbitElements.getElements()`` will calculate orbital properities for the state vector while ``orbitElements.writeResults()`` will write out the results. Package ``twoBodyProblem.py`` writes the calulated orbital properites results to orbitElements.txt and can be overwritten by reassigning attribute ``resultsOut``.

## Script Setup

```python
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
```

## Output

**Example.results file contents**

```
Initial State Vectors:
----------------------------------------
Position = [5000, 100, 0] km
Velocity = [1, 9.928605714219886, 1] km/sec


Computed Results
Element                            Value          Units
-------------------------------------------------------
Position Magnitude                  5001             km
Velocity Magnitude                10.029         km/sec
Specific Energy                  -29.415     km^2/sec^2
Specific Angular Momentum          49795       km^2/sec
Eccentricity                     0.28615               
Inclination                       5.7641        degrees
Long. of Ascend. Node (Ω)         1.1458        degrees
Argument of Perigee (ω)           328.46        degrees
Semi-Major Axis                   6775.3             km
Mean Motion                    0.0011321        rad/sec
True Anomaly                      31.544        degrees
Eccentric Anomaly                 23.766        degrees
Mean Anomaly                      17.159        degrees
Period                            1.5417          hours

```


## Exposing Script Methods

All code blocks below are references to method ``orbitElements.getElements()``. 

The state vector magnitudes are calulcated  using [numpy.linalg.norm](https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html)

```python
from numpy.linalg import norm
v = norm(posVector)
r = norm(velVector)
```

The first two properities to compute are Specific Energy and Specific Angular Momentum.

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


### Specific Anguluar Momentum 

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

Knowing the Angular Momentum the following elements came be determined.

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

The Ascending Node Vector is defined as:

:::{math}
\mathbf{\hat{n}} = \hat{\mathbf{z}} \times \hat{\mathbf{h}}
:::

```python
# Ascending Node Vector 
# --------------------------------------------------------------------------------   
node_vec = np.cross([0,0,1],ang_momentum)
```

### Longitude of Ascending Node

In Astrodynamics the Longitude of Ascending Node is define to be betwewn 0$^{\circ}$ and 360$^{\circ}$. To solve for the angle we must perform a quadrant check due to its trigometric definition. By looking at the y-component of the Node Vector ($\mathbf{\hat{n}_y}$).

If $\mathbf{\hat{n}_y} \geq 0^{\circ}$ then $\mathbf{\Omega}$ lies between I and II quadrants, otherwise if $\mathbf{\hat{n}_y} \leq 0^{\circ}$ then $\mathbf{\Omega}$ lies between III and IV quadrants,

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


### Argument of Perigee 

The Argument of Periapsis is defined as the angled between the Node Vector ($\mathbf{n}$) and Eccentcity Vector ($\mathbf{e}$). It has a range of $0^\circ \lt \omega \lt 360^\circ$ and points towards periapsis. To solve for the angle a quadrant check is required by looking at z-component of the Eccentrcity Vector.

:::{math}
\mathbf{\omega} = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{n}\cdot\mathbf{e}}{|\mathbf{n}||\mathbf{e}|}\right) & e_z \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{n}\cdot\mathbf{e}}{|\mathbf{n}||\mathbf{e}|}\right) & e_z < 0^{\circ}
\end{cases}
:::

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

### Semi-major Axis

For a bound orbit, such as an elliptical orbit, looking at the specific energy equation at apsides the semi-major axis can be derivied:

:::{math}
\varepsilon = -\frac{\mu}{2a}
:::

:::{math}
a = -\frac{\mu}{2\varepsilon}
:::

```python
# Semi-major Axis
# --------------------------------------------------------------------------------   
a = -self.mu/(2*energy)
self.orbit_elements["Semi-Major Axis"] = {"value": a, 
                                          "units": "km"}
```

### True Anomaly

The True Anomaly is defined as the angle between the line of apse ($\mathbf{e}$) and the position vector. It has a range of $0^\circ \lt \nu \lt 360^\circ$ 

:::{math}
\nu = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{e}\cdot\mathbf{r}}{|\mathbf{e}||\mathbf{r}|}\right) & \mathbf{r}\cdot\mathbf{v} \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{e}\cdot\mathbf{r}}{|\mathbf{e}||\mathbf{r}|}\right) & \mathbf{r}\cdot\mathbf{v}  < 0^{\circ}
\end{cases}
:::

```python
# True Anomaly
# -------------------------------------------------------------
f = np.arccos(np.dot(eccentricity,self.position) / 
              (norm(eccentricity)*norm(self.positionMag)))
# Check orientation of True Anomaly
if np.dot(self.position,self.velocity) < 0:
    f = 2*np.pi - f
self.orbit_elements["True Anomaly"] = {"value": np.degrees(f), 
                                       "units": "degrees"}
```

### Period

```python
# Period
# --------------------------------------------------------------------------------   
period = 2*np.pi / n
print(period)
self.orbit_elements["Period"] = {"value": (period)/(3600), 
                                 "units": "hours"}
```