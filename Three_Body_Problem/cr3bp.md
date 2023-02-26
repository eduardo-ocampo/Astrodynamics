
# Circular Restricted Three-Body Problem 

By letting $m_3 \rightarrow 0$ then Equation 10-11 as derived from the [Jacobian Coordinate Frame](introduction.md/#jacobian-coordinate-frame) simplifies to the Two-Body Problem form. 

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

These equations represent where the spacecraft is relative to the Jacobian Coordinate frame. **Figure 1.4** shows an update frame of reference:


```{figure} ./images/jacobi_frame_shift_updated.png
:name: fig:jacobi_frame_shift_updated
:width: 90%
**Figure 1.4** Circular Restricted Three-Body Problem in the Jacobian Coordinate Frame
```

```{note}

In Astrodynamics the mass ratios are generally defined as:

:::{math}
:label:
\mu = \frac{m_2}{m_1+m_2} 

1 - \mu = \frac{m_1}{m_1+m_2} 

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

V\left(x,y,z\right) = \frac{1}{2}n^2\left( x^2 + y^2 \right) + U
:::

:::{math}
U = \frac{Gm_1}{r_1} + \frac{Gm_2}{r_2}
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

Finally, the equations of motion for the **Circular Restricted Three-Body Problem** become:

:::{math}
:label: cr3bp_eom_simp

\ddot{x} - 2n\dot{y} = \frac{\partial{V}}{\partial{x}}

\ddot{y} + 2n\dot{x} = \frac{\partial{V}}{\partial{y}}

\ddot{z} = \frac{\partial{V}}{\partial{z}}

:::


TODO: Create a plot of V potential for an arbitrary mu

## Non-Dimensional Circular Restricted Three-Body Problem 

Non-dimensionalization of the Circular Restricted Three-Body Problem has the advantage of solving one problem and applying the results to a general number of problems. The system is generalized for any Three-Body Problem by removing the dependence of the rotating reference rate.

Normalize the equations for the Three-Body Problem along 3 physical properties of the system 

**1. Mass**

As shown in **Figure 1.4** the primary masses are normalized such that: 

:::{math}
:label:
\mu = \frac{m_2}{m_1+m_2} 

1 - \mu = \frac{m_1}{m_1+m_2} 

:::

This allows our equations of motion to be independent of the primary masses and relies more on their relative size ratio. 

**2. Length**

As shown in the [Jacobian Coordinate Frame](introduction.md#jacobian-coordinate-frame) the characteristic length of the Three-Body system is the vector $\mathbf{R}$. Define the non-dimensional length scale as $\mathbf{R}$ and normalize position vectors $\mathbf{r_1}$, $\mathbf{r_2}$, etc. 

the length scale is:

:::{math}
r_s = R
:::

and yields the non-dimensional length term

:::{math}
:label:
\mathbf{r}^* = \frac{\mathbf{r}}{r_s} = \frac{\mathbf{r}}{R}
:::

**3. Time**

The time scale is simply normalized against the period of the circular orbit such that:

:::{math}
t_s = \frac{1}{n}
:::

this yields the non-dimensional time term:

:::{math}
:label:
\tau = nt
:::

***********
Apply the non-dimensional terms to Equation {eq}`cr3bp_eom_simp` to get non-dimensional equations of motion:


:::{math}
:label: cr3bp_eom_norm

n^2R\ddot{x}^* - 2n^2R\dot{y}^* = \frac{1}{R}\frac{\partial{V}}{\partial{x^*}}

n^2R\ddot{y}^* - 2n^2R\dot{x}^* = \frac{1}{R}\frac{\partial{V}}{\partial{x^*}}

n^2R\ddot{z}^* = \frac{1}{R}\frac{\partial{V}}{\partial{z^*}}

:::

Normalize the force potential Equation {eq}`cr3bp_V` as:

:::{math}
:label:

\tilde{V} = \frac{V}{n^2R^2}

:::

Now the equations of motion for the **Non-Dimensional Circular Restricted Three-Body Problem** become: 

:::{math}
:label: cr3bp_eom_norm_simp

\ddot{x}^* - 2\dot{y}^* = \frac{\partial{\tilde{V}}}{\partial{x^*}}

\ddot{y}^* + 2\dot{x}^* = \frac{\partial{\tilde{V}}}{\partial{y^*}}

\ddot{z}^* = \frac{\partial{\tilde{V}}}{\partial{z^*}}

:::

Note that is this looks similar to Equation {eq}`cr3bp_eom_simp` it's just that the definition of $\tilde{V}$ and $\tilde{U}$ are different. Different in the sense that we scaled the force potential. 

:::{math}
:label: cr3bp_V_norm
\tilde{V}\left(x^*,y^*,z^*\right) = \frac{1}{2}\left( {x^*}^2 + {y^*}^2\right) + \tilde{U}
:::

:::{math}

\tilde{U} = \frac{U}{n^2R^2}
:::

We assume for the Non-Dimensional Restricted Three-Body Problem that $\mu < \frac{1}{2}$. This is not a bad assumptions for most problems we are Non-Dimensional Restricted Three-Body Problem that in solving. If not one can always swap $m_1$ and $m_2$.

The gravity potential can be written as 

:::{math}
:label: cr3bp_U_norm
\tilde{U} = \frac{1-\mu}{r^*_1} + \frac{\mu}{r^*_2}
:::

where $r^*_1$ and $r^*_2$ are:

:::{math}
r^*_1 = \sqrt{\left( x^* + \mu \right)^2+{y^*}^2+{z^*}^2}
:::

:::{math}
r^*_2 = \sqrt{\left( x^* - 1 + \mu \right)^2+{y^*}^2+{z^*}^2}
:::

Given a solution for the the Non-Dimensional Circular Restricted Three-Body Problem ($\mathbf{r^*}$, $\mathbf{\dot{r}^*}$) we can transform back to dimensional system by introducing $\mathbf{R}$, $m_1$ and $m_2$ and solving for the mean motion of the two masses:

:::{math}
n = \sqrt{\frac{G\left( m_1 + m_2 \right)}{R^3}}
:::

:::{math}

x = Rx^*, y = Ry^*, z = Rz^*
:::

:::{math}
\dot{x} = nR\dot{x}^*, \dot{y} = nR\dot{y}^*, \dot{z} = nR\dot{z}^*

:::

By solving one non-dimensional problem, we actually solve **infinite** number of problems in dimensional set.


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

Begin by importing module [three_body_problem](three_body_problem.py) and setting the initial state vector {eq}`py_example_state`

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
\frac{d}{dt}
\begin{bmatrix}
x^* \\
y^* \\
z^* \end{bmatrix}
= 
\begin{bmatrix}
v^*_x(t)\\
v^*_y(t) \\
v^*_z(t)
\end{bmatrix}
:::

:::{math}
:label: odes_2
\frac{d^2}{dt^2}
\begin{bmatrix}
x^* \\
y^* \\
z^*
\end{bmatrix}
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


```{figure} ./images/cr3bp_example.png
:name: fig:cr3bp_example
:width: 100%
**Figure 1.5** Example Solution to the Circular Restricted Three-Body Problem 
```