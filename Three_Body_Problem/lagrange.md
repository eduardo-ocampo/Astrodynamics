## Lagrange Points

The Lagrange Points are equilibrium points in a dynamic system. Here the dynamical system to analysis is the [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem). 

The potential for this system is define as Equation {eq}`cr3bp_V_norm`
 
:::{math}
:label:
\tilde{V}\left(x^*,y^*,z^*\right) = \frac{1}{2}\left( {x^*}^2 + {y^*}^2\right) + \frac{1-\mu}{r^*_1} + \frac{\mu}{r^*_2}
:::

where $r^*_1$ and $r^*_2$ are:

:::{math}
:label: postion_vectors_lagrange
\begin{align*}
r^*_1 &= \sqrt{\left( x^* + \mu \right)^2+{y^*}^2+{z^*}^2} \\
r^*_2 &= \sqrt{\left( x^* - 1 + \mu \right)^2+{y^*}^2+{z^*}^2}
\end{align*}
:::

```{warning}
The non-dimensional length term in section [Non-Dimensional Circular Restricted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem) is defined as:


:::{math} 
\mathbf{r}^* = \frac{\mathbf{r}}{r_s} = \frac{\mathbf{r}}{R}
:::

For this section on **Lagrange Points & Stability**, $^*$ notation will be dropped from parameters. It should be made clear that the discussion here applies to a **Non-Dimensional System**. 


```

To find the location of the Lagrange Points take the  partial derivative of $\mathbf{\tilde{V}}$ and find locations where motion is zero. Taking the partial of $\mathbf{\tilde{V}}$ yields:

:::{math}
:label: dv_dx_dy_dz
\begin{align*}
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}} &= x - \frac{(1-\mu)(x+\mu)}{{r_1}^3} - \frac{\mu(x+\mu-1)}{{r_2}^3} \\
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}} &= \left[ 1 -\frac{1-\mu}{{r_1}^3} - \frac{\mu}{{r_2}^3} \right]y \\
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{z}} &= -\left[ \frac{1-\mu}{{r_1}^3} + \frac{\mu}{{r_2}^3} \right]
\end{align*}
:::

From plotting the potential there are clues about how many and where the Lagrange Points lie.

TODO: Point or paste the 3d graph here

There are known to be 5 equilibrium points along the potential surface. $L_{1-3}$ lie co-linear along the axis joining primaries P1 and P2 and $L_{4-5}$ lies somewhere along the sides. 


TODO: Provide figure Topology of Lagrange Points in the rotating coordinate frame


### Co-Linear Lagrange Points

For the co-linear Lagrange Points $L_{1-3}$ the y- and z-coordinates are zero. This reduces their known position vectors {eq}`postion_vectors_lagrange` to depend only on their location along the x-axis relative to primary bodies.

:::{math}
:label: position_vectors_L1_L2_L3
\begin{align*}
r_1 &= |x+mu| \\ 
r_2 &= |x-1+mu|
\end{align*}
:::

Now substitute the relative position vectors {eq}`position_vectors_L1_L2_L3` into $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$. To compute the x-coordinates of the co-linear Lagrange Points we need to solve $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$ only since $y = 0$  and $z = 0$. 


:::{math}
:label: L1-L3_dv_dx

\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}} = x - \frac{(1-\mu)(x+\mu)}{|x+\mu|^3} - \frac{\mu(x+\mu-1)}{|x-1+\mu|^3} = 0

:::

By simply plotting $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$ it gives a quick and easy means of locating Lagrange Points $L_{1-3}$ for an arbituary $\mu$. 

Show plot for dv vs dx

Plot dv/dx to illustraute how the potential changes as a funciton of position. 

Figure 

Notice the function cross the x-axis precisely were the co-linear points lie. Then $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$ heads asymptotically towards infinity at primary P1 and similarly as the x-coordinates approaches P2.

To aid in solving for the roots $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}\big|_{x=0}$  it helps to approximate the co-linear equilibrium points. Expanding out {eq}`L1-L3_dv_dx` up to the first power yields:


:::{math}
\begin{align*}
x_1 &\approx 1 - \left(\frac{\mu}{3}\right)^{\frac{1}{3}} + \sigma\left(\mu^{\frac{2}{3}} \right) \\
x_2 &\approx 1 + \left(\frac{\mu}{3}\right)^{\frac{1}{3}} + \sigma\left(\mu^{\frac{2}{3}} \right) \\
x_3 &\approx -1 + \left(\frac{\sqrt(2)-1}{3}\right)\mu + \sigma\mu^2
\end{align*}
:::
     
By removing higher order terms, the equations reduce to:


:::{math}
:label: x1_x2_x3_approx
\begin{align*}
x_1 &\cong 1 - \left(\frac{\mu}{3}\right)^{\frac{1}{3}} \\
x_2 &\cong 1 + \left(\frac{\mu}{3}\right)^{\frac{1}{3}} \\
x_3 &\cong -1 + \left(\frac{\sqrt(2)-1}{3}\right)\mu 
\end{align*}
:::


There are many numerical solvers for getting the roots of Equation {eq}`L1-L3_dv_dx`. Approximating the co-linear Lagrange Points can be used to initialize a solver. An example is shown TODO ADD EXAMPLE. 

### Example

Here add homeworrk problem that asks us to craete plots of L1, L2, and L3 for vary mu

## Equilateral Lagrange Points

Solving for the position of Lagrange Points $L_{4}$ and $L_{5}$ are fairly straightforward compared to the [co-linear lagrange points](#co-linear-lagrange-points). $L_{4}$ and $L_{5}$ exist such that $y = 0$. Now check Equation {eq}`dv_dx_dy_dz` for $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}} = 0$.

:::{math}
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}} = \left[ 1 -\frac{1-\mu}{{r_1}^3} - \frac{\mu}{{r_2}^3} \right]y = 0
:::

The root for this function is trivial and results in the relative position vectors ${r_1}^3$ and ${r_2}^3$ to both be 1. Now applying this information to the definition of $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}}$ from Equation {eq}`dv_dx_dy_dz` becomes:


:::{math}
:label:
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}} = x - (1-\mu)(x+\mu) - \mu(x+\mu-1)
:::

Sovling for $\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}} = 0$ gives exactly:

:::{math}
:label:

x_{4,5} = \frac{1}{2} - \mu

:::

and using Equation {eq}`postion_vectors_lagrange` from the Three-Body definition of vectors ${r_1}$ and ${r_2}$ the y-coordinates for $L_{4-5}$ are:

:::{math}
:label:

y_4 = \frac{\sqrt{3}}{2}

y_5 = -\frac{\sqrt{3}}{2}

:::

Theses results demonstrate that Lagrange Points $L_{4}$ and $L_{5}$ lie equaliteraly with respect to primaries P1 and P2. As shown in FIGURE above.

We now have the exact results of for Lagrange Points $L_{4-5}$ whereas Lagrange Points $L_{1-3}$ need to be solved iteratively using a root-finding soler with the aid of the approximate $x_1$, $x_2$ and $x_3$ values {eq}`x1_x2_x3_approx`. 

For a non-restricted Three-Body Problem system ($\mu_3 \neq 0$), these 5 Lagrange Points still exist. However, the positions of the co-linear Lagrange Points are shifted. If the primaries P1 and P2 are on an elliptical orbit, analogue of the Lagrange Points do also exists. 


### Python Example


