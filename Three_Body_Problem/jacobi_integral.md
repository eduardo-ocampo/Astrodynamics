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

## The Jacobi Constant

When dealing with the [Circular Restricted Three-Body Problem](cr3bp.md) there exists a time-invariant integral of motion known as the Jacobian Integral of Motion. To get this integral of motion, multiple the Circular Restricted Three-Body Problem equations of motion, Equation {eq}`cr3bp_eom_simp`, by the velocity vector:

:::{math}
:label: 
\begin{align*}
\dot{x}\left(\ddot{x} - 2n\dot{y}\right) &= \dot{x}\left(\frac{\partial{V}}{\partial{x}}\right) \\ 
\dot{y}\left(\ddot{y} + 2n\dot{x}\right) &= \dot{y}\left(\frac{\partial{V}}{\partial{y}}\right) \\
\dot{z}\left(\ddot{z} \right) &= \dot{z}\left(\frac{\partial{V}}{\partial{z}}\right)
\end{align*}
:::

:::{math}

\dot{x}\ddot{x} + \dot{y}\ddot{y} + \dot{z}\ddot{z} = \frac{\partial{V}}{\partial{x}}\dot{x} + \frac{\partial{V}}{\partial{y}}\dot{y} + \frac{\partial{V}}{\partial{z}}\dot{z}

:::

and then integrate both ends

:::{math}
:label: 

\frac{1}{2} \frac{d}{dt} \left[ \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right] = \frac{d}{dt} V\left(x,y,z \right)

:::

:::{math}
:label: 

\frac{d}{dt} \left[ \frac{1}{2}\left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) - V \right] = 0
:::

This yields the constant **Jacobi Integral (J)**: 

:::{math}
:label: jacobi_constant

\frac{1}{2}\left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) - V\left(x,y,z \right) = J 
:::


## Non-Dimensional Jacobi Constant

There exists a Non-Dimensional Jacobi Constant that follows the same formation as the [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem).

Consider the **Jacobian Integral** {eq}`jacobi_constant` with applied normalized potentials $\tilde{V}$ {eq}`cr3bp_V_norm`, and $\tilde{U}$ {eq}`cr3bp_U_norm`. This results in:


:::{math}
:label: jacobi_constant_norm
\frac{1}{2}\left( {\dot{x}^*}^2 + {\dot{y}^*}^2 + {\dot{z}^*}^2 \right) - \tilde{V}\left(x^*,y^*,z^*\right) = \tilde{J} 
:::

which is still a constant.

### Zero-Velocity Curves

For a simplified solar system, the motion of the planets are more or less in the x-y plane. Often times it is not a bad approximation to state that $z$ and $\dot{z}$ are to be zero ([small inclination](https://ssd.jpl.nasa.gov/planets/approx_pos.html)). 

:::{math}

\frac{d\mathbf{\tilde{V}}}{dt}\bigg|_{z^* = 0} = 0
:::

In other words, we can decouple the in-plane motion and out-of-plane motion. This system is named the **Circular Planar Restricted Three-Body Problem** (CPR3BP). In this case Expression {eq}`jacobi_constant_norm` becomes:

:::{math} 
:label: crp3bp_jacobi
\left( {\dot{x}^*}^2 + {\dot{y}^*}^2\right) - 2\tilde{V}\left(x^*,y^*\right) = 2\tilde{J} = -C
:::

A new constant ( $C$ ) is used to denote the **Circular Planar Restricted Three-Body Problem Jacobi Constant**. 

The form of the Jacobi Constant is similar to that of total energy such that it has a pseudo-potential term and a kinetic energy like term. Knowing the Jacobi is constant gives insight on a spacecraft's motion in the Three-Body System and its bounds in space. 

Looking at the velocity term in Equation {eq}`crp3bp_jacobi` it is certain to always be positive. Rearranging Expression {eq}`crp3bp_jacobi` shows that $2\tilde{V} - C \ge 0$. 

Knowing $\tilde{V}$ is always positive, if $C \lt 0$ then $2\tilde{V} - C \ge 0$ is always satisfied. However, if $C \gt 0$ things get a bit interesting. What this says is that given a value of Jacobi Constant, motion is not possible in the region of space when:

:::{math}
:label: 
2\tilde{V} - C \le 0
:::

In Astrodynamics this is sometimes referred to as the curve in space where the velocity would go to zero. Sometimes called Zero-Velocity Curves or Forbidden Regions. For the CRP3BP the Zero-Velocity Surface is defined as:

:::{math}
:label: solve_zvc
2\tilde{V}\left( x^*, y^*\right) - C = 0
:::

The next section will dive into generating Forbidden Regions of space using Python.

## Python Example

Consider the **Earth-Moon System**. The [Planetary Satellite Mean Elements](https://ssd.jpl.nasa.gov/sats/elem/) are pulled from Solar System Dynamics database courtesy of NASA JPL. 

| Planet      | Satellite  | Code  | Ephemeris   | a (km) | e      | ω (deg) | M (deg) | i (deg) | node (deg) | P (days) |
| :---:       | :----:     | :---- | :---------- | :----  | :----- | :------ | :-----  | :----   | :--------  | :------- |
| **Earth**   | **Moon**   | 301   | DE405/LE405 | 384400 | 0.0554 | 318.15  | 135.27  | 5.16    | 125.08     | 27.322   |

Knowing the Moon's inclination is 5.16$^\circ$ the Circular Restricted Planar assumption is valid for this analysis.

The following constants were generated for the Earth-Moon system using NASA JPL's Solar System Dynamics [Astrodynamic Parameters](https://ssd.jpl.nasa.gov/astro_par.html) database ($\frac{km^3}{s^2}$):

:::{math}
\begin{align*}
GM_{Earth} &= 398600.435507 \\
GM_{Moon}  &= 4902.800118 \\
\end{align*}
:::

Yielding a mass ratio of:

:::{math}
\mu = 0.012150584394709708
:::

For this example, plot the forbidden regions for the CRP3BP at Jacobi Constants ranging from **3.5 to 3.0**. Here the Lagrange Points are plotted for reference as they are relevant to the forbidden regions. More information about the [Lagrange Points](lagrange.md) can be found here (TODO: POINT TO PLOTS).

Begin by importing module [forbidden_region](https://github.com/thatguyeddieo/Astrodynamics/blob/main/Three_Body_Problem/forbidden_region.py) and defining the Earth-Moon mass ratio $\mu$.

```python
from forbidden_region import forbidden_region

# Earth-Moon System Parameters
# ----------------------------------------------------------
mu = 0.012150584394709708
```

Function `forbidden_region()` has x-y coordinate ranges set by default but in some cases they may be set by the user. Argument **linspace_num** is used to set the density of the meshed grid used for building the forbidden region. This example sets a coarse `np.linspace` spacing for easier to load interactive figures included in this section.

```python
# Calc Forbidden Region
# ----------------------------------------------------------
# meshgrid spacing
lin_num = 150

# Jacobi Constant
C = 3.5

# Get Forbidden Region
x1, y1, forb_region1 = forbidden_region(C,mu,linspace_num=lin_num)
x2, y2, forb_region2 = forbidden_region(C,mu,linspace_num=lin_num,
                                        x_range=[ 0.70,1.20],
                                        y_range=[-0.25,0.25])
```

Using this method, interactive **Figure 1.1** was created to draw forbidden region contours for 8 Jacobi Constant ($C$) values for the Earth-Moon system. Move the slider at the bottom of **Figure 1.1** to view the different contour plots. 


```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import plot_mult_forbbiden_regions 
fig1 = plot_mult_forbbiden_regions.plot()
glue("fig1",fig1)
```

```{glue:figure} fig1
:align: center
:name: forbidden_region_interactive
**Figure 1.1.** Interactive Forbbiden Region Contour Plots
```

**Figure 1.1** is initialized with slider set to $C = 3.5$ for reference. As the Jacobi Constant for the Earth-Moon System decreases towards 3.0 notice how the forbidden region gets smaller in size. 

For $C = 3.18827$ the forbidden region around the Moon comes to a singularity at Lagrange Point 1. As shown with more detail in **Figure 1.2** below.

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import plot_forbidden_region
fig2 = plot_forbidden_region.plot()
glue("fig2",fig2)
```

```{glue:figure} fig2
:align: center
:name: L1_forbbiden_region
**Figure 1.2.** Singularity of the Jacobi Constant at L1 
```

Now for $C \lt 3.18827$ a direct path from the Earth to the Moon begins to appear (Low Energy Transfer). At a high level, Mission Design Engineers aim to change a spacecraft's velocity just enough so that a trajectory exists between two primary bodies using very small energy. For example, here are some more references for how this is used on the Earth-Moon system for [Low Energy Transfer](http://www.gg.caltech.edu/~mwl/publications/papers/lowEnergy.pdf) and [Free-Return Trajectory](https://en.wikipedia.org/wiki/Free-return_trajectory) as means of sending spacecraft to the Moon. 

Using the function `get_jacobi_velocity` provided in module [forbidden_region](https://github.com/thatguyeddieo/Astrodynamics/blob/main/Three_Body_Problem/forbidden_region.py) one can get the required maximum velocity for a given Jacobi Constant. Let's use this function to determine the velocity required to transfer from an Earth parking orbit to the Moon's region in space at initial position and a fixed velocity angle $\theta_0$:

:::{math}
:label: jc_traj_initial_theta
\theta_0 = 31^\circ
:::

:::{math}
:label: jc_traj_initial_position
\mathbf{r_0}^* = 
\begin{bmatrix}
0.00 \\
-0.50  \\
0.00
\end{bmatrix}
:::

Import function `get_jacobi_velocity` and set the initial state vector for this example. 

```python
from forbidden_region import get_jacobi_velocity
```

```python
# Initial State Vectors
# --------------------------------------------------------------------------------
initial_angle = np.radians(31)
x_initial, y_initial =  0.00, -0.5
vel_initial = get_jacobi_velocity(x_initial,y_initial,C,mu)

initial_pos = [x_initial, y_initial, 0.0]
initial_vel = [ np.cos(initial_angle)*vel_initial, 
                -np.sin(initial_angle)*vel_initial, 0.0]
```

Use the same methods from [Python Example](cr3bp.md#python-example) for generating a trajectory in the [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem) to show the interaction between a spacecraft's change in energy and the Jacobi Constant:

```{figure} ./images/moon_region_trajectory.gif
:name: fig:moon_region_trajectory
:width: 100%
**Figure 1.3** Animation of Trajectory Towards the Moon  
```

The animation shows the Jacobi Constant starting at a value of 3.190 and ending with a constant of 3.176. For a fixed spacecraft position {eq}`jc_traj_initial_position` and impulse angle {eq}`jc_traj_initial_theta` as $C$ decreases the magnitude of $\Delta V$ required to maintain the Zero-Velocity Surface {eq}`solve_zvc` increases from 1.015956 to 1.022823. If the mission requirements is to design a trajectory towards the Moon region of space, than we can analyze the minimum $\Delta V$ required until the L1 region opens up but notice how the orbit shape around the Moon also changes with increased velocity. At some point the increase to the initial velocity sets the spacecraft up to return towards L1 and given a $TOF\gt 2.2\pi$ the spacecraft can return towards the primary body. 

As Jacobi Constant $C$ continues to decrease in **Figure 1.2** the region in space between both Lagrange Point 2 and Lagrange Point 3 begin to open. This is shown in **Figure 1.2** by toggling slider between $C = 3.180$ and $C = 3.013$. As $C$ gets closer to 3.0 the forbidden regions disappear to a singularity corresponding to the location of Lagrange Point 4 (L4) and Lagrange Point 5 (L5). For the Earth-Moon System the minimum Jacobi Constant is approximately **2.988043**. This can be shown by hovering your cursor around L4 and L5 on interactive **Figure 1.2**

Lastly, the same analysis can be done to demonstrate how the forbidden regions change in 3-dimenionsal space along the Potential Surfaces {eq}`cr3bp_V_norm` introduced in section [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem)


```{figure} ./images/zvc_cross_section.gif
:name: fig:zvc_cross_section
:width: 100%
**Figure 1.4** Animation of Zero-Velocity Curves for the Earth-Moon System 
```

TODO: Next section can be Jacobian Integral in inertial frame and then lead to Tisserand's Criterion

#### Acknowledgements

Special thanks to Ari Rubinsztejn of [gereshes.com](https://gereshes.com/) for their publication on the Three-Body Problem. Their work played a key role in helping verify & validate the Python routines I created for this section. I encourage the reader to visit Rubinsztejn's work on the Jacobi Integral and how it varies with $\mu$, or at the very least appreciate the informative plots they created by visiting their site [Jacobi and His Constant – The 3-Body Problem](https://gereshes.com/2018/11/26/jacobi-and-his-constant-the-3-body-problem).