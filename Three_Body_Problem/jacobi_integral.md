# Integral of Motion

# Jacobi Integral

When dealing with the [Circular Restricuted Three-Body Problem](cr3bp.md) there exists a time-invariant integral of motion known as the Jacobian Integral of Motion. To get this integral of motion, multiple the Circular Restricuted Three-Body Problem equations of motion, Equation {eq}`cr3bp_eom_simp`, by the velocity vector:

:::{math}
:label: 

\dot{x}\left[\ddot{x} - 2n\dot{y}\right] = \dot{x}\left[\frac{\partial{V}}{\partial{x}}\right]

\dot{y}\left[\ddot{y} + 2n\dot{x}\right] = \dot{y}\left[\frac{\partial{V}}{\partial{y}}\right]

\dot{z}\left[\ddot{z} \right] = \dot{z}\left[\frac{\partial{V}}{\partial{z}}\right]

:::

:::{math}
:label: 

\dot{x}\ddot{x} + \dot{y}\ddot{y} + \dot{z}\ddot{z} = \frac{\partial{V}}{\partial{x}}\dot{x} + \frac{\partial{V}}{\partial{y}}\dot{y} + \frac{\partial{V}}{\partial{z}}\dot{z}

:::

and then integrate both ends

:::{math}
:label: 

\frac{1}{2} \frac{d}{dt} \left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) = \frac{d}{dt} V\left(x,y,z \right)

:::

:::{math}
:label: 

\frac{d}{dt} \left[ \frac{1}{2}\left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) - V \right] = 0
:::

This yields the constant **Jacobi Integral (J)**: 

:::{math}
:label: 

\frac{1}{2}\left( \dot{x}^2 + \dot{y}^2 + \dot{z}^2 \right) - V\left(x,y,z \right) = J 
:::


TODO: Start talking about forbbin regions, look at om.space and make plots

TODO: Next section can be Jacobian Integral in inertial frame and then lead to Tisserand's Criterion

