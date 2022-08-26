# An Attempt To Show Math

Here we go

Reference: 
https://matplotlib.org/stable/tutorials/text/mathtext.html
https://jupyterbook.org/en/stable/content/proof.html

```{math}
:label: my_other_label
\int_0^\infty \frac{x^3}{e^x-1}\,dx = \frac{\pi^4}{15}
```
Alternatively you can use the dollar math syntax with a prefixed label:

```{math}
:label: my_label
w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
```

```md
$$
  w_{t+1} = (1 + r_{t+1}) s(w_t) + y_{t+1}
$$ (my_other_label)
```

:::{math}
:label: eq:gravity-acceleration
g = \frac{GM}{r^2}
:::

:::{math}
:label: eq:gravity-acceleration
s(t) = \mathcal{A}\mathrm{sin}(2 \omega t)
:::

:::{math}
:label: eq:Two_Body_EOM
\ddot{\mathbf{r}} = -G\frac{(m_1+m_2)}{r^3}\mathbf{r}
:::

### Linking to equations

If you have created an equation with a label, you can link to it from within your text
(and across pages!).

You can refer to the equation using the label that you've provided by using
the `{eq}` role. For example:

```md
- A link to an equation directive: {eq}`my_label`
- A link to a dollar math block: {eq}`my_other_label`
```

results in

- A link to an equation directive: {eq}`my_label`
- A link to a dollar math block: {eq}`my_other_label`

```{note}
`\labels` inside LaTeX environment are not currently identified, and so cannot be referenced.
We hope to implement this in a future update (see [executablebooks/MyST-Parser#202](https://github.com/executablebooks/MyST-Parser/issues/202))!
```

```{warning}
Adding your own Sphinx configuration and extensions may cause Jupyter Book to behave
unpredictably.
Use at your own risk!
```