## The Two-Body Problem

The full two-body problem is the motion two bodies with finite masses that are attracted to each other according to Newton's Law of Gravitation. 

We are interested in their relative dynamics. The force of particle $P_1$ acting on particle $P_2$ in the inertial frame yields the following diagram: 

```{figure} ./images/two-body_image.png
:name: fig:Two-Body_Problem_Figure
:width: 75%
**Figure 1.1** Two-Body Problem.
```


Where $P_1$ has mass $m_1$ and $P_2$ has mass $m_2$, and we define the relative vector notation as:

:::{math}
\mathbf{r}_{ij} = \mathbf{r}_j - \mathbf{r}_i

\mathbf{r}_{12} = \mathbf{r}_2 - \mathbf{r}_1
:::

Derived from Newton's Law of Gravitation, the Equation of Motion for the Two-Body Problem is:

:::{math}
:label: eq:Two_Body_EOM
\ddot{\mathbf{r}} = -G\frac{(m_1+m_2)}{r^3}\mathbf{r}
:::

where:

:::{math}
\mathbf{r} = \mathbf{r_{12}} = \mathbf{r_2} - \mathbf{r_1}
:::

Each particle has a State Vector made up of its position and velocity:

:::{math}
:label: eq:state_vector
\mathbf{\bar{x}} = \begin{bmatrix} 
    \mathbf{x} \\ \mathbf{y} \\ \mathbf{z} \\
    \mathbf{\dot{x}} \\ \mathbf{\dot{y}} \\ \mathbf{\dot{z}}
\end{bmatrix}
:::

To solve the for the Two-Body Problem we require 12 equations of motion due to 2 state vectors. However, if we assume one of the particles does not have mass or its mass is negligible  (Earth-satellite system) the system will require only 6 equations of motion. Thus 6 integrals of motion are needed to solve the relative dynamics of the Two-Body Problem.  

These 6 integrals of motion have become to be known as the [Classical Orbital Elements](Classical_Orbit_Elements.md). An integral of motion is a combination of positions, velocities, and times that remain constant under the motion governed by the equations of motion.


```{note}
The term $G(m_1+m_2)$ comes up quite often in our Equations of Motion that is convenient to define it as the Gravitation Constant ($\mu$)

:::{math}
\mu = G(m_1+m_2)
:::
```