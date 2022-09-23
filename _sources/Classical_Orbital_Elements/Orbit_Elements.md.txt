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


```{note}
The term $G(m_1+m_2)$ comes up quite often in our Equations of Motion that is convient to define it as teh Gravitation Constant ($\mu$)

:::{math}
\mu = G(m_1+m_2)
:::
```

## Classical Orbital Elements

:$a$: Semi-Major Axis
:$e$: Eccentricity
:$i$: Incliniation
:$\Omega$: Longitude of Ascending Node
:$\omega$: Argument of Periapsis
:$t_0$: Time of Periapsis Passage

They can be broken down even further as to how they define the shape, and size of the orbit, orientation of orbital plane, and definition of periapsis. 



For the remainder of this course, we will consider the second object being a sat. 


NOTE: Here it might be a good idea to descrbing the elements more and create some sort of animation

### Elements Defining The Shape and Size of The Orbit

<!-- ```{image} ./images/elliptic_orbit_image.jpeg
:alt: Elliptic Orbit Definition
``` -->

```{figure} ./images/elliptic_orbit_image.jpeg
:name: fig:elliptical-orbit-definitions
:width: 75%

The geometry and definition of distances in an elliptical orbit.
```

TODO: Find a method for labeling and numbering figures

[source](https://space.stackexchange.com/questions/28361/spiraling-out-from-circular-orbit-to-escape-via-low-thrust-what-is-%CE%B3-gamma#:~:text=by%20uhoh%27s%20comment-,Source,-It%20is%20just)

#### Semi-Major Axis ($a$)


Figure XXX (show above), shows a satelitte orbiting a central body in an elliptical path. The focus (F) plays a role in defining the satellite's trajectory in space and its angle from Periapsis (Perigee). The Semi-Major axis of the Ellipse is defined as the length from the Geometric Center of the Ellipse to Periapsis. 

Taking a fixed focus (Central Body) Figure XXX below shows how varying Semi-Major Axes changes the shape and size of a given elliptical orbit as well as its geometric center. 

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_semimajor
fig1 = elliptic_orbit_semimajor.plot()
glue("semimajor_axis_fig",fig1)
```

```{glue:figure} semimajor_axis_fig
:align: center
**Figure XXX.** Varying Semi-Major Axis
```


#### Eccentricity ($e$)

The eccentricity is defined as the ratio of the distance from the Geometric Center to the Focus Point (linear eccentricity) compared to the Semi-Major Axis 

:::{math}
:label:
e = \frac{ae}{e} = \frac{c}{e}
:::

Figure XXX below shows how varying Eccentricy changes the shape and size for Elliptical Orbit. (Talk about when 1.0>e or 1.0). Note that when eccentricy is zero the orbit is circular.

```{code-cell} ipython3
:tags: ["remove-input"]
import elliptic_orbit_eccentricity
fig2 = elliptic_orbit_eccentricity.plot()
glue("eccentricity_fig",fig2)
```

```{glue:figure} eccentricity_fig
:align: center
**Figure XXX.** Varying Eccentricity
```

### Elements defing the orientation of the orbital plane in which the plane is embedded

#### Incliniation

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_inclination
fig3 = elliptic_orbit_inclination.plot()
glue("inclination_fig",fig3)
```

```{glue:figure} inclination_fig
:align: center
**Figure XXX.** Inclination Change
```

#### Longitude of The Ascending Node

Earth related LAN, aka as  right ascension of the ascending node RAAN
Describe elements and and figures/animations

TODO: Add note about x-y being body reference axes

TODO: Talk about this somewhere in docs
arc_x = np.cos(np.radians(lan)-np.pi/2)*np.sin(np.linspace(0,np.radians(inclination_angle),100))
arc_y = np.sin(np.radians(lan)-np.pi/2)*np.sin(np.linspace(0,np.radians(inclination_angle),100))
arc_z = np.cos(np.linspace(0,np.radians(inclination_angle),100))
arc = np.vstack((arc_x,arc_y,arc_z)).T

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_long_acsend_node
fig4 = elliptic_orbit_long_acsend_node.plot()
glue("lan_fig",fig4)
```

```{glue:figure} lan_fig
:align: center
**Figure XXX.** Longitude of The Ascending Node Change
```

### Elements defining orientaion of periasis

#### Argument of Periapsis

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_argument_of_periapsis
fig5 = elliptic_orbit_argument_of_periapsis.plot()
glue("arg_peri_fig",fig5)
```

```{glue:figure} arg_peri_fig
:align: center
**Figure XXX.** Argument of Periapsis Change
```

#### Time of Periapsis Passage

Describe elements and and figures/animations
