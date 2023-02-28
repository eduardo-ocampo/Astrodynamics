## The Jacobi Constant

When dealing with the [Circular Restricuted Three-Body Problem](cr3bp.md) there exists a time-invariant integral of motion known as the Jacobian Integral of Motion. To get this integral of motion, multiple the Circular Restricuted Three-Body Problem equations of motion, Equation {eq}`cr3bp_eom_simp`, by the velocity vector:

:::{math}
:label: 

\dot{x}\left(\ddot{x} - 2n\dot{y}\right) = \dot{x}\left(\frac{\partial{V}}{\partial{x}}\right)

\dot{y}\left(\ddot{y} + 2n\dot{x}\right) = \dot{y}\left(\frac{\partial{V}}{\partial{y}}\right)

\dot{z}\left(\ddot{z} \right) = \dot{z}\left(\frac{\partial{V}}{\partial{z}}\right)

:::

:::{math}
:label: 

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

In other words, we can decouple the in-plane motion and out-of-plane motion. This system is call the Circular Planar Restricted Three-Body Problem (CPR3BP). In this case Equation {eq}`jacobi_constant_norm` becomes:

:::{math} 
:label: crp3bp_jacobi
\frac{1}{2}\left( {\dot{x}^*}^2 + {\dot{y}^*}^2\right) - \tilde{V}\left(x^*,y^*\right) = \tilde{J} = C
:::

A new constant ( C ) is used to denote the Circular Planar Restricted Three-Body Problem Jacobi constant. Looking at the first term in Equation {eq}`crp3bp_jacobi` it is certain to always be positive. Rearranging the Equation {eq}`crp3bp_jacobi` shows that $\tilde{V} + C \ge 0$. 

Knowing $\tilde{V}$ is always positive, if $C \gt 0$ then $\tilde{V} + C \ge 0$ is always satisfied. However, if $C \lt 0$ things get a bit interesting. What this says is that given a value of Jacobi constant, motion is not possible in the region of space when:

:::{math}
:label:
\tilde{V} + C \le 0
:::

In Astrodynamics this is sometimes refer to as the forbidden regions and it can relate to the zero-velocity curves. For the CRP3BP the zero-velocity surface is defined as:

:::{math}
:label:
\tilde{V}\left( x^*, y^*\right) + C = 0
:::

Below are plots of the forbidden region for the Earth-Moon Three-Body System at select Jacobi constants. Here the Lagrange Points are plotted for reference as they are relevant to the forbidden regions. More information about the Lagrange Points can be found here (TODO: SOURCE THIS).

TODO: Talk and add and example of having a constant Jacobi for different states
TODO: Start talking about forbbin regions, look at om.space and make plots

Plot A = -5.0
Plot B = -3.0
Plot C = L1
Plot D = L1 + a bit more
Plot E = L2?
Plot F = L3? 

Plot A at C = -5.0 is shown for reference. As C grows towards 0 notice how the forbidden region begins to get smaller in size. 

At Plot C notice the forbidden region between the Earth-Moon system to the right comes to a singularity which at Lagrange Point 1. 

Now by increasing C a bit more from Plot C to Plot D a direct path from the Earth to the Moon begins to appear (Low Energy Transfer). At a high level, Mission Design Engineers aim to change a spacecraft's velocity just enough so that a trajectory exists between the Earth and the Moon using very small energy. Here are some more references on [Low Energy Transfer](http://www.gg.caltech.edu/~mwl/publications/papers/lowEnergy.pdf) and [Free-Return Trajectory](https://en.wikipedia.org/wiki/Free-return_trajectory) as they relate to maneuvering to the Moon. 

As C continues to increase both L2 and L3 begin to open up. as shown in Plots XXXX, and as C gets closer to 0.0 the forbidden regions begins to disappear at singularity corresponding to the location of L4 and L5. 

Lastly, consider a non-planar system. The same analysis can be done to illustrate how the forbidden regions change in 3-dimenionsl space along the potential surfaces:

TODO: Add 3D Example of zero-velocty curves


TODO: Next section can be Jacobian Integral in inertial frame and then lead to Tisserand's Criterion