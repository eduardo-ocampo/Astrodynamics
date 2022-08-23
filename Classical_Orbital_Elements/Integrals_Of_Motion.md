
# Integrals of Motion 
 
Integrals of Motion are used to derive properities of Two-Body Motion without having to solve the equations of motion. They are constant along the trajectory of motion.

## Conservation of Angular Momentum

The specific angular momentum vector $\mathbf{h}$ is defined as:

:::{math}
:label: angular_momentum
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

where
$\mathbf{r}$ is the position vector,
$\mathbf{v}$ is the velocity vecot and both are 3x1 Vectors.

To show that the angular momentum vector is an integral of motion, take the total time derivative of $\mathbf{h}$:

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

Since our angular moementum vecotr ($\mathbf{h}$) is a 3x1 vector, this gives us 3 integrals of motions to work with.

Here we can segway to Slide 10 of notes. Create an animation showing i, h, Omega. Talk about them and the node vector plane (definition) n = kxh


### Angular Momemtum

The first Integral of Motion to determine is Angular Momentum {eq}`angular_momentum`

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

### Inclination

Next we define the Inclination of the orbit to be the angle measuring the tilt of the orbit around it's "celetisal" body. For our diagram this is it is from the reference vector $\mathbf{\hat{z}}$ and unit Specific Angular Momentum vector $\mathbf{\hat{h}}$

In Astrodynamics the Inclination is restricted between 0$^\circ$ and 180$^\circ$. 

:::{math}
:label: inclination
i = \cos^{-1}\left(\frac{\mathbf{\hat{z}}}{\mathbf{\hat{h}}}\right)
:::

There are convetions for common inclinations angles:
From Wiki: (re write and reference future docs)

Might want to include figures/animations here depending on how are they are

:::{math}
:label: raan_cases
\mathbf{i} = \begin{cases}
0^{\circ} \lt \mathbf{i} \lt 90^{\circ} & \text{Prograde Orbit} \\
\mathbf{i} = 0.0^{\circ} & \text{Prograde Orbit within the "reference plane"} \\
\mathbf{i} = 63.4^{\circ} & \text{Critical inclination, when describing artificial - satellites orbiting the Earth, because they have zero apogee drift WIKI Refe} \\
\mathbf{i} = 90.0^{\circ} & \text{Polar Orbit, in which the "spacecraft" passes over the poles of the planet} \\
90.0^{\circ} \lt \mathbf{i} \le 180.0^{\circ} & \text{Retrograde Orbit} \\
\end{cases}
:::


### Longitude of Ascending Node

The Longitude of Ascending Node is the angle between $\mathbf{\hat{x}}$ and Node Vector $\mathbf{\hat{n}}$. It is also known as the Right Ascension of the Ascending Node (RAAN). The Ascending Node is the intesection of the orbit and the reference plane. Thus the Right Ascension of the Ascending Node is the angle at which the "sat" "orbit" ascends through and above the "plane of reference". 

Maybe have figure/animation here

:::{math}
:label: orbital-elements-Omega
\mathbf{\Omega} = \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right)
:::

In Astrodynamics the Longitude of Ascending Node is define to be betwewn 0$^{\circ}$ and 360$^{\circ}$. To solve for the Longitude of Ascending Node we must perform a quadrant check due to its trigometric definition. By looking at the y-component of the Node Vector ($\mathbf{\hat{n}_y}$).

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

Define the trajectory equation based off of notes, I think there was a HW problem that derivied it. 


## Kepler's Law
to

Write about where they come from and describe the 6 that come out
Talk about how we go from state vector to itegrals of motion






## Python Examples

Provide some intro, what position and velocity vector we'll be using. As Elements are shown consider writing out outputs and then summarizing at the end of them all. Talk about what units are assume (SI) km/s etc. 

Consider a statelitte orbiting earth. Let's assume we have recieved the following data about it's position and velocity vector at some time $t$. 

```
Postion:  [1000, 1000, 0] km

Velocity: [1000, 1000, 0] km/sec

```

In the inertial coorindate frame this can be written as:

:::{math}
\mathbf{r} = 1000 \space \mathbf{\hat{i}} + 1000 \space \mathbf{\hat{j}} + 0.0 \space \mathbf{\hat{k}} \space \space {km}
:::

:::{math}
\mathbf{v} = 1000 \space \mathbf{\hat{i}} + 1000 \space \mathbf{\hat{j}} + 0.0 \space \space \mathbf{\hat{k}} \space \space \frac{km}{s}
:::

Let's determine the Sat's Orbital Elements using Python package twoBodyProblem.py





All code blocks below are refereenced from Class orbitElements() in `twoBodyProblem.orbitElements()`. 

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