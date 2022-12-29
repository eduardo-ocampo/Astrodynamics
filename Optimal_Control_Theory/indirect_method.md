
# Optimal Control Theory

## Background

TODO: Mark latex math for label

In this section, we will look at optimizing a co-planar rendezvous manevour. We disire a thrurst direction function that minimizes fuel mass and time of flight. Given a constant thrust rocket engine T = thrust operation for a given length of time tf. Show the optimal trajetory from a cirular orbit of XXX to XXX which are coplanar. 

Simplififed equations of motion,

:::{math}
:label:
\dot{\mathbf{r}} = \mathbf{v}
:::

:::{math}
:label:
\dot{\mathbf{v}} = -\frac{\mu}{r^3}\mathbf{r} + \frac{T}{m}
\begin{pmatrix}
\cos{\theta}\cos{\phi} \\
\sin{\theta}\cos{\phi} \\
\sin{\phi}
\end{pmatrix}
:::


The transfer starts at $t_0$ = 0 and ends with thrust burn cutoff at $t_f$, with a given mass flow rate of $\alpha$

:::{math}
:label:
\dot{m} = -\alpha
:::

Boundary conditions

:::{math}
\begin{matrix}
 Initial & Final \\ 
 \mathbf{r}(t_0) = \mathbf{r_0} & \mathbf{r}(t_f) = \mathbf{r_f} \\  
 \mathbf{v}(t_0) = \mathbf{v_0} & \mathbf{v}(t_f) = \mathbf{v_0} \\  
 m(t_0) = m_0                   & m(t_f) = \text{free variable} \\  
\end{matrix}
:::

To meet our objective of minizing fuel mass we will want to maximize $m(t_f)$ which is the same as minizime transfer time. 



## Optimal Transfer - Indirect Method

Using Optimal Control Theory to select the optimal thrust direction over time. This section follows the notation from LINK BOOK.

Write out the cost function

:::{math}
:label:
\bar{J} = \Phi(x(t_f),t_f) + \int_{t_0}^{t_f} L(x(t),u(t),t) dt
:::
:::{math}
\bar{J} = \Phi(x(t_f),t_f) + 0
:::
:::{math}
:label:
\bar{J} = -m(t_f)
:::
:::{math}
\Phi = -m(t_f)
:::

The control parameter is

:::{math}
:label:
u(t) = 
\begin{bmatrix}
\theta(t) \\
\phi(t)
\end{bmatrix}
:::


The Hamiltonian is, therefore,

:::{math}
H = \lambda(t)^T
:::

:::{math}
H[x(t),u(t),\lambda(t),t] = L(x(t),u(t),t) + \mathbf{\lambda(t)}^T \mathbf{\mathit{f}} 
:::
:::{math}
H = \mathbf{\lambda}(t)^T \mathbf{\mathit{f}} = \mathbf{\lambda^T}\mathbf{\mathit{f}}
:::

Where,
:::{math}
:label:
\mathbf{\lambda}(t) = 
\begin{bmatrix}
\lambda_r(t) \\
\lambda_v(t) \\
\lambda_m(t)
\end{bmatrix}
:::

:::{math}
:label:
\mathbf{\mathit{f}} = 
\begin{bmatrix}
\mathbf{v} \\
-\frac{\mu}{r^3}\mathbf{r} + \frac{T}{m}
\begin{pmatrix}
\cos{\theta}\cos{\phi} \\
\sin{\theta}\cos{\phi} \\
\sin{\phi}
\end{pmatrix} \\
-\alpha
\end{bmatrix}
:::

:::{math}
:label:
H = \mathbf{\lambda}_r^T\mathbf{v} -\frac{\mu}{r^3}\mathbf{\lambda}_r^T\mathbf{r} + \frac{T}{m}\mathbf{\lambda}_r^T 
\begin{pmatrix}
\cos{\theta}\cos{\phi} \\
\sin{\theta}\cos{\phi} \\
\sin{\phi}
\end{pmatrix}
- \lambda_m\alpha
:::


Obtain the differential equations for $\lambda(t)$ by evaluting 

:::{math}
\dot{\mathbf{\lambda}}(t) = -\frac{\partial{H}}{\partial{x}}
:::

Recall that position and velocity vectors each contain 3 states, thus in total there will be 7 differtial equations for $\lambda(t)$.

TODO: Left align this
:::{math}
\dot{\mathbf{\lambda}_r} = -\frac{3\mu}{r^5}\mathbf{r}^T\mathbf{\lambda}_v\mathbf{r} + \frac{\mu}{r^3}\mathbf{\lambda}_v
:::
:::{math}
\dot{\mathbf{\lambda}_v} = -\mathbf{\lambda}_r
:::
:::{math}
\dot{\mathbf{\lambda}_m} = \frac{T}{m^2}
\begin{pmatrix}
\cos{\theta}\cos{\phi} \\
\sin{\theta}\cos{\phi} \\
\sin{\phi}
\end{pmatrix}
\mathbf{\lambda}_v
::: 



Next, we obtain the control by evaluting 

:::{math}
\frac{\partial{H}}{\partial{u(t)}}= 0
:::

The components that contain our control parameters influence the result. Those partials are shown below 

:::{math}
:label:
\frac{\partial{H}}{\partial{\theta}} = \frac{T}{m}\mathbf{\lambda}_v^T
\begin{bmatrix}
-\sin{\theta}\cos{\phi} \\
\cos{\theta}\cos{\phi} \\
0
\end{bmatrix}
:::
:::{math}
:label:
\frac{\partial{H}}{\partial{\phi}} = \frac{T}{m}\mathbf{\lambda}_v^T
\begin{bmatrix}
-\cos{\theta}\sin{\phi} \\
-\sin{\theta}\sin{\phi} \\
0
\end{bmatrix} 
:::

After a few algebraic steps the control matrix has the form,

:::{math}
:label:
\begin{bmatrix}
\cos{\theta}\cos{\phi} \\
\sin{\theta}\cos{\phi} \\
\sin{\phi}
\end{bmatrix} =
\begin{bmatrix}
\frac{\lambda_{v1}}{\lambda_{v12}} \frac{\lambda_{v12}}{|\lambda_{v}|} \\
\frac{\lambda_{v2}}{\lambda_{v12}} \frac{\lambda_{v12}}{|\lambda_{v}|} \\
\frac{\lambda_{v3}}{|\lambda_{v}|} \\
\end{bmatrix} = 
\frac{\mathbf{\lambda_{v}}}{|\mathbf{\lambda_{v}}|} 
:::

The result is the so-called primer vector noteably coined by Derek Lawden and his investiageiton of optimal orbit transfers. LINK SOMETHING HERE.Lawden, D. F. (1963) Optimal Trajectories for Space Navigation, Butterworths, London.Google Scholar

Finally, we can use prime vector Eq XXX to simplify equation XXX and equation XXX

:::{math}
:label:
\dot{\lambda}_m = \frac{T}{m^2}|\mathbf{\lambda}_v|
:::

:::{math}
:label:
H = \mathbf{\lambda}_r^T\mathbf{v} -\frac{\mu}{r^3}\mathbf{\lambda}_r^T\mathbf{r} + \frac{T}{m}|\mathbf{\lambda}_v| - \lambda_m\alpha
:::

Now determine the bound conditions for $\lambda(t)$ by evalutaing $\frac{\partial{\Phi}}{\partial{x}}$. 

:::{math}
\mathbf{\lambda}(t_f) = \left[\frac{\partial{\Phi}}{\partial{x(t_f)}}\right]^T
:::

Note that if a value is specified for a component of the state x($t_f$) then there is no condition its $\lambda$($t_f$) and it is a free variable.


:::{math}
\begin{matrix}
 \mathbf{\lambda}_r(t_0) = \text{free} & \mathbf{\lambda}_r(t_f) = \text{free} \\  
 \mathbf{\lambda}_v(t_0) = \text{free} & \mathbf{\lambda}_v(t_f) = \text{free} \\  
 \mathbf{\lambda}_m(t_0) = \text{free} & \mathbf{\lambda}_m(t_f) = -1 \\  
\end{matrix}
:::

The results shows our natural boundary condition. Note that the control is not a function of $\mathbf{\lambda}_m(t)$. Solving this problem now depends on finding $\mathbf{\lambda}_r(t_0)$ and $\mathbf{\lambda}_v(t_0)$ such that $\mathbf{r}(t_f) = \mathbf{r}_f$ and $\mathbf{v}(t_f) = \mathbf{v}_f$

The next section will conver how numerically solve for $\lambda(t)$ and make use of the boundary conditions. 



# Numerical Setup - Indirect Method


## Compare to Hohmann transfer problem