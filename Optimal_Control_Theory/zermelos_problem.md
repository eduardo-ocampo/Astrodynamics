
# Zermelo's Problem

TODO: Update Figure Numbers X.X

Consider a boat crossing a river as shown in **Figure X.1**. 

```{figure} ./images/zermelos_diagram.png
:name: fig:zermelos_problem
:width: 75%
**Figure X.1** Zermelo's Boat Problem
```


The boat can change direction $\mathbf{\delta}$ by using sails while undergoing a constant velocity $\mathbf{V}$. The river has a current $\mathbf{U}\left(x,y \right)$ which adds to the boat's relative velocity. The objective is to have the boat cross from the left hand side ($x_0$) to the right hand side while steering the boat is such a way as to maximize the distance along the y-axis for a "fixed time" $t_f$.

Typically the cost function is used to minimize an objective. To maximize the cost function, we will apply a negative scale to our objective. So by minimizing $-y(t_f)$ we will be maximizing $y(t_f)$. For this example we will be applying the [Mayer Problem](introduction.md#special-cases-of-the-optimal-control-problem) due not having a control term $L(\mathbf{x},\mathbf{u})$.

## Zermelo's Problem Definition

State
:::{math}
\begin{bmatrix}
x \\
y 
\end{bmatrix}
:::

Control 
:::{math}
\delta
:::

**Objective**

:::{math}
:label:
\begin{align*}
J &= -y\left(t_f\right) \\
\Phi &= -y\left(t_f\right)
\end{align*}
:::

**Final constraint**

:::{math}
:label:
\Psi(x_f,y_f) = 0
:::

### Problem Dynamics

The dynamics of our system can be broken down to the water current and boat dynamics:

Current
:::{math}
:label:
\begin{align*}
\dot{x}_{c} &= U_x\left(x,y\right) \\
\dot{y}_{c} &= U_y\left(x,y\right)
\end{align*}
:::

Boat
:::{math}
:label:
\begin{align*}
\dot{x}_{b} &= V\cos{\delta} \\
\dot{y}_{b} &= V\sin{\delta}
\end{align*}
:::

**Combined effects on Boat**
:::{math}
:label: zermo_dynamics
\begin{align*}
\dot{x} &= V\cos{\delta} + U_x\left(x,y\right) \\
\dot{y} &= V\sin{\delta} + U_y\left(x,y\right)
\end{align*}
:::

### Problem Bounds

For the sake of simplicity let us assume the boat is instantaneously brought to constant velocity $\mathbf{V}$ at initial time $t_0$. 

**Initial State Condition**

:::{math}
:label: zerm_bounds
\begin{matrix}
x(0) = x_0 & v_x(0) = V_0\cos{\delta_0} \\
y(0) = y_0 & v_y(0) = V_0\sin{\delta_0} \\
\end{matrix}
:::

**Terminal Constraint**

The final constraints require only the distance travelled in the x-direction to match that of the width of the river ($X$) such that:

:::{math}
:label: zerm_constraint
\begin{align*}
\Psi\left(x\left(t_f\right),y\left(t_f\right)\right) &= 0 \\
x\left(t_f\right) - X &= 0
\end{align*}
:::

## Application of the Optimal Control Theory

Begin by using the summarized steps for solving an [Optimal Control Problem using the Hamiltonian](introduction.md#summary) from the [Introduction](introduction.md) section. 


```{admonition} An import result for the Hamiltonian

By definition

:::{math}
\frac{d \mathbf{x}}{dt}  = \mathbf{H}_{\mathbf{\lambda}}
:::

By choice

:::{math}
\frac{d \mathbf{\lambda}}{dt}  = -\mathbf{H}_{\mathbf{x}}
:::

By necessity

:::{math}
\frac{\partial{\mathbf{H}}}{\partial{\mathbf{u}}} = 0
:::

If $\mathbf{H}$ is not explicity a function of time, then

:::{math}
\begin{align*}
\dot{\mathbf{H}} &= 0 \\
\mathbf{H} &= \text{constant}
\end{align*}
:::

```

The Hamiltonian is:

:::{math}
\mathbf{H}\left(\mathbf{x},\mathbf{\lambda},\mathbf{u} \right) = \mathbf{\lambda}^T\mathbf{f}\left(\mathbf{x},\mathbf{u} \right) + \mathbf{L}\left(\mathbf{x},\mathbf{u} \right)
:::

Where,

:::{math}
:label:
\mathbf{\lambda}(t) = 
\begin{bmatrix}
\lambda_1(t) \\
\lambda_2(t)
\end{bmatrix}
:::

In this example $\mathbf{L}\left(\mathbf{x},\mathbf{u} \right) = 0$. So the Hamiltonian becomes somewhat simpler

:::{math}
:label: zerm_hammy
\mathbf{H} = \lambda_1 \left(V\cos{\delta} + U_x \right) + \lambda_2 \left(V\sin{\delta} + U_y \right)
:::

Next, obtain the differential equations for costates $\lambda(t)$ by evaluating

:::{math}
\dot{\mathbf{\lambda}}(t) = -\frac{\partial{\mathbf{H}}}{\partial{\mathbf{x}}}
:::

In terms of its components:

:::{math}
\begin{align*}
\dot{\lambda}_1 &= -H_x\\
\dot{\lambda}_2 &= -H_y
\end{align*}
:::


:::{math}
:label: zerm_dlambda_dt
\begin{align*}
\dot{\lambda}_1 &= -\lambda_1\cdot\left(U_x\right)_x - \lambda_2\cdot\left(U_y\right)_x \\
\dot{\lambda}_2 &= -\lambda_1\cdot\left(U_x\right)_y - \lambda_2\cdot\left(U_y\right)_y
\end{align*}
:::

### Control

Get the control by evaluating $\mathbf{H}_u = 0$. The only control term of relevance is steering angle $\delta$.

:::{math}
:label: dh_ddelta
\frac{\partial{H}}{\partial{\delta}} = -\lambda_1 V \sin{\delta} + \lambda_2 V \cos{\delta} = 0
:::

By solving {eq}`dh_ddelta` we get:

:::{math}
:label: control_tan
\tan{\delta} = \frac{\pm\lambda_2}{\pm\lambda_1}
:::

Similarly

:::{math}
:label: control_cos_sin
\begin{align*}
\cos{\delta} &= \pm \frac{\lambda_1}{\sqrt{\lambda^2_1+\lambda^2_2}} \\ 
\sin{\delta} &= \pm \frac{\lambda_2}{\sqrt{\lambda^2_1+\lambda^2_2}}
\end{align*}
:::

Let us consider a positive defeinte of our Optimal Control Problem. The condition for this in terms of our control law {eq}`dh_ddelta` is such that:

:::{math}
:label: dh2_du2
\frac{{\partial^2{H}}}{\partial{{\delta^2}}} \ge 0
:::

:::{math}
\frac{{\partial^2{H}}}{\partial{{\delta^2}}} &= -\lambda_1 V \cos{\delta} - \lambda_2 V \sin{\delta} \ge 0 \\
:::

This will constraint Equations {eq}`dh_ddelta` - {eq}`control_cos_sin` giving clear indication of the direction of steering angle $\delta$ and costates:

:::{math}
:label: zerm_control_reduced
\begin{align*}
\tan{\delta} &= \frac{-\lambda_2}{-\lambda_1} \\
\cos{\delta} &= -\frac{\lambda_1}{\sqrt{\lambda^2_1+\lambda^2_2}} \\ 
\sin{\delta} &= -\frac{\lambda_2}{\sqrt{\lambda^2_1+\lambda^2_2}}
\end{align*}
:::

### Terminal Constraints & Bounds

Now since we have more than one constraint based on the terminal condition. we can determine the bound conditions for $\lambda(t)$ by evaluating Equation {eq}`lambda_phi_psi` from  section [Introduction-The Hamiltonian](introduction.md#the-hamiltonian):


:::{math}
:label: zerm_bound_conditions
\mathbf{\lambda}\left( t_f \right) = \Phi_{x\left(t_f\right)} + \sum_{i=1}^{m} K_i \mathbf{\Psi_i}_{x\left(t_f\right)}
:::

becomes

:::{math}
:label: zerm_bound_conditions2
\begin{bmatrix}
\lambda_1\left( t_f \right) \\
\lambda_2\left( t_f \right)
\end{bmatrix} =
\begin{bmatrix}
0 \\
-1
\end{bmatrix}
+
K_1
\begin{bmatrix}
1 \\
0
\end{bmatrix}
:::

Which gives:

:::{math}
\begin{align*}
\lambda_1\left(t_f\right) &= K_1 \\
\lambda_2\left(t_f\right) &= -1 
\end{align*}
:::

Note that if there is no condition for $\lambda\left(t_f \right)$ than it is considered a free variable. We now can refine [Problem Bounds](#problem-bounds) {eq}`zerm_bounds` with a total of 4 boundary conditions.

:::{math}
:label: zerm_bounds_updated
\begin{matrix}
 x\left(0\right) = x_0 & x\left(t_f\right) = X \\  
 y\left(0\right) = y_0 & \lambda_2\left(t_f\right) = -1 \\  
\end{matrix}
:::

This defines the complete **Zermelo's Optimal Control Problem** using the Mayer approach The next section we dive into solving the problem using numerical analysis in Python.

## Numerical River Example

```{figure} ./images/example_river_current.png
:name: fig:example_river_current
:width: 100%
**Figure X.2** Example River Current
```

Consider crossing a river that has no current in the x-direction but only in the y-direction ($\frac{m}{s}$). As shown in **Figure X.2** for a river of width of 100 meters.

:::{math}
:label: zerm_case2_current
\begin{align*}
U_x &= 0 \\
U_y &= 2 \sin{\frac{\pi x}{100}}
\end{align*}
:::

Assume the following initial conditions for the boat at time $t_0$ in meters and seconds. 

:::{math}
:label: zerm_case2_boat
\begin{matrix}
 x\left(0\right) = 0 & V_{constant} = 2 \\
 y\left(0\right) = 0 & \delta\left(0\right) = free \\
\end{matrix}
:::

And final conditions:

:::{math}
:label: zerm_case2_bounds
\begin{matrix}
 x\left(t_f\right) = 100 m & t_f = 100s \\
 \Psi = x\left(t_f\right) - 100 m = 0 & \\
\end{matrix}
:::

Use what we learned from [Application of the Optimal Control Theory](#application-of-the-optimal-control-theory). Start by constructing the Hamiltonian  using Equations {eq}`zerm_hammy`

:::{math}
H = \lambda_1 \left(2\cos{\delta} \right) + \lambda_2 \left(2\sin{\delta} + 2 \sin{\frac{\pi x}{100}} \right)
:::

From Equations{eq}`zerm_dlambda_dt` and combined dynamics acting on the boat {eq}`zermo_dynamics` we'll get that:

:::{math}
:label: zerm_case2_boat_dynamics
\begin{align*}
\dot{x} &= 2\cos{\delta}  \\
\dot{y} &= 2\sin{\delta} + 2 \sin{\frac{\pi x}{100}}
\end{align*}
:::

:::{math}
:label: zerm_case2_boat_dynamics_reduced
\begin{align*}
\dot{\lambda}_1 &= -\frac{\lambda_2\pi}{50}\cdot\cos{\left(\frac{\pi x}{100}\right)} \\
\dot{\lambda}_2 &= 0
\end{align*}
:::

Most times it is useful to write the local dynamics in terms of $\lambda$ for solving this sort of problem numerically. Bring together Equation {eq}`zerm_control_reduced` and {eq}`zerm_case2_boat_dynamics` to get. 

:::{math}
:label: zerm_case2_boat_dynamics_reduced
\begin{align*}
\dot{x} &= -\frac{2\lambda_1}{\sqrt{\lambda^2_1+\lambda^2_2}}  \\
\dot{y} &= -\frac{2\lambda_2}{\sqrt{\lambda^2_1+\lambda^2_2}} + 2 \sin{\frac{\pi x}{100}}
\end{align*}
:::

Lastly from the terminal constraint {eq}`zerm_bound_conditions` we'll get:

:::{math}
:label: 
\lambda_2\left(t_f\right) = -1
:::

### Numerical Problem Definition

**Bounds**

:::{math}
:label: zerm_case2_bounds_updated
\begin{matrix}
 x\left(0\right) = 0 & \lambda_1\left(t_f\right) - K_1 = 0 \\  
 y\left(0\right) = 0 & \lambda_2\left(t_f\right) = -1 \\
 x\left(t_f\right) = 100 &  
\end{matrix}
:::


**Differential Equations**

:::{math}
:label: zerm_case2_diff_eqs
\begin{align*}
\dot{x} &= -\frac{2\lambda_1}{\sqrt{\lambda^2_1+1}}  \\
\dot{y} &= -\frac{2\lambda_2}{\sqrt{\lambda^2_1+1}} + 2 \sin{\frac{\pi x}{100}} \\
\dot{\lambda}_1 &= \frac{\pi}{50}\cdot\cos{\left(\frac{\pi x}{100}\right)} \\
\end{align*}
:::

**Control**

:::{math}
:label: zerm_case2_control
\delta = \tan^{-1}\left[-\frac{1}{\lambda_1}\right]
:::

**Shooting Method** 

There are many numerically methods for solving this [Problem Definition](#numerical-problem-definition) but one of the most popular numerical approach is the [Shooting Method](https://en.wikipedia.org/wiki/Shooting_method). This can be expressed as a targeting or root-find problem using [scipy.optimize.fsolve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.fsolve.html) to search for an optimal trajectory that matches the constraints.

:::{math}
\mathbf{S}(\mathbf{z}) - \mathbf{z_f} = 0
:::

Instead of looking for $\lambda_1\left(t_0\right)$ that maximizes our upstream distance travelled, we can look for $\mathbf{z}$ where $\mathbf{S}(\mathbf{z})$ is the arrangement of components of $\mathbf{x}(t_f)$ that meet final constraints {eq}`zerm_case2_bounds_updated`

:::{math}
:label: zerm_shooting_method
\begin{bmatrix}
x\left(t_f\right) \\
\lambda_2\left(t_f\right) 
\end{bmatrix} - 
\begin{bmatrix}
100 \\
-1 
\end{bmatrix}  = 0
:::

## Solving Example Using Python 

Begin by importing module zermelos.py TODO link to github [zermelos](zermelos.py) and setting initial state vector and target position Equation {eq}`zerm_case2_bounds`. 

:::{math}
:label: zerm_py_example_state
\mathbf{r}\left(t_0\right) = 
\begin{bmatrix}
0.0 \\
0.0 
\end{bmatrix}
:::

Take an initial boat angle guess of 45$^{\circ}$. 

:::{math}
:label: zerm_py_example_initial_guess
\begin{align*}
\mathbf{\delta}\left(t_0\right)  &= {45}^{\circ}  \\
\mathbf{\lambda_1}\left(t_0\right) &=  \left[ -1 \right]
\end{align*}
:::

Set the target x-position as the width of the river (**Figure X.2**) in this case let's assume 100 meters and a constant boat velocity of 2 m/s as stated in Equation {eq}`zerm_case2_bounds`. 

```python
import numpy as np
from zermelos import zermelos
import zermelos_plots as zplts

# Initial State
# --------------------------------------------------------------------------------
initial_guess = [ 0, # x-position
                  0, # y-position
                 -1] # lambda_1, 45 degrees

# Constant velocity
boat_velocity = 2.0 # m/sec

# Final x-position
final_pos = 100 # meters
```

Instantiate class `zermelos.boat()` with initial state guess. This being a fixed time analysis of 100 seconds. 

```python
# Instantiate Analysis Object
# --------------------------------------------------------------------------------
opt_analysis = boat(initial_guess)

# Numerical Analysis Setup
# --------------------------------------------------------------------------------
opt_analysis.x_target = 100 # meters

opt_analysis.boat_velocity = boat_velocity # m/sec
time = np.linspace(0,100,1000) # seconds
opt_analysis.time = time
```

Solve the initial guess and observe the boat's trajectory. Method `boat.solve_initial_value_problem()` uses [scipy.integrate.solve_ivp](https://docs.scipy.org/doc/scipy/reference/generated/scipy.integrate.solve_ivp.html) to solve derived boat Differential Equations {eq}`zerm_case2_diff_eqs`

```python
# Run Numerical Analysis: 
# --------------------------------------------------------------------------------

# Solve initial guess
# -------------------------------------
opt_analysis.initial_value_problem = initial_guess
opt_analysis.solve_initial_value_problem()

# Plot Results
zplts.plot_trajectory(opt_analysis)
```

From **Figure X.3** we can see that our initial guess of $\lambda_{1}\left(t_0\right) =  -1$ results in an infeasible solution. As the boat moves upstream it returns to the starting side in approximately **33.1 seconds** yet our goal is to cross the river. Let's move forward with the initial guess and let the solver find a solution that is not only feasible but also maximizes the distance travelled upstream. 


```{figure} ./images/zermelos_initial_guess_trajectory.png
:name: fig:initial_control_guess
:width: 100%
**Figure X.3** Initial Boat Control Guess
```

Solve Zermelo's Optimal Control Problem using the Shooting Method {eq}`zerm_shooting_method` by calling method `boat.solve_trajectory()`. This method is allowed to vary $\lambda_1$ guess until constraint $\Psi$ {eq}`zerm_case2_bounds` is satisfied. 

```python
# Solve Optimal Control Problem
# -------------------------------------
# Run shooting method with scipy solver 
opt_analysis.solve_trajectory()
```

Generate plots to inspect the shooting method results. First let's plot the solution:

```python 
# Plot Boat Trajectory
zplts.plot_trajectory(opt_analysis)
```

```{figure} ./images/zermelos_final_trajectory.png
:name: fig:final_trajectory
:width: 100%
**Figure X.4** Converged Optimal Control Trajectory
```

TODO: Talk about trajectory results, number of iterations, and inflection point matches sinusoid nature of river current. 

Next let's look at the number of iterations the solver used and display the trajectory history as it converged. 

```python
# Plot Shooting Method Results
zplts.plot_trajectory_shooting_method(opt_analysis)
```

```{figure} ./images/zermelos_trajectory_history.png
:name: fig:zermelos_trajectory_history
:width: 100%
**Figure X.5** Trajectory History of Converged Objective Function
```

Note that some of these trajectories are infeasible as they cross the river boundaries for a give fixed time of 100 seconds. 

TODO: Talk more about the results and how the solver swept different regions

Now inspect the final solution. The converged solution is stored in attribute `boat.final_state`.

```python
print(opt_analysis.final_state)
```

```
[100.         315.52936904  -1.7597103 ]
```

The output of `boat.final_state` returns the final state vector $\left[x_f,y_f,\lambda_{1,f}\right]$. We notice that the terminal constraint {eq}`zerm_case2_bounds` of **100 meters is met**. The solver converged to a maximize upstream distance of **315.529 meters**. The $\lambda_1$ value shown here corresponds to the final control $\lambda_{1}\left(t_f\right)$ observed. However, we are interested in knowing the initial control $\lambda_{1}\left(t_0\right)$ the solver converged towards. To get this inspect the shooting method results stored in attribute `boat.lambda_solution`

```python
print(np.degrees(np.arctan2(1,-1*opt_analysis.lambda_solution)))

```

```
[-1.7597103]
```

This happens to match $\lambda_1\left(t_f\right)$. Using Equation {eq}`zerm_case2_control` this value corresponds to an initial **boat angle of 29.61$^{\circ}$**. To get a better understanding of the boat's motion of the 100 seconds of travel let us plot the state history and control as a function of time. 

```python
zplts.plot_state_history(opt_analysis)
```

```{figure} ./images/zermelos_boat_state_history.png
:name: fig:boat_state_history
:width: 100%
**Figure X.6** State History of Optimal Control Solution
```

Want to check if dH/du = 0

## Solving Alternative River Example Using Python 

TODO: Give example of alt. river current and results