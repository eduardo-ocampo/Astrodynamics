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

## Circular Restricted Three-Body Problem 

By letting $m_3 \rightarrow 0$ then Equation {eq}`3bp_eom_1`-{eq}`3bp_eom_2` as derived from the [Jacobian Coordinate Frame](introduction.md/#jacobian-coordinate-frame) section simplifies to the Two-Body Problem form. 

:::{math}
:label:
\ddot{\mathbf{R}} = - G\frac{\left(m_1+m_2\right)}{R^3}\mathbf{R}
:::

Many import results can be derived from this general form such as the analysis of the relative motion of the International Space Station, satellites, asteroids etc. among the Earth-Moon system:

Next, we can setup the total force potential as:

:::{math}
:label:
U = \frac{Gm_1}{|\mathbf{r}+\frac{m_2}{m_1+m_2}\mathbf{R}|} + \frac{Gm_2}{|\mathbf{r}-\frac{m_1}{m_1+m_2}\mathbf{R}|} 
:::

so that 

:::{math}
:label:
\ddot{\mathbf{r}} = \frac{\partial{U}}{\partial{\mathbf{r}}}
:::

In many scenarios, assume $|\mathbf{R}|$ is constant such that $P_1$ and $P_2$ are in mutual circular orbit. This is certainly a valid assumption for systems such as Earth-Moon, or the Earth-Sun. 

In a rotating coordinate frame, the position vector for the Three-Body system can be represented as:

:::{math}
:label:
\mathbf{R} = \left[ \cos\left(nt\right)\mathbf{\hat{x}}+ \sin\left(nt\right) \mathbf{\hat{y}} \right]
:::
where $n$ is the mean motion of the primary body system.

:::{math}
:label:
n = \sqrt{\frac{G\left(m_1+m_2\right)}{R^3}} = n_{12}
:::
Now shift the coordinate system to a rotating frame such that $\mathbf{R}$ is stationary and vector $\mathbf{R}$ is stationary along the local x-coordinate axis ($\hat{\mathbf{x}}_R$). 

For example, consider the Earth-Moon system the x-coordinate axis is always from the Earth to the Moon and is rotating at a rate of $\mathbf{n}$:

```{figure} ./images/jacobi_frame_shift.png
:name: fig:jacobi_frame_shift
:width: 90%
**Figure 1.3** Jacobi Coordinate Frame Shifted to The Rotating Frame
```

Where the angular velocity ($\Omega$) is defined as:

:::{math}
:label:
\mathbf{\Omega} = n\mathbf{\hat{z}}
:::

It is useful to relate the inerital position vector ($\mathbf{r}_I$) to the rotational vector ($\mathbf{r}_R$):

:::{math}
:label:
\mathbf{r}_I = \mathbf{r}_R
:::

The velocity in the inertial frame is:

:::{math}
:label:
\dot{\mathbf{r}}_I = \dot{\mathbf{r}}_R + \mathbf{\Omega}\times\mathbf{r}_R
:::

The acceleration in the inertial frame is:

:::{math}
:label: r_ddot_i_to_rot
\ddot{\mathbf{r}}_I = \ddot{\mathbf{r}}_R + \dot{\mathbf{\Omega}}\times\mathbf{r}_R + 2\mathbf{\Omega}\times\dot{\mathbf{r}}_R+\mathbf{\Omega}\times\left(\mathbf{\Omega}\times\mathbf{r}_R \right)
:::

Note that $\dot{\Omega} = 0$ since we assumed the orbit is circular. In other words $n$ is constant.

Let $\mathbf{r}_R$ be the position in the rotating coordinate frame. $\mathbf{R}_R = \mathbf{r}$

We can rewrite Equation {eq}`r_ddot_i_to_rot` as:

:::{math}
\ddot{\mathbf{r}}_I = \ddot{\mathbf{r}} + 2\mathbf{\Omega}\times\dot{\mathbf{r}}+\mathbf{\Omega}\times\left(\mathbf{\Omega}\times\mathbf{r} \right) = \frac{\partial{U}}{\partial{\mathbf{r}}}
:::

:::{math}
:label: r_ddot_i_to_rot_simp
\ddot{\mathbf{r}}_I = \ddot{\mathbf{r}} + 2n\mathbf{\hat{z}}\times\dot{\mathbf{r}} + n^2\mathbf{\hat{z}} \times \left( \mathbf{\hat{z}} \times \mathbf{r}\right)= \frac{\partial{U}}{\partial{\mathbf{r}}}
:::

As part of the rotating coordinate frame, it is convenient to write Equation {eq}`r_ddot_i_to_rot_simp` in vector form by breaking [$2n\mathbf{\hat{z}}\times\dot{\mathbf{r}}$] and [$n^2\mathbf{\hat{z}} \times \left( \mathbf{\hat{z}} \times \mathbf{r}\right)$] into their components.

Thus, the set of equations of the Three-Body Problem for the circular restricted problem in the rotating coordinate frame are:

:::{math}
:label: cr3bp_eom

\ddot{x} - 2n\dot{y} = n^2x + \frac{\partial{U}}{\partial{x}}

\ddot{y} + 2n\dot{x} = n^2y + \frac{\partial{U}}{\partial{y}}

\ddot{z} = \frac{\partial{U}}{\partial{z}}

:::

```{note}
The components of [$2n\mathbf{\hat{z}}\times\dot{\mathbf{r}}$] are usually referred to as the **tidal terms** in Astrodynamics. Think of this as $P_2$ orbits $P_1$ every orbital period there is a force experience directly as a function of $n$

:::{math}
\begin{matrix}
 - 2n\dot{y} \\  
 + 2n\dot{x} \\  
\end{matrix} = \text{Tidal Terms}
:::

```

These equations represent where the spacecraft is relative to the Jacobian Coordinate frame. [Figure 1.4](jacobi_frame_shift_updated) below shows an updated frame of reference:


```{figure} ./images/jacobi_frame_shift_updated.png
:name: jacobi_frame_shift_updated
:width: 90%
**Figure 1.4** Circular Restricted Three-Body Problem in the Jacobian Coordinate Frame
```

```{note}

In Astrodynamics the mass ratios are generally defined as:

:::{math}
:label:
\begin{align*}
\mu &= \frac{m_2}{m_1+m_2} \\
1 - \mu &= \frac{m_1}{m_1+m_2} 
\end{align*}
:::

```

The total force potential for this system can be given as:

:::{math}
:label:
U\left(\mathbf{r} \right) = \frac{Gm_1}{\sqrt{\left( x + \frac{m_2}{m_1+m_2}R \right)^2+y^2+z^2}} + \frac{Gm_2}{\sqrt{\left( x - \frac{m_1}{m_1+m_2}R \right)^2+y^2+z^2}}

:::

Let us write this a bit more concisely by defining a new force potential as $\mathbf{V}$ in order to simplify our equations of motion Equation {eq}`cr3bp_eom`:

:::{math}
:label: cr3bp_V

\mathbf{V}\left(x,y,z\right) = \frac{1}{2}n^2\left( x^2 + y^2 \right) + \mathbf{U}
:::

:::{math}
:label:
\mathbf{U} = \frac{Gm_1}{r_1} + \frac{Gm_2}{r_2}
:::

where $r_1$ and $r_2$ are:
:::{math}
r_1 = \sqrt{\left( x + \frac{m_2}{m_1+m_2}R \right)^2+y^2+z^2}
:::

:::{math}
r_ 2 = \sqrt{\left( x - \frac{m_1}{m_1+m_2}R \right)^2+y^2+z^2}
:::

```{note}
The potential energy is made up of three components

1. The potential energy due to the force induced by the rotating reference frame
2. The gravitational potential energy from $P_1$
3. The gravitational potential energy from $P_2$

```

[Figure 1.5](cr3bp_potent) below is an example of solving Force Potential {eq}`cr3bp_V` for the Earth-Moon system. The figure is interactive and generated using [Plotly](https://plotly.com/python/), an open-source graphing library for Python. The reader is encouraged to interact with [Figure 1.5](cr3bp_potent) using their mouse to zoom into the region of space around the bodies and rotate the surface to inspect the potential wells.

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import cr3bp_potential_plot
cr3bp_fig1 = cr3bp_potential_plot.force_potential()
glue("cr3bp_potent",cr3bp_fig1)
```

```{glue:figure} cr3bp_potent
:align: center
:name: cr3bp_potent
**Figure 1.5.** Example of CR3BP Potential
```

Finally, the equations of motion for the **Circular Restricted Three-Body Problem** becomes:

:::{math}
:label: cr3bp_eom_simp
\begin{align*}
\ddot{x} - 2n\dot{y} &= \frac{\partial{\mathbf{V}}}{\partial{x}} \\
\ddot{y} + 2n\dot{x} &= \frac{\partial{\mathbf{V}}}{\partial{y}} \\
\ddot{z} &= \frac{\partial{\mathbf{V}}}{\partial{z}}
\end{align*}
:::


## Non-Dimensional Circular Restricted Three-Body Problem 


Non-dimensionalization of the Circular Restricted Three-Body Problem has the advantage of solving one problem and applying the results to a general number of problems. The system is generalized for any Three-Body Problem by removing the dependence of the rotating reference rate.

Normalize the equations for the Three-Body Problem along 3 physical properties of the system 

### 1. Mass

As shown by [Figure 1.4](jacobi_frame_shift_updated) the primary masses are normalized such that: 

:::{math}
:label:
\begin{align*}
\mu &= \frac{m_2}{m_1+m_2} \\
1 - \mu &= \frac{m_1}{m_1+m_2} 
\end{align*}

:::

This allows our equations of motion to be independent of the primary masses and relies more on their relative size ratio. 

### 2. Length

As described by the [Jacobian Coordinate Frame](introduction.md#jacobian-coordinate-frame) section the characteristic length of the Three-Body system is the vector $\mathbf{R}$. Define the non-dimensional length scale as $\mathbf{R}$ and normalize position vectors $\mathbf{r_1}$, $\mathbf{r_2}$, etc. 

the length scale is:

:::{math}
r_s = R
:::

and yields the non-dimensional length term

:::{math}
:label:
\mathbf{r}^* = \frac{\mathbf{r}}{r_s} = \frac{\mathbf{r}}{R}
:::

### 3. Time

The time scale is simply normalized against the period of the circular orbit such that:

:::{math}
t_s = \frac{1}{n}
:::

this yields the non-dimensional time term:

:::{math}
:label:
\tau = nt
:::

---

Now apply the non-dimensional terms to Equation {eq}`cr3bp_eom_simp` to get non-dimensional equations of motion:


:::{math}
:label: cr3bp_eom_norm
\begin{align*}
n^2R\ddot{x}^* - 2n^2R\dot{y}^* &= \frac{1}{R}\frac{\partial{\mathbf{V}}}{\partial{x^*}} \\
n^2R\ddot{y}^* - 2n^2R\dot{x}^* &= \frac{1}{R}\frac{\partial{\mathbf{V}}}{\partial{x^*}} \\
n^2R\ddot{z}^* &= \frac{1}{R}\frac{\partial{\mathbf{V}}}{\partial{z^*}}
\end{align*}

:::

Normalize the force potential Equation {eq}`cr3bp_V` as:

:::{math}
:label:

\mathbf{\tilde{V}} = \frac{\mathbf{V}}{n^2R^2}

:::

The equations of motion for the **Non-Dimensional Circular Restricted Three-Body Problem** become: 

:::{math}
:label: cr3bp_eom_norm_simp
\begin{align*}
\ddot{x}^* - 2\dot{y}^* &= \frac{\partial{\tilde{\mathbf{V}}}}{\partial{x^*}} \\
\ddot{y}^* + 2\dot{x}^* &= \frac{\partial{\tilde{\mathbf{V}}}}{\partial{y^*}} \\
\ddot{z}^* &= \frac{\partial{\tilde{\mathbf{V}}}}{\partial{z^*}}
\end{align*}
:::

Note that this looks similar to the equations of motion for the Circular Restricted Three-Body Problem{eq}`cr3bp_eom_simp` it's just that the definition of $\mathbf{\tilde{V}}$ and $\mathbf{\tilde{U}}$ are different. Different in the sense that we scaled the force potential. 

:::{math}
:label: cr3bp_V_norm
\mathbf{\tilde{V}}\left(x^*,y^*,z^*\right) = \frac{1}{2}\left( {x^*}^2 + {y^*}^2\right) + \mathbf{\tilde{U}}
:::

:::{math}
:label:
\mathbf{\tilde{U}} = \frac{U}{n^2R^2}
:::

We assume for the **Non-Dimensional Restricted Three-Body Problem** that $\mu < \frac{1}{2}$. This is not a bad assumptions for most problems we are Non-Dimensional Restricted Three-Body Problem that in solving. If not one can always swap $m_1$ and $m_2$.

The gravity potential can be written as 

:::{math}
:label: cr3bp_U_norm
\mathbf{\tilde{U}} = \frac{1-\mu}{r^*_1} + \frac{\mu}{r^*_2}
:::

where $r^*_1$ and $r^*_2$ are:

:::{math}
\begin{align*}
r^*_1 &= \sqrt{\left( x^* + \mu \right)^2+{y^*}^2+{z^*}^2} \\
r^*_2 &= \sqrt{\left( x^* - 1 + \mu \right)^2+{y^*}^2+{z^*}^2}
\end{align*}
:::

[Figure 1.6](cr3bp_nondim_potent) below is an example of solving the Non-Dimensional Force Potential {eq}`cr3bp_V_norm`. Since [Figure 1.5](cr3bp_potent) gave an example for the Earth-Moon system ($\mu = 0.012156$) this example exaggerates the potential wells by looking at a large mass ratio of $\mu=0.09$. Again, the reader is encouraged to interact with [Figure 1.6](cr3bp_nondim_potent) using their mouse to zoom into the region of space around the bodies and rotate the surface to inspect the potential wells.

```{code-cell} ipython3
:tags: ["remove-input"]
from myst_nb import glue
import cr3bp_potential_plot
cr3bp_fig2 = cr3bp_potential_plot.non_dim_force_potential()
glue("cr3bp_nondim_potent",cr3bp_fig2)
```

```{glue:figure} cr3bp_nondim_potent
:align: center
:name: cr3bp_nondim_potent
**Figure 1.6.** Example of Non-Dimensional CR3BP Potential
```

Given a solution for the the Non-Dimensional Circular Restricted Three-Body Problem ($\mathbf{r^*}$, $\mathbf{\dot{r}^*}$) we can transform back to dimensional system by introducing $\mathbf{R}$, $m_1$ and $m_2$ and solving for the mean motion of the two masses:

:::{math}
n = \sqrt{\frac{G\left( m_1 + m_2 \right)}{R^3}}
:::

:::{math}
\begin{matrix}
 x = Rx^* & \dot{x} = nR\dot{x}^* \\  
 y = Ry^* & \dot{y} = nR\dot{y}^* \\  
 z = Rz^* & \dot{z} = nR\dot{z}^* \\  
\end{matrix}
:::


The advantage of this transformation is that by solving one non-dimensional problem, is actually solves **infinite** number of problems in a dimensional set!


## Python Example

Using the functions derived in this section let's walk through a simple example of solving for the trajectory of a spacecraft among the Earth-Moon system. 

The Earth-Moon mass ratio is:

:::{math}
\mu = 0.012150515586657583
:::

In the rotating frame the initial position and velocity normalized vectors are given as:

:::{math}
:label: py_example_state
\mathbf{r}^*(t_0) = 
\begin{bmatrix}
0.50 \\
0.50  \\
0.00
\end{bmatrix}

\mathbf{v}^*(t_0) = 
\begin{bmatrix}
0.01 \\
0.01 \\
0.00
\end{bmatrix}
:::

Begin by importing module [three_body_problem](https://github.com/thatguyeddieo/Astrodynamics/blob/main/Three_Body_Problem/three_body_problem.py) and setting the initial state vector {eq}`py_example_state`

```python
import numpy as np
import three_body_problem as three_body_problem

# Initial State Vectors
# --------------------------------------------------------------------------------
initial_pos = [0.50, 0.50, 0.0]
initial_vel = [0.01, 0.01, 0.0]
```

Instantiate class `three_body_problem.cr3bp()` with the initial state vector and set the mass ratio $\mu$ for the analysis of the Earth-Moon system.

```python

# Instantiate CR3BP Object:
# --------------------------------------------------------------------------------
# Set Earth-Moon Mass Ratio
mu = 0.012150515586657583
sc = three_body_problem.cr3bp(initial_pos,initial_vel)
sc.mu = mu
```

For this example analysis the trajectory of the spacecraft up to a non-dimensional time of $8\pi$.

```python
# Numerical Analysis Setup
# --------------------------------------------------------------------------------
sc.time = np.linspace(0, 2*np.pi*4, 10000)
```

The numerical solver relies on running [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) for solving the initial value problem for the system of non-dimensional {eq}`cr3bp_eom_norm_simp` ordinary differential equations. Note that when taking the partial derivate of $\tilde{V}$ or $\tilde{U}$ the distance vectors $\mathbf{r^*}(t)$ are a function of time and must be decomposed in the process. 

:::{math}
:label: odes_1
\mathbf{\dot{r}}^*
= 
\begin{bmatrix}
v^*_x\\
v^*_y \\
v^*_z
\end{bmatrix}
:::

:::{math}
\mathbf{\ddot{r}}^*
= 
\begin{bmatrix}
2v_y + x - \frac{\left(1-\mu\right)\left(x+\mu \right)}{{r^*_1}^3} - \frac{\mu\left(x + \mu -1\right)}{{r^*_2}^3}\\
-2v_x + y\left[1 - \frac{1-\mu}{{r^*_1}^3} - \frac{\mu}{{r^*_2}^3}\right] \\
-z \left[ \frac{1-\mu}{{r^*_1}^3}  + \frac{\mu}{{r^*_2}^3} \right]
\end{bmatrix}
:::

Solve for the spacecraft trajectory. By flagging the argument `saveAnalysis = True ` the numerical solution is saved off as a pickle file. This gives the a time advantage of solving a complex initial value problem only once and loading the results later for post-processing.

```python
# Run Numerical Analysis: scipy.integrate methods
# --------------------------------------------------------------------------------
# Run scipy solver 
sc.solve_threeBody_trajectory(saveAnalysis=False)

# Extract Results
position_numerical = sc.position_numerical
velocity_numerical = sc.velocity_numerical
```

The default absolute tolerance is set to 1e-10 and relative tolerance is also set to 1e- 10. However, they can be updated prior to running `solve_threeBody_trajectory` as:

```python
# Set up tolerances, relative & absolute
sc.relTol = 1e-12
sc.absTol = 1e-13
```

The full [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) solution is assigned to `sc.num_sol` but for convenience the position and velocity time history are store as `sc.position_numerical` and `sc.position_numerical`.

Plotting the results shows the spacecraft’s trajectory for a non-dimensional time of $8\pi$. It appears to be stable while orbiting the Earth at some periodic rate. To better illustrate the time of flight a blue gradient trajectory is plotted along non-dimensional axes showing where the spacecraft started and ended along the Earth-Moon system. 


```{figure} ./images/cr3bp_example.jpeg
:name: fig:cr3bp_example
:width: 100%
**Figure 1.7** Example Solution to the CR3BP in the Rotating Reference Frame
```


TODO: Add a more exciting CR3BP trajectory example, also add figure/plot of trajectory in inertial frame