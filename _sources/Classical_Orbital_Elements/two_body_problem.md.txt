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

# The Two-Body Problem

## Introduction

The full Two-Body problem is the motion two bodies with finite masses that are attracted to each other according to Newton's Law of Gravitation. 

We are interested in their relative dynamics. The force of particle $P_1$ acting on particle $P_2$ in the inertial frame yields the following diagram: 

```{figure} ./images/two-body_image.png
:name: TwoBody_Problem_Figure
:width: 75%
**Figure 1.1** Two-Body Problem in an Inertial Reference Frame
```


Where $P_1$ has mass $m_1$ and $P_2$ has mass $m_2$, and we define the relative vector notation as:

:::{math}
\begin{align*}
\mathbf{r}_{ij} &= \mathbf{r}_j - \mathbf{r}_i \\
\mathbf{r}_{12} &= \mathbf{r}_2 - \mathbf{r}_1
\end{align*}
:::

Derived from Newton's Law of Gravitation, the **Equation of Motion** for the Two-Body Problem is defined by Second-Order Ordinary Differential Equations:

:::{math}
:label: Two_Body_EOM
\ddot{\mathbf{r}} = -G\frac{(m_1+m_2)}{r^3}\mathbf{r}
:::

where:

:::{math}
\mathbf{r} = \mathbf{r_{12}} = \mathbf{r_2} - \mathbf{r_1}
:::

```{note}
The term $G(m_1+m_2)$ comes up quite often in our Equations of Motion that is convenient to define it as the Gravitation Constant ($\mu$)

:::{math}
:label: gravitation_constant_mu
\mu = G(m_1+m_2)
:::
```

## The Relative State Vector

Each particle has a State Vector made up of its position and velocity:

:::{math}
:label: eq:state_vector
\mathbf{\bar{x}} = \begin{bmatrix} 
    x_0       \\ y_0       \\ z_0 \\
    \dot{x_0} \\ \dot{y_0} \\ \dot{z_0}
\end{bmatrix}
:::

To solve the for the Two-Body Problem we require 12 equations of motion due to 2 state vectors. However, if we assume one of the particles does not have mass or its mass is negligible (Earth-satellite system) the system will require only 6 equations of motion. Thus 6 integrals of motion are needed to solve the **relative dynamics of the Two-Body Problem.**  The 6 integrals of motion have become to be known as the [Classical Orbital Elements](Classical_Orbit_Elements.md). An integral of motion is a combination of positions, velocities, and times that remain constant under the motion governed by the equations of motion.


For Two-Body systems were $m_2 \ll m_1$ the Expression {eq}`gravitation_constant_mu` for Gravitation Constant simplifies to:

:::{math}
:label:
\mu = G(m_1)
:::

NASA JPL's Solar System Dynamics Group maintains and publishes accurate [Astrodynamic Parameters](https://ssd.jpl.nasa.gov/astro_par.html) for planetary bodies. Below are just a few common Gravitation Constants for planets in our Solar System. Visit [Astrodynamic Parameters](https://ssd.jpl.nasa.gov/astro_par.html) to find more information: 


| Body        | GM ($km^3s^{-2}$)   |
| :--------:  | :-----------------: |
| **Sun**     | 1.32712440041279e11 |
| **Earth**   | 398600.435507       |
| **Mars**    | 42828.375816        |
| **Saturn**  | 137940584.841800    |

## Solving The Two-Body Problem

Assume we are given the following information about a spacecraft's position and velocity at some initial time ($t_0$) while orbiting Earth. In the relative coordinate frame the position and velocity vectors are:

**Boundary Conditions** 

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
:label: twoBody_example_ivp
\mathbf{v}(t_0) = 
\begin{bmatrix}
1 \\
10 \\
5
\end{bmatrix} \frac{km}{sec}
::: 

For the Earth centered system the Gravitation Constant to use is:

:::{math}
\mu = 398,600 \frac{km^3}{sec^2}
:::

**Differential Equations**

Using the Equations of Motions for the Two-Body problem {eq}`Two_Body_EOM`, expand the Second-Order Ordinary Differential Equations to be solved Numerically. 

:::{math}
:label: twoBody_example_diff_eqs
\begin{align*}
\ddot{x} &= -\mu \frac{x}{r^3} \\
\ddot{y} &= -\mu \frac{y}{r^3} \\
\ddot{z} &= -\mu \frac{z}{r^3} 
\end{align*}
:::

**Numerical Setup**

Begin by importing module [twoBody_problem](https://github.com/thatguyeddieo/Astrodynamics/blob/main/Classical_Orbital_Elements/twoBody_problem.py) and defining the initial state vector {eq}`twoBody_example_ivp` 

```python
import numpy as np
import twoBody_problem

# Initial State Vectors
# ------------------------------------------------------
position = [5000, 100, 0] # km
velocity = [1, 10, 5] # km/s
```

Instantiate Python class `twoBody_problem.twoBody()` with the initial state vector and set the Gravitation Constant for this analysis:

```python
# Instantiate Object: For this example consider a 
# spacecraft orbiting Earth
# ------------------------------------------------------
# Earth Gravitation Constant
mu = 398600 # km^3/sec^2

satellite = twoBody_problem.twoBody(position,velocity)
satellite.mu = mu
```

To solve for the satellite's trajectory, we must first define a time of flight. For now let us integrate our differential equations up to 20 orbital periods. Get the satellite’s orbital period by computing state elements more on how to do this at LINK.  

```python
# Get Initial State Elements
# ------------------------------------------------------
satellite.get_state_elements()
# Determine orbital period
period = satellite.orbit_elements["Period"]["value"] # Hours
satellite.period = period
print("Period: ",period, " hours")
```

```
Period:  3.602745730309696  hours
```

The satellite’s orbital period is 3.603 hours. Set a time range up to 20 orbital periods broken up into evenly spaced 15-minute intervals.


```python
# Numerical Analysis Setup
# ------------------------------------------------------
# Set upper time bond of 20 orbital periods
time_ub = 20*period*3600 # convert hrs to seconds 
# Take 15 minute steps
time_step= 15*60 # convert mins to seconds 
satellite.time = np.arange(0, time_ub, time_step)
```

The solver relies on running [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) for solving the initial value problem for the system of differential equations {eq}`twoBody_example_diff_eqs`. Class `twoBody` has built-in relative and absolute tolerances, but they are initialized here as an example for the reader:

```python 
# Run Numerical Analysis: scipy.integrate methods
# --------------------------------------------------------------------------------
# Set up tolerances, relative & absolute
satellite.relTol = 1e-10
satellite.absTol = 1e-12

# Run scipy analysis 
# --------------------------------------
satellite.solve_twoBody_trajectory()
```



```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import dev_plot_twoBody_trajectory_animation 
twoBody_animation = dev_plot_twoBody_trajectory_animation.plot()
```

To illustrate the numerical results, the satellite's trajectory is projected on the x-y & x-z plane as shown in [Figure 1.2](twoBody_plotOrbitTrajectory)



```{figure} ./images/twoBody_plotOrbitTrajectory.png
:align: center
:name: twoBody_plotOrbitTrajectory
:width: 100%
**Figure 1.2** Satellite Trajectory Projected on 2D Planes
```

It is good practice to spot check the results by checking if [Specific Energy](integrals_of_motion.md#conservation-of-energy) ($\varepsilon$) and [Specific Angular Momentum](integrals_of_motion.md#conservation-of-angular-momentum) ($h$) are conserved. [Figure 1.3](twoBody_plotEnergyAngMoment) plots both $\varepsilon$ & $h$ as a function of time. As we expect the characteristic parameters are conserved. The slight increase over time is due to computation limitation but take note of the y-axis range. 


```{figure} ./images/twoBody_plotEnergyAngMoment.png
:align: center
:name: twoBody_plotEnergyAngMoment
:width: 100%
**Figure 1.3** History of Oribtal Parameters
```

Lastly, a 3-dimensional plot of the satellite’s trajectory is shown below in interactive [Figure 1.4](plot_twoBody_trajectory_animation). Play the animation by pressing the blue button and rotate the figure using your mouse. The duration (Time of Flight) of the animation is equivalate to 1 orbital period. Notice how the satellite’s relative speed compares at periapsis and apoapsis TODO LINK SECTION THAT DESCRIBES THIS. At periapsis, the satellite’s altitude is 4,926.081 $km$ and its relative speed is 2.94710 $\frac{km}{s}$ while at apoapsis the altitude is 18,938.773 $km$ and at a speed of 1.33245 $\frac{km}{s}$. More on how this is calculated in SECTION TODO LINK.

```{code-cell} ipython3
:tags: ["remove-input"]
glue("twoBody_animation",twoBody_animation)
```

```{glue:figure} twoBody_animation
:align: center
:name: plot_twoBody_trajectory_animation
**Figure 1.4.** Interactive Animation of the Satellite's Trajectory Relative to Earth 
```
