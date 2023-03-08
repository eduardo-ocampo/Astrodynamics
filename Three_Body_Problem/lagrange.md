## Lagrange 

The Lagrange Points are equilibrium points in a dynimcal system. Here the dynamical system to analysis is the [Non-Dimensional Circular Restricuted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem). 

TODO: Provide figure Topology of Lagrange Points in the rotating coordinate fram

The potential for this system is define as Equation {eq}`cr3bp_V_norm`
 
:::{math}
\tilde{V}\left(x^*,y^*,z^*\right) = \frac{1}{2}\left( {x^*}^2 + {y^*}^2\right) + \frac{1-\mu}{r^*_1} + \frac{\mu}{r^*_2}
:::

where $r^*_1$ and $r^*_2$ are:

:::{math}
r^*_1 = \sqrt{\left( x^* + \mu \right)^2+{y^*}^2+{z^*}^2}
:::

:::{math}
r^*_2 = \sqrt{\left( x^* - 1 + \mu \right)^2+{y^*}^2+{z^*}^2}
:::

```{warning}
The non-dimensional length term in section [Non-Dimensional Circular Restricuted Three-Body Problem](cr3bp.md#non-dimensional-circular-restricted-three-body-problem) is defined as:


:::{math}
\mathbf{r}^* = \frac{\mathbf{r}}{r_s} = \frac{\mathbf{r}}{R}
:::

For this section on **Lagrange Points & Stability**, $^*$ notation will be dropped from parameters. It should be made clear that the discussion here applies to a **Non-Dimensional System**. 


```

To find the location of the Lagrange Points take the partile of $\mathbf{\tilde{V}}$ and find locations where motion is zero. Taking the partial of $\mathbf{\tilde{V}}$ yields:

Show partile direviate of V

:::{math}
:label:
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{x}} = x - \frac{(1-\mu)(x+\mu)}{{r_1}^3} - \frac{\mu(x+\mu-1)}{{r_2}^3}
:::

:::{math}
:label:
dv/dy
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{y}}
:::

:::{math}
:label:
dv/dz
\frac{\partial{\mathbf{\tilde{V}}}}{\partial{z}}
:::

L1, L2, L3 are unstable

L4, and L5 are stable

### Co-Linaer Points

For L1, L2, and L3 the y- and z-coordnaties are zero. This reduces their known position vectors Eq ABOVE to depending only on their location along the x-axis relative to primary bodies.

r_1 = |x+mu|
r_2 = |x-1+mu|

Now subsitiute the relative position vector Eq {}`above` into dv/dx. To compute the x-coordnates of L1, L2, adn L3 we need to solve dv/dx only since dv/dy= 0 dv/dz = 0.

slide 3
:::{math}

dv/dx = 0

:::

Show plot for dv vs dx

Plot dv/dx to illustraute how the potential changes as a funciton of position. 

Figure 


What you will see is that as x -> P1, it that dv crosses L3 and the head asymptotically to infition at P1. Then as x -> P2 the potential trend from negative infinity to positive infinity while crossing L1. Fianlly the potentialtneds from negative infitinty to positive infitiny while crossing L2. 

By simply plotting dv/dx it gives a quick and easy means of locating L1, L2, and L3 for an arbituary mu. There are many numerical solvers for getting the roots of a funciton like dv/dx and an example is shown below TODO ADD EXAMPLE. 

To aid in solving the lagrantge points using Equation EQ{} let us approxiamte the co-linear equalirbirum points. If we expand out Eq{} up to the first power we get:

Show HOT approximate terms
:::{math}

:::
     
By remvoing higer order terms the equations are roughly 


Show HOT approximate terms
:::{math}

:::

The approximate equations for co-lineary Lagrange POints can be used to intiailize a solver before solving for Equation dv/dx.  

### Example

Here add homeworrk problem that asks us to craete plots of L1, L2, and L3 for vary mu

## equilateral lagrange points

Solving for the posiiton of Lagrange Ponints 4 and 5 are failry straighforwad compared to the co-linear lagrange points. The equailaterl lagrange opints exist such that y=/ 0. Now check Equation {}`dv/dy` 

:::{math}
dv/dy = 0
:::

Equation ABOVE is trival and results in the relative position vectors t have a magnitude of r_1 = 1 and r_2 = 1. Now applying this information to the dfeineito of dv/dx eq{adove dv/dx} reduces to 


:::{math}
dv/dx = x - (1-mu)(x+mu) - mu(x+mu-1)
:::

Sovling for dv/dx = 0 gives exatcly:

x_4,5 = 1/2 -mu

and using equation for r_1^2 = (x+mu)^2 + y^2 + z^2 and r_2^2 = (x-1+mu)^2 +y^2 + z^2 gives the y-coordintea of the equlatiater lagrante oitns

y_4,5, = +- sqrt(3/2)

This shows that lagrange points L4 and L5 lie equaliteraly along P1 and P2. 

Thus we have exact results of for Lagrange POints 4 and 5 whereas Lagraen Points 1,2,3 are needed to solve iterativly while you can intiialized your solver by using the approxiamte values eq{}. 

For a non-restricted Three-body problem system (mu_3 not 0), these 5 Lagrante Poitns still exits. However, the positions of the co-linear lagrange points are shifted. If the primarires P1 and P2 are on a ellitpical orbit analogue of the Lagrange Points due exisits. If 