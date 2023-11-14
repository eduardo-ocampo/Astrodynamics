# Local Dynamics

https://ocw.mit.edu/courses/16-346-astrodynamics-fall-2008/resources/lec_19/

https://space.stackexchange.com/questions/20590/how-to-best-think-of-the-state-transition-matrix-and-how-to-use-it-to-find-peri#:~:text=The%20State%20Transition%20Matrix%20(STM,over%20short%20period%20of%20times.

Juan Senent, Cesar Ocampo, and Antonio Capella; Low-Thrust Variable-Specific-Impulse Transfers and Guidance to Unstable Periodic Orbits. Journal of Guidance, Control, and Dynamics, 28 (2) March–April 2005:

TODO: fix (t) to \left( t \right) in LaTex
TODO: Figure out where to place this. Thinking part of two-body section

Consider a spacecraft at initial state $\mathbf{x}_0$ undergoing some deviation $\delta \mathbf{x}$ at time $t_0$. As shown in [Figure 1](local_dynamics_initial) below. Assume we are interested in knowing how to determine the state history of the deviation vector $\delta \mathbf{x}(t)$

```{figure} ./images/local_dynamics_initial.png
:name: local_dynamics_initial
:width: 100%
**Figure X.X** TITLE
```

Up to now, the strategy for handling this type of problem involving numerically integrating a trajectory given an initial condition vector (see [Solving The Two-Body Problem](/Two_Body_Problem.md#solving-the-two-body-problem)) up to a final time $t_f$. With that approach, one can determine the deviation state $\delta \mathbf{x}$ by computing the difference between the integrated deviated trajectory $\mathbf{x}$ with the nominal trajectory $\mathbf{x}_n$ 

:::{math}
:label: ld_problem
\delta \mathbf{x}\left(t\right)  = \mathbf{x}\left(t\right) - \mathbf{x}_n\left(t \right) 
:::

Given the following initial state vectors 

:::{math}
:label: nominal_state_vector

\mathbf{{x}_{n,0}} = \begin{bmatrix} 
    x_0       \\ y_0       \\ z_0 \\
    \dot{x_0} \\ \dot{y_0} \\ \dot{z_0}
\end{bmatrix} 
:::

:::{math}
\mathbf{{x}_{0}} = \begin{bmatrix} 
    x_0 + \delta{x_0}      \\ y_0 + \delta{y_0}       \\ z_0 + \delta{z_0} \\
    \dot{x_0} + \delta{\dot{x_0}} \\ \dot{y_0} + \delta{\dot{x_0}} \\ \dot{z_0} + \delta{\dot{x_0}}
\end{bmatrix}
:::

Although this method is a valid approach, this section deals with getting an approximation solution for the derviation state without directly intergrating both trajectory states {eq}`ld_problem` by introductioning what is know is Astrodynamics as the **State Transiton Matrix**.

## Introduction

The State Transition Matrix (STM) is a linearization of a dynamical system. It can be used as a  simplify method for progating system dynamics over a given time. 

Let $\mathbf{x}$ be the state of the sytstem. Begin by generalizing the equations of motion as:

:::{math}
:label: general_eoms
\mathbf{\dot{x}}\left(t\right) = \mathbf{g}\left( t;\mathbf{x}_0 \right)
:::

where $\mathbf{g}$ is some general state function which is a function of time based on  initiail state vector $\mathbf{x}_0$.

For example, for the [Two-Body Problem](Two_Body_Problem.md) $\mathbf{g}$ is

:::{math}
:label: 

\mathbf{g} = 
\begin{bmatrix} 
\mathbf{\dot{r}} \\
-\frac{\mu}{r^3}\mathbf{r}
\end{bmatrix} 

:::

Once we have $\mathbf{x}_0$ we can propagate forwards or backwards in time $t_f$.

Now consider a small deviation in $\mathbf{x}$, how would its equations of motion change as a function of time? We can take the difference:

:::{math}
:label: ld_deviated_x
\delta\mathbf{\dot{x}} = \mathbf{g}\left(t;\mathbf{x}_0+\delta\dot{x}_0\right) - \mathbf{g}\left(t;\mathbf{x}_0\right)
:::


where it is assumed that 

:::{math}
||\delta{\mathbf{x}}|| \ll ||\mathbf{x}||
:::

Often the deviation vector is thought of as a sort of localized effect. Local in the sense that it is relative to the nominal trajectory based on $\mathbf{x}_0$ as shown in [Figure X.X](local_dynamics_propagation):


```{figure} ./images/local_dynamics_propagation.png
:name: local_dynamics_propagation
:width: 100%
**Figure X.X** TITLE
```

Let's attempt to solve Equation {eq}`ld_deviated_x` using [Taylor Series Expansion](https://mathworld.wolfram.com/TaylorSeries.html). Suppose we have an infinitely differentiable, real function $\mathbf{g}\left({\mathbf{x}}\right)$ with $\mathbf{g}$ , $\mathbf{x} \in \mathbb{R}^n$ where $n$ comes from the state being nth-dimensional. The Taylor series expansion about some  point $\mathbf{x}$ = $\mathbf{a}$ is defined below for the $i^{th}$ component of $\mathbf{g}\left(\mathbf{x} \right)$:

:::{math}
:label: gi_taylor
g_i\left( \mathbf{x} \right) = \sum_{n=0}^{\infty} \frac{1}{n!}\left[\left( \mathbf{x} - \mathbf{a}\right)\cdot \nabla_a  \right]^n g_i\left(\mathbf{a} \right)
:::


where ${\nabla}_a$ is a gradient operator of n-dimensional. 

Re-ordering gives:

:::{math}
:label: gix_gia_taylor
g_i\left( \mathbf{x} \right) - g_i\left( \mathbf{a} \right) =  \sum_{n=1}^{\infty} \frac{1}{n!}\left[\left( \mathbf{x} - \mathbf{a}\right)\cdot \nabla_a  \right]^n g_i\left(\mathbf{a} \right)
:::

Now lets say instead of truncating the expansion {eq}`gi_taylor` and {eq}`gix_gia_taylor` at infinity we apply the $M^{th}$-order Taylor expansion. The equations of motion can be written for the $i^{th}$ component of $\delta\mathbf{\dot{\mathbf{x}}}$ as:

:::{math}
:label: dxi_taylor_expan
\delta\mathbf{\dot{\mathbf{x}}_i} = \sum_{p=1}^{M}\frac{1}{p!} g_{i,\gamma_1,\dots\gamma_p} \delta x^{\gamma_1} \dots \delta x^{\gamma_p}
:::

where $\gamma_j \in \left\{1,\dots,N \right\}$ and the subscript $\gamma_j$ represents the $\gamma^{th}_j$ component of the state vectors $\mathbf{x}$. In this form the term $g_{i,\gamma_1,\dots\gamma_p}$ is:

:::{math}
g_{i,\gamma_1,\dots \gamma_p} = \frac{\partial^p g_i\left( t,\mathbf{x} \right)}{\partial x_{\gamma_1} \dots \delta x_{\gamma_p}}
:::


## First-Order Dynamics and The State Transition Matrix

For a typical Astrodynamics problem, $M = 1$ is often considered for solving the equations of motion when evaluating Equation {eq}`dxi_taylor_expan`. Consider the equations of motion are given:

:::{math}
:label:
\mathbf{\dot{x}} = \mathbf{g}\left( \mathbf{x} \right)
:::

With $\phi$ as the solution 


:::{math}
:label: x_phi_solution
\mathbf{x}\left( t \right) = \phi \left(t;\mathbf{x}_0,t_0 \right)
:::

Taking the derivative of the solution with respect to the initial states gives rise to the State Transition Matrix ($\mathbf{\Phi}$) which maps from current time to some different time $t$:

:::{math}
:label: stm_def
\mathbf{\Phi}\left( t,t_0 \right) = \frac{\partial\phi}{\partial\mathbf{x}_0}
:::

or using Expression {eq}`x_phi_solution` this can also be thought as:

:::{math}
:label: stm_general
\mathbf{\Phi}\left( t,t_0 \right) = \frac{\partial\mathbf{x}}{\partial\mathbf{x}_0}
:::

such that

:::{math}
:label:
\frac{d \mathbf{\Phi}}{dt} = \frac{\partial\mathbf{g}\left(t,\mathbf{x} \right)}{\partial\mathbf{x}} \mathbf{\Phi}
:::

By using the definition of the STM in the form of {eq}`stm_general` then the deviation vector to the first-order becomes a linear equation:

:::{math}
:label: deviated_stm
\delta\mathbf{x} =  \mathbf{\Phi}\left( t,t_0\right) \delta \mathbf{x}_0
:::


For the [Two-Body Problem](ref) $\mathbf{\Phi}$ is a symplectic 6x6 matrix with $det(\mathbf{\Phi}) = 1$. This mean we can also solve for $\delta\mathbf{x}_0$ and are allowed to easily change time from $t$ to $t_0$ in either direction:

:::{math}
:label: devivated_stm_forward_backward
\begin{align*}
\delta\mathbf{x}_0 &= \mathbf{\Phi}^{-1}\left(t,t_0 \right) \delta\mathbf{x} \\
\delta\mathbf{x}_0 &= \mathbf{\Phi}\left(t_0,t\right) \delta\mathbf{x}
\end{align*}
:::

$\mathbf{\Phi}$ tells us is how to map from the initial state $t_0$ to some different time (forwards or backwards.) thus Expression {eq}`deviated_stm` also maps the deviation vector forwards or backwards as shown in Expression {eq}`devivated_stm_forward_backward` and illustrated in [Figure X.X](local_dynamics_stm).

```{figure} ./images/local_dynamics_stm.png
:name: local_dynamics_stm
:width: 100%
**Figure X.X** TITLE
```

Now determine the time derivative of our deviation vector $\delta \mathbf{\dot{x}}$ by reducing the $M^{th}$-order Taylor expansion {eq}`dxi_taylor_expan`. For our case of $\mathbf{\dot{x}} = \mathbf{g}\left( \mathbf{x} \right)$ and letting $M = 1$ reduces to:

:::{math}
:label:
\delta \mathbf{\dot{x}}\left( t \right) = \frac{\partial{\dot{\mathbf{x}}}}{\partial\mathbf{x}} \delta{\mathbf{x}} 
:::

or by substituting $\mathbf{\Phi}$ {eq}`stm_general`:

:::{math}
:label:
\begin{align*}
\delta \mathbf{\dot{x}}\left( t \right) &= \frac{\partial{\dot{\mathbf{x}}}}{\partial\mathbf{x}} \frac{\partial\mathbf{x}}{\partial\mathbf{x}_0} \delta\mathbf{x}_0 \\
\delta \mathbf{\dot{x}}\left( t \right) &= A \mathbf{\Phi} \delta{\mathbf{x}_0}
\end{align*}
:::

Resulting in the time derivative of $\mathbf{\Phi}$ as:

:::{math}
:label: phi_a_dt
\mathbf{\dot{\Phi}} = A \mathbf{\Phi}
:::

The use of the state transition matrix to obtain the deviation vector $\delta\mathbf{x}$ {eq}`deviated_stm` for some time $t_f$ is semi-analytic because the method still requires integration of $\mathbf{\phi}$. 
However, the advantage for using the linear analysis governed by the STM is that it is much faster to use than directly integration the trajectory governed by nominal trajectory. 

For example, consider solving the deviation vector for the Two-Body Problem. Integrating the nominal and deviation trajectory directly requires solving 6 equations of motions for each state or 12 equations altogether. Whereas the STM method requires solving 36 equations for $\mathbf{\Phi}$ and 6 equations for th nominal trajectory so 42 equations altogether. For this scenario solving the trajectory directly is faster. However, suppose you need to do this for 100 times. Solving directly requires one to integrate a total of 1,200 equations whereas solving 100 times using the STM linear approximation require only solving for $\mathbf{\Phi}\left(t,t_0 \right)$ once or solving for 42 equations and is much faster to use. The penalty paid for speed is lost in accuracy. The STM method is an approximation and is best used to for short periods of time. Solving the equations directly is more accurate for longer time spans. TODO Point to example.

TODO: Point to example?


## Planar Two-Body Problem Example

We can integrate the State Transition Matrix together with the Two-Body Problem equations of motion.  

:::{math}
\begin{align*}
\mathbf{\dot{x}} = \mathbf{g}\left(\mathbf{x}\right) &= 
\begin{bmatrix} 
\mathbf{\dot{r}} \\
-\frac{\mu}{r^3}\mathbf{r}
\end{bmatrix}  \\
\mathbf{\dot{\Phi}} &= \frac{\partial\mathbf{g}}{\partial\mathbf{x}}\mathbf{\Phi}
\end{align*}
:::

Given the following initial state:

:::{math}
\mathbf{x}_0 = 
\begin{bmatrix}
\mathbf{r}_0 \\
\mathbf{v}_0
\end{bmatrix}
:::

and

:::{math}
\mathbf{\Phi}_0 = \mathbf{I}_{4x4}
:::

Then $A$ from the linearized equations formulated {eq}`phi_a_dt` becomes:

:::{math}
A = \frac{\partial\mathbf{\dot{x}}}{\partial\mathbf{x}} = 
\begin{bmatrix}
\frac{\partial\mathbf{\dot{r}}}{\partial{\mathbf{r}}} & \frac{\partial\mathbf{\dot{r}}}{\partial{\mathbf{v}}} \\
\frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{r}}} & \frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{v}}}
\end{bmatrix}
:::

The only partial that is non-zero or $I$ in this case is $\frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{r}}}$

:::{math}
A = \frac{\partial\mathbf{\dot{x}}}{\partial\mathbf{x}} = 
\begin{bmatrix}
0 & I \\
\frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{r}}} & 0
\end{bmatrix}
:::

Evalute $\frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{r}}}$:

:::{math}
\frac{\partial\mathbf{\dot{v}}}{\partial{\mathbf{r}}} =  \frac{\partial}{\partial\mathbf{r}}\left[ -\frac{\mu}{r^3}\mathbf{r} \right] =
\begin{bmatrix}
-\frac{\mu}{r^3} + \frac{3 \mu x^2}{r^5} & \frac{3\mu x y }{r^5} \\
\frac{3\mu x y }{r^5}  & -\frac{\mu}{r^3} + \frac{3\mu y^2}{r^5}
\end{bmatrix}
:::

so that $A$ is now:

:::{math}
A =
\begin{bmatrix}
0 & 0  & 1 & 0  \\
0 & 0  & 0 & 1  \\
-\frac{\mu}{r^3} + \frac{3 \mu x^2}{r^5} & \frac{3\mu x y }{r^5} & 0 & 0  \\
\frac{3\mu x y }{r^5}  & -\frac{\mu}{r^3} + \frac{3\mu y^2}{r^5} & 0 & 0 
\end{bmatrix}

:::

Once we numerically solved for $\mathbf{\Phi}$ up to $t_f$ we can then easilty progagte back and forth in time by simply mulitplyhing by $\mathbf{\Phi}\left( t_i,t_o \right)$


```{figure} ./images/local_dynamics_stm_propagate.png
:name: local_dynamics_stm_propagate
:width: 100%
**Figure X.X** TITLE
```


From $t_0\rightarrow t_i$ and $t_0 \rightarrow t_f$ we can solve for $t_i \rightarrow t_f$.

:::{math}

\left.\begin{aligned}
\delta \mathbf{x}_i = \mathbf{\Phi}\left( t_i,t_o \right) \delta \mathbf{x}_0 \\
\delta \mathbf{x}_f = \mathbf{\Phi}\left( t_f,t_o \right) \delta \mathbf{x}_0 
\end{aligned}\right\}
\delta \mathbf{x}_f = \mathbf{\Phi}\left( t_f,t_i \right) \delta \mathbf{x}_i
:::

such that:

:::{math}
\begin{align*}
\mathbf{\Phi}\left(t_f,t_i \right) &= \mathbf{\Phi}\left(t_f,t_0 \right) \mathbf{\Phi}^{-1}\left(t_i,t_0 \right) \\
&= \mathbf{\Phi}\left(t_f,t_0 \right) \mathbf{\Phi}\left(t_0,t_i \right) \\
\end{align*}
:::

This derivation is important for mapping various times between two times and only numerically solving for $\mathbf{\Phi}$ once.


## Python Example



Introduce problem statement 

**Initial Conditions** 

:::{math}
:label: localdynamics_example_ivp_r
\mathbf{r}(t_0) = 
\begin{bmatrix}
8000 \\
200  \\
0
\end{bmatrix} km
::: 

:::{math}
:label: localdynamics_example_ivp_v
\mathbf{v}(t_0) = 
\begin{bmatrix}
0 \\
8 \\
0
\end{bmatrix} \frac{km}{sec}
::: 

**Initial Devivation**

:::{math}
:label: devivaiton_vec_r
\delta\mathbf{r}(t_0) = 
\begin{bmatrix}
1 \\
1  \\
1
\end{bmatrix} km
::: 

:::{math}
:label: devivaiton_vec_v
\delta\mathbf{v}(t_0) = 
\begin{bmatrix}
0 \\
1 \\
0
\end{bmatrix} \frac{mm}{sec}
::: 

Talk about comparing two methods

Method 1 is STM

Method 2 is Nomial Trajectory + Deviated Trajectory

Point to [Two-Body Problem Example](Two_Body_Problem.md#solving-the-two-body-problem)


Script Snippets to include

Initial Devivation Vector
```python
# devivation vector
initial_dx = [1,1,1,0e-6,1e-6,0e-6]

deviated_position = np.array(initial_pos) + np.array(initial_dx[:3])
deviated_velocity = np.array(initial_vel) + np.array(initial_dx[3:])
```

Since solving STM need initial phi, which is just identiy of size 36 (symtem of equations)

```python
initial_phi = np.eye(6).reshape(36)
```

Class module `two_problem` has class twoBody_STM

```python
sc_stm = twoBody_problem.twoBody_STM(initial_pos,initial_vel,initial_phi) # State Transition Matrix Methods
```

Run solver
```python
# Run scipy analysis for STM Method
# --------------------------------------
sc_nominal.solve_twoBody_trajectory(saveAnalysis=False)
sc_deviated.solve_twoBody_trajectory(saveAnalysis=False)
sc_stm.solve_twoBody_problem(saveAnalysis=False)
```

Calc stuff of interest 
```python
# Get determinate of STM
sc_stm.stm_det_numerical = [determinant(np.reshape(p,(6,6))) 
                        for p in sc_stm.phis_numerical]

# From results, determine Devivation Vector
dX_0 = np.array([initial_dx]).T
sc_stm.dX_numerical = np.array([np.dot(np.reshape(p,(6,6)),dX_0) 
                            for p in sc_stm.phis_numerical])
```


Plots

```{figure} ./images/local_dynamics_stm_solution.png
:align: center
:name: local_dynamics_stm_solution
:width: 100%
**Figure X.X** Title
```

```{figure} ./images/local_dynamics_solution_diff.png
:align: center
:name: local_dynamics_solution_diff
:width: 100%
**Figure X.X** Title
```

```{figure} ./images/local_dynamics_trajectory_diff.png
:align: center
:name: local_dynamics_trajectory_diff
:width: 100%
**Figure X.X** Title
```