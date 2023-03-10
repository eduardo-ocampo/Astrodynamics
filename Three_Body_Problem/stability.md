# Stability of Equilibrium Points

The Lagrange Points are known to be equilibrium points along the potential function curve. TODO: Add reference. However, this does not necessarily mean they are **stable** equilibrium points. In Astrodynamics, a particle is stable if it returns to its initial state after being perturbed. This section looks at determining the stability of the equilibrium points Lagrange Points. 


## Introduction to Linearized Stability Analysis

Consider a spacecraft at an equilibrium point $L_i$, satisfied by initial state ($x_0$,$y_0$,$z_0$):

:::{math}
:label:

\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\biggr|_{x=x_0} = \frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}}\biggr|_{y=y_0} = \frac{\partial{\mathbf{\tilde{V}}}}{\partial{z}}\biggr|_{z=z_0} = 0
:::

We are interested in knowing if the spacecraft at point $L_i$ undergoing some small deviation ($\delta\mathbf{r}$) from its initial state, will it stay in stable equilibrium?

:::{math}
:label: small_deviation
\begin{bmatrix} 
    x_0 \\ y_0 \\ z_0 \\
\end{bmatrix}
\rightarrow
\begin{bmatrix} 
    x_0 + \delta x \\ y_0 + \delta y \\ z_0 + \delta z \\
\end{bmatrix}
:::

The derivative of this deviated state becomes:

:::{math}
\begin{bmatrix} 
    \dot{x} \\ 
    \dot{y} \\
    \dot{z} \\
\end{bmatrix}
\rightarrow
\begin{bmatrix} 
    \delta\dot{x} \\ 
    \delta\dot{y} \\ 
    \delta\dot{z} \\
\end{bmatrix}
:::
 
and 

:::{math}
\begin{bmatrix} 
    \ddot{x} \\ 
    \ddot{y} \\
    \ddot{z} \\
\end{bmatrix}
\rightarrow
\begin{bmatrix} 
    \delta\ddot{x} \\ 
    \delta\ddot{y} \\ 
    \delta\ddot{z} \\
\end{bmatrix}
:::

Plug this is into the equations of motion for the [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem) {eq}`cr3bp_eom_norm_simp` to get:

:::{math}
:label: deviated_eom
\begin{align*}
\delta\ddot{x} - 2 \delta \dot{y} &= \frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\biggr|_{(x_0+\delta x, y_0 + \delta y, z_0 + \delta z)} \\
\delta\ddot{y} + 2 \delta \dot{x} &= \frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}}\biggr|_{(x_0+\delta x, y_0 + \delta y, z_0 + \delta z)} \\
\delta\ddot{z}  &= \frac{\partial{\mathbf{\tilde{V}}}}{\partial{z}}\biggr|_{(x_0+\delta x, y_0 + \delta y, z_0 + \delta z)}
\end{align*}
:::

These new systems of equations are six-dimensional and depict how the deviated spacecraft changes relative to the equilibrium point $L_i$. 

Let's linearize Equations {eq}`deviated_eom` by expanding the right-hand partial terms and remove higher order terms. Take $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$ as an example. 

:::{math}
\begin{align*}
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\biggr|_{(x_0+\delta x, y_0 + \delta y, z_0 + \delta z)} &= \frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\biggr|_{0} + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x^2}}\biggr|_{0} \delta x  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{y}}\biggr|_{0} \delta y  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{z}}\biggr|_{0} \delta z + \dots \\
\end{align*}
:::

becomes

:::{math}
\begin{align*}
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\biggr|_{(x_0+\delta x, y_0 + \delta y, z_0 + \delta z)} &=  \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x^2}}\biggr|_{0} \delta x  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{y}}\biggr|_{0} \delta y  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{z}}\biggr|_{0} \delta z
\end{align*}
:::

Linearize the remaining partial potentials in a similar manner and substitute into Equation {eq}`deviated_eom` to get the linearized equations of motion for the deviated system:

:::{math}
:label: linearized_deviated_eom
\begin{align*}
\delta\ddot{x} - 2 \delta \dot{y} &= \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x^2}}\biggr|_{0} \delta x  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{y}}\biggr|_{0} \delta y  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{x}\partial{z}}\biggr|_{0} \delta z \\
\delta\ddot{y} + 2 \delta \dot{x} &= \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{y}\partial{x}}\biggr|_{0} \delta x  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{y^2}}\biggr|_{0} \delta y  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{y}\partial{z}}\biggr|_{0} \delta z \\
\delta\ddot{z}  &= \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{z}\partial{x}}\biggr|_{0} \delta x  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{z}\partial{y}}\biggr|_{0} \delta y  + \frac{\partial^2{\mathbf{\tilde{V}}}}{\partial{z^2}}\biggr|_{0} \delta z
\end{align*}
:::

To make things easier to work with rewrite {eq}`linearized_deviated_eom` in matrix form:

:::{math}
:label: linearized_deviated_eom_matrix
\begin{bmatrix} 
    \delta\ddot{x} \\ \delta\ddot{y} \\ \delta\ddot{z} 
\end{bmatrix}
- 2 
\begin{bmatrix} 
    0 & 1 & 0 \\
   -1 & 0 & 0 \\
    0 & 0 & 0 
\end{bmatrix}
\begin{bmatrix} 
    \delta\dot{x} \\ \delta\dot{y} \\ \delta\dot{z} 
\end{bmatrix}
= 
\mathbf{\tilde{V}}_{\mathbf{rr}}
\begin{bmatrix} 
    \delta x \\ \delta y \\ \delta z
\end{bmatrix}
:::

where the potential matrix is defined as:

:::{math}
:label: vrr_matrix
\mathbf{\tilde{V}}_{\mathbf{rr}} =
\begin{bmatrix} 
    {\tilde{V}}_{xx} & {\tilde{V}}_{xy} & {\tilde{V}}_{xz} \\
    {\tilde{V}}_{yx} & {\tilde{V}}_{yy} & {\tilde{V}}_{yz} \\
    {\tilde{V}}_{zx} & {\tilde{V}}_{zy} & {\tilde{V}}_{zz}  
\end{bmatrix}
:::

Matrix {eq}`vrr_matrix` is a symmetric matrix and the partial notation is defined as:

:::{math}
\tilde{V}_{ij} = \frac{\partial{\tilde{V}}}{\partial{x}\partial{y}}
:::

Altogether, Equation {eq}`linearized_deviated_eom_matrix` is the linearized equations of motion for a spacecraft perturbed to a deviated state.

TODO: Consider writing partial derivates of Vrr slide 11 somewhere. Maybe as an appendix and point to it. 3 diagonal terms and 3 off-diagonal terms

## Stability of Co-Linear Lagrange Points

Now consider the [co-linear equilibrium points](#co-linear-lagrange-points) $L_{1-3}$. Having properties:  

:::{math}

\begin{align*}
y = z &= 0 \\
r_1 &= |x+\mu| \\ 
r_2 &= |x-1+\mu|
\end{align*}
:::

Substitute the form of $r_1$ and $r_2$ into matrix $\mathbf{\tilde{V}}_\mathbf{rr}$ {eq}`vrr_matrix` and simplify the partial derivative matrix.

:::{math}
:label:
\begin{align*}
\tilde{V}_{xx} &= 1 + \frac{2\left( 1 - \mu \right)}{|x+\mu|^3} + \frac{2\mu}{|x+\mu-1|^3} \\ 
\tilde{V}_{yy} &= 1 - \frac{\left( 1 - \mu \right)}{|x+\mu|^3} + \frac{\mu}{|x+\mu-1|^3}  \\ 
\tilde{V}_{zz} &= - \left[ \frac{\left( 1 - \mu \right)}{|x+\mu|^3} + \frac{\mu}{|x+\mu-1|^3} \right]  \\ 
\tilde{V}_{xy} = \tilde{V}_{xz} = \tilde{V}_{yz} &= 0
\end{align*}
:::

in matrix form:

:::{math}
:label:
\mathbf{\tilde{V}}_{\mathbf{rr}} =
\begin{bmatrix} 
    \mathbf{\tilde{V}}_{xx} & 0 & 0 \\
    0 & \mathbf{\tilde{V}}_{yy} & 0 \\
    0 & 0 & \mathbf{\tilde{V}}_{zz}  
\end{bmatrix}
:::

The signs for the non-zero terms will be important later. By inspection we determine $\tilde{V}_{xx} > 0 $ because we assumed $\mu < \frac{1}{2}$ for the [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem). Similarly, $\tilde{V}_{zz} < 0$ as both terms are positive and then multiplied by a negative values. For $\tilde{V}_{yy}$ it is not intuitive if the expression is positive or negative. It mostly depends on the dominating effect of either the second or third term.

Substitute into and reduce matrix {eq}`linearized_deviated_eom_matrix` to further analyze the stability of our co-linear equilibrium points. 


:::{math}
:label: stability_eom_matrix_L1-L3
\begin{bmatrix} 
    \delta\ddot{x} \\ \delta\ddot{y} \\ \delta\ddot{z} 
\end{bmatrix}
- 2 
\begin{bmatrix} 
    0 & 1 & 0 \\
   -1 & 0 & 0 \\
    0 & 0 & 0 
\end{bmatrix}
\begin{bmatrix} 
    \delta\dot{x} \\ \delta\dot{y} \\ \delta\dot{z} 
\end{bmatrix}
= 
\begin{bmatrix} 
    \mathbf{\tilde{V}}_{xx} \delta x & 0 & 0 \\
    0 & \mathbf{\tilde{V}}_{yy} \delta y & 0 \\
    0 & 0 & \mathbf{\tilde{V}}_{zz} \delta z
\end{bmatrix}
:::

Note that the z-component decouples from x and y:

:::{math}
:label: z_shm_eq
\delta\ddot{z} = \mathbf{\tilde{V}}_{zz} \delta z
:::

given that $\tilde{V}_{zz} < 0$ this has the form of a [harmonic differential equation](https://en.wikipedia.org/wiki/Harmonic_oscillator) with a well-known solution.

The general solution for differential equation {eq}`z_shm_eq` can be written as:

:::{math}
:label: delta_z_L1-L3
\delta z = A e^{\lambda t}
:::

Computing eigenvalues gives:

:::{math}
(\lambda^2 - \tilde{V}_{zz})A = 0
:::

:::{math}
:label:
\lambda = \pm \sqrt{\tilde{V}_{zz}} = \pm i \sqrt{|\tilde{V}_{zz}|}
:::

This gives a sinusoidal solution to {eq}`delta_z_L1-L3`


:::{math}

\delta z(t) = C_1 \cos{\omega t} + C_2 \sin{\omega t}

:::

where $\omega$ is the characteristic frequency; $\omega =  \sqrt{|\tilde{V}_{zz}|}$. 

By assuming the initial state $\delta z (0) = \delta z_0$ and $\delta \dot{z} (0) = \delta \dot{z}_0$ then we can write down the final solution to $\delta z(t)$ {eq}`delta_z_L1-L3` which shows it simply oscillates making the z-component of the deviated spacecraft a **stable** component.  

Now consider the x- and y-components of {eq}`stability_eom_matrix_L1-L3` 



:::{math}
:label: 
\begin{bmatrix} 
    \delta\ddot{x} \\ \delta\ddot{y} 
\end{bmatrix}
- 2 
\begin{bmatrix} 
    0 & 1  \\
   -1 & 0  \\
\end{bmatrix}
\begin{bmatrix} 
    \delta\dot{x} \\ \delta\dot{y} 
\end{bmatrix}
= 
\begin{bmatrix} 
    \mathbf{\tilde{V}}_{xx} \delta x & 0  \\
    0 & \mathbf{\tilde{V}}_{yy} \delta y  \\
\end{bmatrix}
= 
\begin{bmatrix} 
    0  \\
    0  \\
\end{bmatrix}
:::

Going directly to the solution of the eigenvalues yields:

:::{math}

\lambda^2 = -\frac{1}{2}\left( 4 - \tilde{V}_{xx} - \tilde{V}_{yy} \right) + \sqrt{{\left( 4 - \tilde{V}_{xx} - \tilde{V}_{yy} \right)}^2 - 4 \tilde{V}_{xx} \tilde{V}_{yy}}
:::

In this form the eigenvalues will be symmetric about real and imaginary axes. There are four possible roots, knowing $\tilde{V}_{xx} > 0 $, $\tilde{V}_{yy} < 0 $  and  $\tilde{V}_{xx}\tilde{V}_{yy} < 0 $  we can argue that there will be two real ($\pm \sigma $) and two imaginary ($\pm \omega $) roots. The imaginary roots pose no issue as the solution to {eq}`delta_z_L1-L3` will result in a sinusoidal function like what was proven to be stable for the z-component. The negative real root results in a solution that asymptotically converges to zero. Whereas a positive real root will cause the solution to diverge. 

For this reason the Lagrange Points $L_{1-3}$ are **unstable**. 


## Stability of Equilateral  Lagrange Points

Apply the same mathematical exercise from [Stability Of Co-Linear Lagrange Points](#stability-of-co-linear-lagrange-points) to [equilateral Lagrange Points](lagrange.md#equilateral-lagrange-points) $L_4$ and $L_5$. 

TODO: Consider working out this section as done in 589 HW 4 Problem 1

The eigenvalues have the form:

:::{math}
:label: L4_L5_lambdas
\lambda^2 = -\frac{1}{2} \pm \frac{1}{2} \sqrt{ 1 - 27\mu \left( 1 - \mu \right)}

:::

Giving two solutions:

:::{math}
\lambda^2 = -\omega^2_1, \omega^2_2
:::

or 

:::{math}
\lambda^2 = \alpha \pm i \beta
:::

Inspecting the square root term of {eq}`L4_L5_lambdas` the system is stable only if:

:::{math}
27\mu\left( 1 - \mu \right) < 1
:::

or 

:::{math}
\mu^2 - \mu + \frac{1}{27} > 0
:::

we know $\mu \lt \frac{1}{2}$ from the controlling condition thus the equilateral Lagrange Points are **stable** only if

:::{math}
:label:
\mu \lt \frac{1}{2}\left( 1 - \sqrt{\frac{23}{27}}\right) \approx ~ 0.03852
:::


There are some examples of stable and unstable $L_4$, $L_5$ points in our solar system. The Sun-Jupiter system has $\mu \approx 0.01$ making $L_4$ and $L_5$ stable equilibrium points. TODO: talk about Trojan system. 

Whereas the Pluto-Charon system $\mu \approx 0.10$ making $L_4$ and $L_5$ unstable equilibrium points TODO: find more info about this. 


## Non-Linear Stability 

The analysis shown in this section to determine the [stability of equilibrium points](#stability-of-equilibrium-points) is based off a linearized system {eq}`linearized_deviated_eom_matrix`. Linear stability does not necessarily imply non-linear stability. To apply this method to non-linear systems, it really depends on the characteristic time of the system. If a system is very non-linear the linearly stability analysis might only be good for a small propagation of time. To show that non-linear systems are stable or unstable a different technique must be applied. Often the [Lyapunov Stability](https://en.wikipedia.org/wiki/Lyapunov_stability) techniques is used to show when a system is non-linearly stable. 

## Python Example

There are a few examples to provide. From 589 HW3 and HW4 form 580 HW3


TODO: State L1-L3 are unstable and lie on saddle points, 