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
.. _
# Integrals of Motion 

TOOD: review when variable are and should be capatilized

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

This Integral of Motion is also known as the Right Ascension of the Ascending Node (RAAN). The Ascending Node is the intesection of the orbit and the reference plane as shown in [Figure 3.2](iom_Figure_2). Thus the Right Ascension of the Ascending Node is the angle at which the spacecraft ascends through and above the "plane of reference". 

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



## Conservation of Energy (ε)

The specific energy ($\varepsilon$) of the Two-Body system is defined as:

:::{math}
:label: energy 
\varepsilon = \frac{v^2}{2} - \frac{\mu}{r}
:::

### 4. Specific Energy

To show that the energy is an integral of motion, start by taking a dot product of our Equations of Motion for the Two-Body Problem with respect to velocity.

:::{math}
:label:
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

This form of the specific energy is know as the vis-viva equation in Astrodynamics. Specific energy does not change as a function of time, thus it is considered an Integral of Motion. Note the scalar values and that $\mu$ is the gravitational constant for the Two-Body Problem.

**Properites of Specific Energy:**

:::{math}
:label: eq:raan_cases
\varepsilon = \begin{cases}
\varepsilon \lt 0.0 & \text{Orbit is bound: Elliptical Orbit}\\
\varepsilon = 0.0   & \text{Orbit is escaped: Parabolic Orbit} \\
\varepsilon \gt 0.0 & \text{Orbit is escaped: Hyperbolic Orbit}
\end{cases}
:::

For a bound orbit

:::{math}
r \lt -\frac{\mu}{\varepsilon}
:::

For an escaped orbit

:::{math}
r \rightarrow \infty
:::

:::{math}
\frac{v^2}{2} = \varepsilon
:::

## Eccentricity Vector (e)

The Eccentricity Vector ($\mathbf{e}$) is defined as:

:::{math}
:label: eccentricity_vector
\mathbf{e} = \frac{1}{\mu}\left(\mathbf{v}\times\mathbf{h}\right) - \frac{\mathbf{r}}{r}
:::

To show that the Eccentricity Vector is an integral of motion, take a cross-product of our Equations of Motion for the Two-Body Problem with respect to Angular Momemtum ($\mathbf{h}$)

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
:label: proof_eccent
\mathbf{v}\times\mathbf{h} = \mu\frac{\mathbf{r}}{r} + \mathbf{C}
:::

Where $\mathbf{C}$ is a constant vector. The constant vector has the same dimensions as $\mu$, thus we can transform it into a dimensionless number by dividing Equation {eq}`proof_eccent` by $\mu$ and defining the Eccentricity Vector as 

:::{math}
:label:
\mathbf{e} = \frac{\mathbf{c}}{\mu}
:::

Finally, we can rewrite our Eccentcity Vector as:

:::{math}
\mathbf{e} = \frac{1}{\mu}\left(\mathbf{v}\times\mathbf{h}\right) - \frac{\mathbf{r}}{r}
:::


Some Notes:

By inspection it is known that constant vector $\mathbf{c}$ lies in the orbital plane. Therefore, the Eccentricity Vector also lies in the orbital plane. Althought $\mathbf{e}$ is a 3x1 vector its magnitude is define by components of Node Vector ($\mathbf{\hat{n}_\Omega}$,  $\mathbf{\hat{n}_T}$) which are already account for in defining the third Integral of Motion: [Longitdue of Ascending Node](#3-longitude-of-ascending-node). The only extra integral of motion comes from the orientation of $\mathbf{e}$ within the orbital plane. This angle is know as the Argument of Periapsis ($\omega$). 

### 5. The Argument of Periapsis ($\omega$)

TODO: Insert a figure here showing eccent vector and $\omega$

As shown in figure XXX, The Argument of Periapsis is defined as the angled between the Node Vector ($\mathbf{n}$) and Eccentcity Vector ($\mathbf{e}$). It has a range of $0^\circ \lt \omega \lt 360^\circ$ and points towards periapsis. To solve for the angle a quadrant check is required by looking at z-component of the Eccentrcity Vector.

:::{math}
:label: raan_cases
\mathbf{\omega} = \begin{cases}
\cos^{-1}\left(\frac{\mathbf{n}\cdot\mathbf{e}}{|\mathbf{n}||\mathbf{e}|}\right) & e_z \geq 0^{\circ} \\
360^{\circ} - \cos^{-1}\left(\frac{\mathbf{n}\cdot\mathbf{e}}{|\mathbf{n}||\mathbf{e}|}\right) & e_z < 0^{\circ}
\end{cases}
:::

# Kepler's Law

The last Integral of Motion comes from Kepler's Law:

:::{math}
:label:
\frac{d}{dt}\left(A\right) = \frac{h}{2}
:::

to

Write about where they come from and describe the 6 that come out
Talk about how we go from state vector to itegrals of motion

