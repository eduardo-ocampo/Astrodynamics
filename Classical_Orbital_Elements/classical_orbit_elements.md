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


# Classical Orbit Elements

The Classical Orbit Elements can be categorized as to how they define the shape and size of an orbit, orientation of the orbital plane, and definition of periapsis. From the definition of the [Two-Body Problem](Two_Body_Problem.md) we know the relative motion of a secondary body to a primary body can be described with a given position and velocity. However, these vectors are constantly changing with time. 

In this section let us consider the Two-Body system of a satellite orbiting Earth. The following 6 Orbital Elements describe the satellite's relative orbit around Earth. 

1. Semi-Major Axis ($a$)
2. Eccentricity ($e$)
3. Inclination  ($i$)
4. Longitude of Ascending Node ($\Omega$)
5. Argument of Periapsis ($\omega$)
6. Time of Periapsis Passage ($t_0$)

## Elements Defining The Shape and Size of The Orbit

```{figure} ./images/elliptic_orbit_image.jpeg
:align: center
:name: coe_Figure_1
**Figure 2.1** Geometric Definition of an Elliptical Orbit.
```

[source](https://space.stackexchange.com/questions/28361/spiraling-out-from-circular-orbit-to-escape-via-low-thrust-what-is-%CE%B3-gamma#:~:text=by%20uhoh%27s%20comment-,Source,-It%20is%20just)

### Semi-Major Axis ($a$)

[Figure 2.1](coe_Figure_1), shows a satellite orbiting a central body in an elliptical path. The focus (F) plays a role in defining the satellite's trajectory in space and its angle from Periapsis (Perigee). The Semi-Major axis of the Ellipse is defined as the length from the Geometric Center of the Ellipse to Periapsis. 

Taking a fixed focus (Central Body) [Figure 2.2](coe_Figure_2) below shows how varying Semi-Major Axes changes the shape and size of a given elliptical orbit as well as its geometric center. 

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_semimajor
fig1 = elliptic_orbit_semimajor.plot()
glue("semimajor_axis_fig",fig1)
```

```{glue:figure} semimajor_axis_fig
:align: center
:name: coe_Figure_2
**Figure 2.2** Orbits with Varying Semi-Major Axis
```


### Eccentricity ($e$)

The eccentricity is defined as the ratio of the distance from the Geometric Center to the Focus Point (linear eccentricity) compared to the Semi-Major Axis 

:::{math}
:label:
e = \frac{ae}{e} = \frac{c}{e}
:::

Interactive [Figure 2.3](coe_Figure_3) shows how varying Eccentricity changes the shape and size for Elliptical Orbit. Note that when eccentricity is zero the orbit is circular.

TODO: Talk or point to section when about when 1.0>e or 1.0

```{code-cell} ipython3
:tags: ["remove-input"]
import elliptic_orbit_eccentricity
fig2 = elliptic_orbit_eccentricity.plot()
glue("eccentricity_fig",fig2)
```

```{glue:figure} eccentricity_fig
:align: center
:name: coe_Figure_3
**Figure 2.3** Orbits with Varying Eccentricity
```

## Elements Defining the Orientation of the Orbital Plane in which the Plane is Embedded

### Inclination

TODO: Write a desciption

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_inclination
fig3 = elliptic_orbit_inclination.plot()
glue("inclination_fig",fig3)
```

```{glue:figure} inclination_fig
:align: center
**Figure 2.4.** Inclination Change
```

### Longitude of The Ascending Node

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
**Figure 2.5.** Longitude of The Ascending Node Change
```

## Elements Defining Orientaion of Periasis

### Argument of Periapsis

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import elliptic_orbit_argument_of_periapsis
fig5 = elliptic_orbit_argument_of_periapsis.plot()
glue("arg_peri_fig",fig5)
```

```{glue:figure} arg_peri_fig
:align: center
**Figure 2.6.** Argument of Periapsis Change
```

### Time of Periapsis Passage

Describe elements and figures/animations
