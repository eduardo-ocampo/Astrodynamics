---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Integrals of Motion 
 
As discussed in [the Two-Body Problem](Two_Body_Problem.md), Integrals of Motion are used to derive properties  of Two-Body Motion without having to solve the equations of motion. For a relative dynamic system, there are 6 Integrals of Motion to solve which are constant along the trajectory of motion.

## Conservation of Angular Momentum

The specific angular momentum vector $\mathbf{h}$ is defined as:

:::{math}
:label: angular_momentum
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

where
$\mathbf{r}$ is the position vector,
$\mathbf{v}$ is the velocity vector and both are 3x1 Vectors.

To show that the angular momentum vector is an integral of motion, take the total time derivative of $\mathbf{h}$ and show that $\frac{d}{dt}\left({\mathbf{h}}\right) = 0$:

:::{math}
:label:
{}

\frac{d}{dt}\left({\mathbf{h}}\right) = \frac{d}{dt}{(\mathbf{r}\times\mathbf{v})}

:::

:::{math}
{}

\frac{d}{dt}\left({\mathbf{h}}\right) = \frac{d}{dt}\left({\mathbf{r}}\right) \times \mathbf{v} + \mathbf{r} \times  \frac{d}{dt}\left({\mathbf{v}}\right)

:::

Recall

:::{math}

\frac{d}{dt}\left({\mathbf{v}}\right) = \ddot{\mathbf{r}} = -G\frac{(m_1+m_2)}{r^3}\mathbf{r}

:::

In other words

:::{math}
\mathbf{r} \times \frac{d}{dt}\left({\mathbf{v}}\right) = 0
:::

:::{math}
\frac{d}{dt}\left({\mathbf{r}}\right) \times \mathbf{v} = 0
:::

:::{math}
{}

\frac{d}{dt}\left({\mathbf{h}}\right) = \mathbf{v} \times \mathbf{v} + \mathbf{r} \times  \mathbf{\ddot{r}}
:::

Thus
:::{math}
:label:
\frac{d}{dt}\left({\mathbf{h}}\right) = 0
:::

Since our Angular Momentum Vector ($\mathbf{h}$) is a 3x1 vector, this gives us 3 integrals of motions to work with. $\mathbf{h}$ can be represented using two angles and its magnitude. 

Thus the first 3 Integrals of Motion are: 

1. Magnitude of Angular Momentum (h)
2. Inclination (i)
3. Longitude of Ascending Node ($\Omega$)


```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_long_acsend_node
fig4 = elliptic_orbit_long_acsend_node.plot()
fig4.update_layout(title={'text':"<b>First Three Integrals of Motion (h,i Ω)<b>"})
glue("lan_fig",fig4)
```

```{glue:figure} lan_fig
:align: center
:name: iom_Figure_1
**Figure 3.1.** Example Orientation of Angular Momentum Vector in an Elliptical Orbit
```

Note: The Ascending Node Vector is sometimes referred to as the Node Vector. It is defined as $\mathbf{\hat{n}_\Omega}$:

:::{math}
:label:
\mathbf{\hat{n}_\Omega} = \hat{\mathbf{z}} \times \hat{\mathbf{h}}
:::


### 1. Magnitude of Angular Momentum

The first Integral of Motion to determine is the Magnitude of Angular Momentum (h) using Equation {eq}`angular_momentum`

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

Note that $\mathbf{h}$ = h$\hat{\mathbf{h}}$, where

:::{math}
:label:
\hat{\mathbf{h}} = \frac{\mathbf{r}\times\mathbf{v}}{|\mathbf{r}\times\mathbf{v}|}
:::

### 2. Inclination

The Inclination of an orbit is defined as the angle measuring the tilt of the orbit around the primary body. From [Figure 3.1](iom_Figure_1) it is shown as the the angle between the reference vector $\mathbf{\hat{z}}$ and unit Specific Angular Momentum vector $\mathbf{\hat{h}}$.

:::{math}
\hat{\mathbf{h}} \cdot \hat{\mathbf{z}} = cos(i)
:::

In Astrodynamics the Inclination is restricted between 0$^\circ$ $\le$ i $\le$ 180$^\circ$. 


:::{math}
:label:
i = cos^{-1}\left({\hat{\mathbf{h}} \cdot \hat{\mathbf{z}}}\right)
:::

Or,

:::{math}
:label: inclination
i = \cos^{-1}\left(\frac{h_z}{|\mathbf{h}|}\right)
:::

There are convetions for common inclinations angles that will be discribed in other sections: TODO: Write and reference futre docs. 

TODO: Consider including a figures/animations here. Already created file elliptic_orbit_inclination_types.py which can be converted to animation

:::{math}
:label: raan_cases
i = \begin{cases}
i = 0.0^{\circ} & \text{Prograde Orbit - within the Reference Plane} \\
0^{\circ} \lt i \lt 90^{\circ} & \text{Prograde Orbit} \\
i = 63.4^{\circ} & \text{Critical Inclination - spacecraft with zero apogee drift} \\
i = 90.0^{\circ} & \text{Polar Orbit, spacecraft passes over the poles of the primary body} \\
90.0^{\circ} \lt i \le 180.0^{\circ} & \text{Retrograde Orbit} \\
\end{cases}
:::


### 3. Longitude of Ascending Node

The Longitude of Ascending Node is the angle between $\mathbf{\hat{x}}$ and Node Vector $\mathbf{\hat{n}}$. 

:::{math}
:label: orbital-elements-Omega
\mathbf{\Omega} = \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right)
:::

```{figure} ./images/laan_reference.png
:align: center
:name: iom_Figure_2
**Figure 3.2**
```

This Integral of Motion is also known as the Right Ascension of the Ascending Node (RAAN). The Ascending Node is the intesection of the orbit and the reference plane as shown in Figure 3.2. Thus the Right Ascension of the Ascending Node is the angle at which the spacecraft ascends through and above the "plane of reference". 

In Astrodynamics the Longitude of Ascending Node is define to be betwewn 0$^{\circ}$ and 360$^{\circ}$. To solve for the angle we must perform a quadrant check due to its trigometric definition. By looking at the y-component of the Node Vector ($\mathbf{\hat{n}_y}$).

TODO: See how codes work either use x or nx, y or ny

If $\mathbf{\hat{n}_y} \geq 0^{\circ}$ then $\mathbf{\Omega}$ lies between I and II quadrants, otherwise if $\mathbf{\hat{n}_y} \leq 0^{\circ}$ then $\mathbf{\Omega}$ lies between III and IV quadrants,

:::{math}
:label: raan_cases
\mathbf{\Omega} = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} < 0^{\circ}
\end{cases}
:::



## Conservation of Energy 
E

The specific Energy ($\varepsilon$) of the Two-Body system is defined as:

Note: Scalars
:::{math}
:label: energy
\varepsilon = \frac{v^2}{2} - \frac{\mu}{r}
:::

To show that the Energy is an integral of motion, start by taking a dot product of our EOMs with respect to Velcoty.

EOMs {eq}`Two_Body_EOM`:

:::{math}
\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}
:::


:::{math}
\left(\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}\right) \cdot \mathbf{v}
:::

:::{math}
\mathbf{\ddot{r}} \cdot \mathbf{v} = -\frac{\mu}{r^3}\mathbf{r} \cdot \mathbf{v}
:::


:::{math}

\frac{\mathbf{\ddot{r}}\cdot\mathbf{\dot{r}} + \mathbf{\dot{r}}\cdot\mathbf{\ddot{r}}}{2} =  -\frac{\mu}{2r^3}\left( \mathbf{\dot{r}}\cdot\mathbf{r} + \mathbf{r}\cdot\mathbf{\dot{r}}\right)

:::

Take the integral of both sides:

:::{math}
{}

\frac{d}{dt}\left({\frac{\mathbf{\dot{r}}\cdot\mathbf{\dot{r}}}{2}}\right) = \frac{d}{dt}\left(\frac{\mu}{r}\right)

:::

:::{math}
{}

\frac{d}{dt}\left({\frac{\mathbf{v}\cdot\mathbf{v}}{2}} - \frac{\mu}{r}\right) = 0

:::

Thus:

:::{math}
:label:
\varepsilon = \frac{v^2}{2} - \frac{\mu}{r} = Constant
:::

This form of the Energy Equation is know for deriving the Vis-Viva Equation in Astrodynamics. (Since equal we can set equal to other points in traject for example va/ra = vp/rp energies) The Vis-Viva equation relates the... Talk more about this and introduce the Vis-Viva Equation

Properites of Specific Energy:



:::{math}
:label: eq:raan_cases
\varepsilon = \begin{cases}
\varepsilon \lt 0.0 & \text{Orbit is bound: Elliptical Orbit}\\
\varepsilon = 0.0   & \text{Orbit is escaped: Parabolic Orbit} \\
\varepsilon \gt 0.0 & \text{Orbit is escaped: Hyperbolic Orbit}
\end{cases}
:::


## Eccentricity Vector

The Eccentricity Vector ($\mathbf{e}$) is defined as:

:::{math}
:label: eccentricity_vector
\mathbf{e} = \frac{1}{\mu}\left(\mathbf{v}\times\mathbf{h}\right) - \frac{\mathbf{r}}{r}
:::

To show that the Eccentricity Vector is an integral of motion, take a cross-product of our EOM with respect to Angular Momemtum ($\mathbf{h}$)

EOMs {eq}`Two_Body_EOM`:

:::{math}
\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}
:::


:::{math}
\left(\ddot{\mathbf{r}} = -\frac{\mu}{r^3}\mathbf{r}\right) \times \mathbf{h}
:::


:::{math}
\mathbf{\ddot{r}} \times \mathbf{h} = -\frac{\mu}{r^3}\mathbf{r} \times \mathbf{h}
:::


:::{math}
\mathbf{\ddot{r}} \times \mathbf{h} = -\frac{\mu}{r^3}\mathbf{r} \times \left(\mathbf{r} \times \mathbf{v}\right)
:::

Apply [Vector Triple Product](https://en.wikipedia.org/wiki/Triple_product):

:::{math}
\mathbf{\ddot{r}} \times \mathbf{h} = -\frac{\mu}{r^3} \left[\mathbf{r}\left(\mathbf{r}\cdot\mathbf{v}\right) - \mathbf{v}\left(\mathbf{r}\cdot\mathbf{r}\right) \right]
:::

:::{math}
{}

\frac{d}{dt} \left(\mathbf{v}\right)\times\mathbf{h} = \mu\cdot\frac{d}{dt}\left(\frac{\mathbf{r}}{r}\right)

:::

Integrate both sides to get:

:::{math}
:label:
\mathbf{v}\times\mathbf{h} = \mu\frac{\mathbf{r}}{r} + \mathbf{C}
:::

Where $\mathbf{C}$ is a constant vector. The constant vector has the same dimensions as $\mu$, thus we can transform it into a dimensionless number by dividing Equation XXX by $\mu$ and defining the Eccentricity Vector as $\mathbf{e} = \frac{\mathbf{c}}{\mu}$

Finally, we can rewrite our Eccentcity Vector as:

:::{math}
\mathbf{e} = \frac{1}{\mu}\left(\mathbf{v}\times\mathbf{h}\right) - \frac{\mathbf{r}}{r}
:::


Some Notes:

By inspection it is known that constant vector $\mathbf{c}$ lies in the orbital plane. Therefore, the Eccentricity Vector also lies in the orbital plane. Althought $\mathbf{e}$ is a 3x1 Vector it's magnitude is define by components of Node Vector ($\mathbf{\hat{n}_\Omega}$,  $\mathbf{\hat{n}_T}$) which are already account for in defining hte Longtidue of Ascending Node (LINK HERE). The only extra integral of motion comes from the orientation of $\mathbf{e}$. This is know as the Argument of Periapsis ($\omega$). 

### The Argument of Periapsis

Mention it's range and maybe have animation.


### The Trajectory Equation

From the Eccentricty Vector the trajectory equation cab be derived by taking the dot product of Position Vector ($\mathbf{r}$) with the Eccentricity Vector ($\mathbf{e}$).

:::{math}
\mathbf{r}\cdot\left[ \mathbf{e} = \left( \frac{\mathbf{v}\times\mathbf{h}}{\mu} - \frac{\mathbf{r}}{r} \right) \right]
:::

:::{math}
\mathbf{r}\cdot\mathbf{e} = \left( \frac{\left(\mathbf{v}\times\mathbf{r}\right)\cdot\mathbf{h}}{\mu} - {r} \right) 
:::

Here show a diagram of some sort that defines True Anomally (f/v)

:::{math}
\mathbf{r}\cdot\mathbf{e} = re\cos{f}
:::

Recall 

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

:::{math}
re\cos{f} = \frac{h^2}{\mu} - r
:::

:::{math}
r\left( 1 + e\cos{f} \right) = \frac{h^2}{\mu}
:::

:::{math}
r = \frac{h^2}{\mu} \frac{1}{\left( 1 + e\cos{f} \right)}
:::

Define $p$ which is the Semi-lastus Rectrum

:::{math}
p = \frac{h^2}{\mu}
:::

Thus the Trajector Equation as a function of True Anomally is:
https://en.wikipedia.org/wiki/True_anomaly

:::{math}
r(f) = \frac{p}{\left( 1 + e\cos{f} \right)} = 
:::

Write something here about Trajector Equation 
https://en.wikipedia.org/wiki/Kepler_orbit

The trajectory equation deines the geometry of a conic section. Which describes four different orbit types for the Two-Body Problem:

Good idea to have some figures here


Change this format to something better

:::{math}
\text{Oribt Type} = \begin{cases}
e = 0.0   & \text{Circular Orbit} \\
0.0 \lt e \lt 1.0 & \text{Elliptical Orbit} \\
e = 1.0   & \text{Parabolic Orbit} \\
e \gt 1.0 & \text{Hyperbolic Orbit} \\
\end{cases}
:::


## Kepler's Law
to

Write about where they come from and describe the 6 that come out
Talk about how we go from state vector to itegrals of motion






## Python Examples

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

#### Script Setup

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

