# Introduction

Consider the simplest spacecraft trajectory maneuver which involves getting from one circular orbit to another circular orbit. Assuming we have two impulse burns, the Hohmann Transfer TODO LINK SECTION is the optimal solution for this maneuver. However, be mindful that that what is considered an **optimal solution** is influenced heavy by the system requirements. In some case the Hohmann Transfer is not the most optimal approach because technically a solver might converge to a solution that thrusts with two large impulses. Sometimes we need to throw in realism into the problem statement such as getting to a target body with some $\Delta\mathbf{V}$ budget and time of flight (TOF). Now suppose the possibility of more than two impulse burns during the maneuver. The Hohmann Transfer may also not be suited as the optimal solution if the problem requires minimizing total $\Delta\mathbf{V}$. In some cases, the Bi-elliptic Transfer TODO LINK is more optimal if one is trying to minimize impulse burn at the cost of more travel time. 
 
Things get more complicated as soon we consider trade-offs between $\Delta\mathbf{V}$, TOF, and spacecraft attitude control. The Hohmann Transfer or Bi-elliptic Transfer are not going to be the most optimal solution to meet all the system requirements. Instead, one can design a low-thrust trajectory maneuver. However, the control solution cannot result in back and forth between directions despite that being the optimal solution. So practically we might constraint the control to change at a certain rate or maintain some attitude direction such as keeping solar panels pointed towards the sun direction within some tolerance. With that said, in practice there might exist a more optimal control solution but sometimes one must face the physical limitation of the spacecraft design. This section will provide the reader with the tools and knowledge for setting up an **Optimal Control Problem** for optimizing spacecraft trajectories.

## Defining the Optimal Control Problem Statement:

Consider a trajectory from point A to point B, i.e Earth to Mars. It might be of importance to solve for an optimal trajectory using **Optimal Control Theory** ([Additional Ref.](https://homes.cs.washington.edu/~todorov/courses/amath579/Todorov_chapter.pdf) by E. Todorov). The approach is to design a control law that satisfy minimizing a cost function. This could be minimizing a flight parameter such as $\Delta\mathbf{V}$, TOF, spacecraft attitude control, fuel usage, or a combination of other parameters.

### Dynamics

Consider $\frac{d \mathbf{x}}{dt}$ which is a function of state $\mathbf{x}$, thrust maneuver or control law $\mathbf{u}$, and time. 

:::{math}
:label:
\frac{d \mathbf{x}}{dt} = \mathbf{f}\left( \mathbf{x}, \mathbf{u}, t \right)
:::

with initial bound:

:::{math}
\mathbf{x}\left(t_0 \right) = \mathbf{x}_0
:::

The solution set ($\mathbf{x}$,$\mathbf{u}$) to the **Optimal Control Problem** exists for time $t_0 \leq t \leq t_f$ and is admissible if ($\mathbf{x}$,$\mathbf{u}$) satisfies all the constraints. 

### Constraints

The final constraints ($\Psi$) are defined at time $t_f$ such that it is zero. 

:::{math}
:label: psi_constraint
\Psi\left( \mathbf{x}\left( t_f \right), t_f \right) = 0
:::

There are numerous applications using this form of the constraints which could be a function of position, velocity, thrust angle, etc. and require the final state to match that of the final conditions for $\Psi$ to be zero.  For example, rendezvousing at a target body such as the International Space Station requires the final non-zero position and velocity to match that of the ISS at time $t_f$. Flying by a body such as an asteroid may simply require only the position to match that of the asteroid at $t_f$. Wanting to land on a body such as Mars may require the thrust direction to line up so that the spacecraft is reasonably allowed to land safely on the body's surface. Regardless of the problem statement the final constraints must be satisfied at the final time such that: 

:::{math}
:label:
\mathbf{x}\left(t_f\right) - \mathbf{x}_{target} = 0
:::

### The Cost Function

The core of **Optimal Control Theory** is wanting to minimize an objective in the form of a cost function $J$ which is a function of the state $\mathbf{x}$ and control $\mathbf{u}$. 

The general form of the cost function is:

:::{math}
:label: cost_function_explicit
J \left(\mathbf{x},\mathbf{u} \right) = \Phi \left( \mathbf{x}\left( t_f \right), t_f \right) + 
\int_{t_0}^{t_f} L\left(\mathbf{x}\left(t\right),\mathbf{u}\left(t\right),t\right) dt
:::

The set ($\mathbf{x}^*$, $\mathbf{u}^*$) is optimal if $J\left( \mathbf{x}^*, \mathbf{u}^* \right) \leq J\left(\mathbf{x}, \mathbf{u} \right)$. This is known as the **Minimum J Value** solution. 

The terms $\Phi$ and $L$ are called the **terminal conditions** and the **running cost** respectively. The running cost term is a function of state and control integrated over some time. For example, if a continuous thrust maneuver is applied it is an integral over some time period accounted for with $\mathbf{u}\left(t_f\right)$. This is a form that is best used to minimize a parameter directly related to the control such as minimizing fuel consumption over some time period $T$. 

For the rest of this section consider a problem that is **not** an explicit function of time:

:::{math}
:label:
\frac{d \mathbf{x}}{dt} = \mathbf{f}\left( \mathbf{x}, \mathbf{u} \right)
:::

The Cost Function {eq}`cost_function_explicit` is then: 

:::{math}
:label: cost_function_this_section
J \left(\mathbf{x},\mathbf{u} \right) = \Phi \left( \mathbf{x}\left( t_f \right) \right) + 
\int_{t_0}^{t_f} L\left(\mathbf{x}\left(t\right),\mathbf{u}\left(t\right)\right) dt
:::

## The Hamiltonian

To define the Hamiltonian, consider a local optimal solution ($\mathbf{x}^*$, $\mathbf{u}^*$) and define $\mathbf{x}$ and $\mathbf{u}$ such that $J\left( \mathbf{x}^*, \mathbf{u}^* \right) \leq J\left( \mathbf{x},\mathbf{u} \right)$  :

:::{math}
\begin{align*}
\mathbf{x} &= \mathbf{x}^* + t \delta \mathbf{x} \\
\mathbf{u} &= \mathbf{u}^* + t \delta \mathbf{u}
\end{align*}
:::

Consider a valid and alternative form of the cost function {eq}`cost_function_this_section`:

:::{math}
J \left(\mathbf{x},\mathbf{u} \right) = \Phi \left( \mathbf{x}\left( t_f \right) \right) + K^T  \Psi\left( \mathbf{x}\left( t_f \right) \right) + 
\int_{t_0}^{t_f}\left[ L\left(\mathbf{x}\left(t\right),\mathbf{u}\left(t\right)\right)  
+ \mathbf{\lambda}^T\left[ f\left(\mathbf{x},\mathbf{u} \right) - \frac{d\mathbf{x}}{dt} \right]
\right]dt
:::

Where $K$ and $\mathbf{\lambda}$ are multipliers. Recall that $\Psi = 0 $ and $f\left(\mathbf{x},\mathbf{u} \right) - \frac{d\mathbf{x}}{dt} = 0$

If small change $\delta\mathbf{x}$ and $\delta\mathbf{u}$ satisfy the constraints, then this implies that:

:::{math}
\frac{dJ}{dt} \left( \mathbf{x}^* + \delta\mathbf{x}, \mathbf{u}^* + \delta\mathbf{u} \right) \biggr|_{t=0} = 0
:::

Expanding out $\frac{dJ}{dt}\biggr|_{t=0}$ gives:

:::{math}
:label: dj_dt_hammy
\left[\Phi_{u} \left(\mathbf{x}^*\left( t_f \right) \right)\right]^T \delta\mathbf{x}\left( t_f \right) + 
K^T \Psi_x\left(\mathbf{x}^*\left( t_f \right)\right) 
+ \int_{t_0}^{t_f} \left[ 
\left[L_x\left( \mathbf{x}^*, \mathbf{u}^* \right)\right]^T \delta \mathbf{x} + 
\left[L_u\left( \mathbf{x}^*, \mathbf{u}^* \right)\right]^T \delta \mathbf{u} + 
\mathbf{\lambda}^T \left[ 
f_x\left(\mathbf{x}^*,\mathbf{u}^* \right)\delta\mathbf{x} + 
f_u\left(\mathbf{x}^*,\mathbf{u}^* \right)\delta\mathbf{u} - 
\frac{d\left(\delta\mathbf{x} \right)}{dt}
\right]
\right] dt = 0
:::

```{note}
Partial derivatives will sometimes be referred to using a subscript notation. For example:

:::{math}
\frac{\partial{\Phi}}{\partial{\mathbf{x}}} = \Phi_x
:::

```

From Expression {eq}`dj_dt_hammy` the following important relationships arise. For more information on the intermediate steps resulting in these relationships see [Hamiltonian (control theory)](https://en.wikipedia.org/wiki/Hamiltonian_(control_theory)). A summary of the derived Hamiltonian relationship Equations {eq}`hammy` - {eq}`lambda_phi_psi` are presented in the [Summary section](#summary)

The Hamiltonian Function is defined as:

:::{math}
:label: hammy
\mathbf{H}\left(\mathbf{x},\mathbf{\lambda},\mathbf{u} \right) = \mathbf{\lambda}^T\mathbf{f}\left(\mathbf{x},\mathbf{u} \right) + \mathbf{L}\left(\mathbf{x},\mathbf{u} \right)
:::

Note that the $\mathbf{f}$ term is the system dynamics and $\mathbf{L}$ is the integrate of the cost function. 

In order to solve for $\frac{dJ}{dt}$ in Equation {eq}`dj_dt_hammy` [lagrange multipliers](https://tutorial.math.lamar.edu/classes/calciii/lagrangemultipliers.aspx) $\mathbf{\lambda}$ are defined such that:

:::{math}
:label: expand_dl_dt
\frac{d\mathbf{\lambda}}{dt} = - \mathbf{\lambda}\left[ f_x\left(\mathbf{x}^*,\mathbf{u}^*\right) \right] - L_x\left( \mathbf{x}^*, \mathbf{u}^*\right)
:::

which in terms of the Hamiltonian {eq}`expand_dl_dt` is best written as:

:::{math}
:label: dlambda_dt
\frac{d\mathbf{\lambda}{\left(t\right)}}{dt} = - \frac{\partial{\mathbf{H}\left(\mathbf{x}^*(t),\mathbf{\lambda}(t),\mathbf{u}^*(t) \right)}}{\partial{\mathbf{x}}}
:::

:::{math}
\frac{d\mathbf{\lambda}{\left(t\right)}}{dt} = - \mathbf{H}_\mathbf{x}
:::

From Expression {eq}`dj_dt_hammy` we can define what is referred to as the **Necessary Condition** by knowing that $\int \delta\mathbf{u}dt = 0$ 

:::{math}
:label: expand_necessary_condition
L_u \left( \mathbf{x}^*,\mathbf{u}^* \right) + 
\left[f_x \left( \mathbf{x}^*, \mathbf{u}^* \right)\right] \mathbf{\lambda} = 0
:::

or in terms of the Hamiltonian the Necessary Condition is:

:::{math}
:label: 
\frac{\partial{\mathbf{H}\left(\mathbf{x}^*(t),\mathbf{\lambda}(t),\mathbf{u}^*(t) \right)}}{\partial{\mathbf{u}}} = 0
:::

:::{math}
\mathbf{H}_\mathbf{u} = 0
:::

And finally, from knowing $\delta\mathbf{x}t_0 = 0$ Expression {eq}`dj_dt_hammy` results in a useful relationship between the lagrange multiplier and constraint function $\Psi$:

:::{math}
:label: lambda_phi_psi
\mathbf{\lambda}\left( t_f \right) - \Phi_x\left( \mathbf{x}^*\left( t_f \right) \right) = \sum_{i=1}^{m} K_i \mathbf{\Psi_i}_x\left(\mathbf{x}^*\left(t_f \right) \right)
:::

## Summary

In summary an **Optimal Control Problem** is really no more than setting up a cost function {eq}`cost_function_explicit` defining the system dynamics and finding a solution ($\mathbf{x}^*$,$\mathbf{u}^*$) that satisfies the system constraints and the Hamiltonian relationships:

```{admonition} Summary of the Hamiltonian as used to solve an Optimal Control Problem for a dynamical system
The Hamiltonian is defined as:

:::{math}
\mathbf{H}\left(\mathbf{x},\mathbf{\lambda},\mathbf{u} \right) = \mathbf{\lambda}^T\mathbf{f}\left(\mathbf{x},\mathbf{u} \right) + \mathbf{L}\left(\mathbf{x},\mathbf{u} \right)
:::

for dynamical system $\mathbf{x}$, and $\mathbf{u}$.

:::{math}
\frac{d \mathbf{x}}{dt} = \mathbf{f}\left( \mathbf{x}, \mathbf{u} \right)
:::

subject to final constraints 

:::{math}
\Psi\left( \mathbf{x}\left( t_f \right) \right) = 0
:::

Let $\mathbf{x}^*$, $\mathbf{u}^*$, $t_0 \leq t \leq t_f$ be **locally optimal**, then there is $\mathbf{\lambda} (t)$ along  $t_0 \leq t \leq t_f$ such that:

:::{math}
\frac{d \mathbf{x}}{dt}  = \mathbf{H}_{\mathbf{\lambda}}
:::

:::{math}
\frac{d \mathbf{\lambda}}{dt}  = -\mathbf{H}_{\mathbf{x}}
:::

:::{math}
\mathbf{\lambda}\left( t_f \right) - \Phi_x\left( \mathbf{x}^*\left( t_f \right) \right) = \sum_{i=1}^{m} K_i \mathbf{\Psi_i}_x\left(\mathbf{x}^*\left(t_f \right) \right)
:::

:::{math}
\mathbf{H}_{\mathbf{u}} = 0
:::

Note this is not a theorem because multiplier functions may not necessarily exist!
```

### Local vs Global Minimum

The work at hand in this section deals with a locally optimal solution set ($\mathbf{x}^*$, $\mathbf{u}^*$) which does not guarantee to be the global minimum solution. In reality finding a global minimum for this type of problem setup is difficult. There are certain class of problems were a solution is most likely to exist such as a [Convex Optimization Problem](https://en.wikipedia.org/wiki/Convex_optimization) and [Convex Quadratic Programming](https://www.geometrictools.com/Documentation/ConvexQuadraticProgramming.pdf). Often times defining a trajectory problem as a Convex Optimization Problem requires making simplifying assumptions which could jeopardize the fidelity of the solution set. Here is some more information on [Convex Optimization](http://underactuated.mit.edu/trajopt.html) and a deeper dive into [trajectory optimization and guidance design](https://docs.lib.purdue.edu/cgi/viewcontent.cgi?article=3316&context=open_access_dissertations) by Zhenbo Wang of Purdue University. 

In practice you'll have to rely on numerical methods to optimize the problem. Section on [Zermelo's Problem](zermelos_problem.md) provides an example of solving a classic optimal control problem using numerical methods in Python. 

## Special Cases of the Optimal Control Problem

There are generally three different forms of the Optimal Control Problem. 

### 1. Bolza Problem

An **Optimal Control Problem** in which the cost is given by Equation {eq}`cost_function_explicit` and a combination of the terminal cost and running cost are minimized. 

:::{math}
J \left(\mathbf{x},\mathbf{u} \right) = \Phi \left( \mathbf{x}\left( t_f \right) \right) + 
\int_{t_0}^{t_f} L\left(\mathbf{x}\left(t\right),\mathbf{u}\left(t\right)\right) dt
:::
### 2. Mayer Problem

Based on the terminal constraint only ($\mathbf{L}=0$). Useful if only the final bounds of the system are of importance and it does not matter how to get there. 

:::{math}
J \left(\mathbf{x},\mathbf{u} \right) = \Phi \left( \mathbf{x}\left( t_f \right) \right)
:::

### 3. Lagrange Problem

Typically used to minimize the running cost $\mathbf{L}$ integrate over some time domain.

:::{math}
J \left(\mathbf{x},\mathbf{u} \right) = \int_{t_0}^{t_f} L\left(\mathbf{x}\left(t\right),\mathbf{u}\left(t\right)\right) dt
:::

For example, consider a trajectory design for getting to the Moon. Suppose you are trying to get to the Moon by minimizing the fuel consumption then the **Lagrange Problem** formulation will be more applicable. If the final position of the landing site or Moon's position is of most importance, then the **Mayer Problem** formulation is best to use. 
