# Orbit Elements


## The Two-Body Problem

Build up to this:
http://www.physics.drexel.edu/~steve/Courses/Physics-431/two-body.pdf
From Newton's Law of Gravitation (ref), the force of particle $P_1$ acting on particle $P_2$ in the intertial fram yields: 

Let r = r_2 - r_1

The Equation of Motion for the Two-Body Problem is:

:::{math}
:label: eq:Two_Body_EOM
\ddot{\mathbf{r}} = -G\frac{(m_1+m_2)}{r^3}\mathbf{r}
:::

where:

<!-- :::{math}
M = m_1 + m_2
::: -->

:::{math}
\mathbf{r} = \mathbf{r_{12}} = \mathbf{r_2} - \mathbf{r_1}
:::



State Vector:

:::{math}
:label: eq:state_vector
\mathbf{\bar{x}} = \begin{bmatrix} 
    \mathbf{x} \\ \mathbf{y} \\ \mathbf{z} \\
    \mathbf{\dot{x}} \\ \mathbf{\dot{y}} \\ \mathbf{\dot{z}}
\end{bmatrix}
:::

This is a second-order differential equation which requires solving 6 intergrals of motion. Which have become to be known as the Classical Orbital Elements. They can be found solved by positions, velocities, and times that remain constant under the motion governed by the equations of motion.

##### Classical Orbital Elements

:$a$: Semi-Major Axis
:$e$: Eccentricity
:$i$: Incliniation
:$\Omega$: Longitude of Ascending Node
:$\omega$: Argument of Periapsis
:$t_0$: Time of Periapsis Passage

They can be broken down even further as to how they define the shape, and size of the orbit, orientation of orbital plane, and definition of periapsis. 



For the remainder of this course, we will consider the second object being a sat. 


NOTE: Here it might be a good idea to descrbing the elements more and create some sort of animation

#### Elements defining the shape and size of the orbit
##### Semi-Major Axis
##### Eccentricity

Describe elements and and figures/animations

#### Elements defing the orientation of the orbital plane in which the plane is embedded
##### Incliniation
##### Longitude of Ascending Node

Describe elements and and figures/animations

#### Elements defining orientaion of periasis
##### Argument of Periapsis
##### Time of Periapsis Passage

Describe elements and and figures/animations

## Integrals of Motion 
 
NOTE: This could be it's own page

Integrals of Motion are used to derive properities of Two-Body Motion without having to solve the equations of motion. They are constant along the trajectory of motion.

#### Conservation of Angular Momentum

h, i, Omega

The specific angular momentum vector $\mathbf{h}$ is defined as:

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

where
$\mathbf{r}$ is the position vector,
$\mathbf{v}$ is the velocity vecot and both are 3x1 Vectors 

To show that the angular momentum vector is an integral of motion, take the total time derivative of $\mathbf{h}$:

:::{math}
:label: eq:angular_momentum
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


##### Angular Momemtum

The first Integral of Motion to determine is Angular Momentum 

:::{math}
\mathbf{h} = \mathbf{r} \times \mathbf{v}
:::

##### Inclination

Next we define the Inclination of the orbit to be the angle measuring the tilt of the orbit around it's "celetisal" body. For our diagram this is it is from the reference vector $\mathbf{\hat{z}}$ and unit Specific Angular Momentum vector $\hat{h}$

In Astrodynamics the Inclination is restricted between 0$^\circ$ and 180$^\circ$. 

:::{math}
:label: eq:inclination
i = \cos^{-1}\left(\frac{\mathbf{\hat{z}}}{\mathbf{\hat{h}}}\right)
:::

From Wiki: (re write and reference future docs)

An inclination of 0° means the orbiting body has a prograde orbit in the planet's equatorial plane.
- An inclination greater than 0° and less than 90° also describes a prograde orbit.
- An inclination of 63.4° is often called a critical inclination, when describing artificial - satellites orbiting the Earth, because they have zero apogee drift.[3]
- An inclination of exactly 90° is a polar orbit, in which the spacecraft passes over the poles of the planet.
- An inclination greater than 90° and less than 180° is a retrograde orbit.
- An inclination of exactly 180° is a retrograde equatorial orbit.

**There are convetions for common inclinations angles:**

Might want to include figures/animations here depending on how are they are

$0^{\circ} \le i \le 90^{\circ}$
: "Orbiting body" has a prograde orbit

$i = 0$
: "Orbiting body" has a prograde orbit within the "reference plane"

$i = 63.4^\circ$
: Is often called a critical inclination, when describing artificial - satellites orbiting the Earth, because they have zero apogee drift. [3] WIKI Refe

$i = 90.0^\circ$
: Is a polar orbit, in which the "spacecraft" passes over the poles of the planet

$ 90.0^\circ \le i \le 180.0^\circ$
: Is retrograde orbit


:::{math}
:label: eq:raan_cases
\mathbf{i} = \begin{cases}
0^{\circ} \lt \mathbf{i} \lt 90^{\circ} & \text{"Orbiting body" has a prograde orbit} \\
\mathbf{i} = 0.0^{\circ} & \text{"Orbiting body" has a prograde orbit within the "reference plane"} \\
\mathbf{i} = 63.4^{\circ} & \text{Often called a critical inclination, when describing artificial - satellites orbiting the Earth, because they have zero apogee drift WIKI Refe} \\
\mathbf{i} = 90.0^{\circ} & \text{A polar orbit, in which the "spacecraft" passes over the poles of the planet} \\
90.0^{\circ} \lt \mathbf{i} \le 180.0^{\circ} & \text{"Orbiting body" has a retrograde orbit} \\
\end{cases}
:::


##### Longitude of Ascending Node

The Longitude of Ascending Node is the angle between $\mathbf{\hat{x}}$ and Node Vector $\mathbf{\hat{n}}$. It is also known as the Right Ascension of the Ascending Node (RAAN). The Ascending Node is the intesection of the orbit and the reference plane. Thus the Right Ascension of the Ascending Node is the angle at which the "sat" "orbit" ascends through and above the "plane of reference". 

Maybe have figure/animation here

:::{math}
:label: eq:orbital-elements-Omega
\mathbf{\Omega} = \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right)
:::

In Astrodynamics the Longitude of Ascending Node is define to be betwewn 0$^{\circ}$ and 360$^{\circ}$. To solve for the Longitude of Ascending Node we must perform a quadrant check due to its trigometric definition. By looking at the y component of the Node Vector ($\mathbf{\hat{n}_y}$).

TODO: See how codes work either use x or nx, y or ny

If $\mathbf{\hat{n}_y} \geq 0^{\circ}$ then $\mathbf{\Omega}$ lies between I and II quadrants, otherwise if $\mathbf{\hat{n}_y} \leq 0^{\circ}$ then $\mathbf{\Omega}$ lies between III and IV quadrants,

:::{math}
:label: eq:raan_cases
\mathbf{\Omega} = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{\hat{x}}}{\mathbf{\hat{n}}}\right) & \mathbf{\hat{n}_y} < 0^{\circ}
\end{cases}
:::



#### Conservation of Energy 
E

#### Eccentricity Vector
omega

#### Kepler's Law
to

Write about where they come from and describe the 6 that come out
Talk about how we go from state vector to itegrals of motion

