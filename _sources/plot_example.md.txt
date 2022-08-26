---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.14.1
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Examples of Rendering Plots in HTML

```{code-cell} ipython3
from myst_nb import glue
a = "my variable!"
glue("my_variable", a)
```

```{glue} my_variable
```

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
N = 10
```

```{code-cell} ipython3
data = np.linspace(1,10,10)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(6, 2))
ax.plot(data)
glue("boot_fig", fig, display=True)
```

```{glue:} boot_fig
```

# Plotly Examples

<!-- ```{code-cell} ipython3
from IPython.display import HTML
from the_orbit_equation import def_inclination
from myst_nb import glue

glue("def_inclination", HTML(def_inclination.html), display=False)
```

:::{glue:figure} def_inclination
::: -->
<!-- 

```{code-cell} ipython3
import plotly.express as px
df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 size='petal_length', hover_data=['petal_width'])
fig.show()

from plotly.io import to_html

fig_html = to_html(fig, full_html=True)

from myst_nb import glue

glue("fig", fig_html, display=False) 
```

:::{glue:figure} fig
::: -->

```{code-cell} ipython3
import plotly.express as px
df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width',
              color='species')
fig.show()
```


```{code-cell} ipython3
import plotly.io as pio
import plotly.express as px
import plotly.offline as py

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", size="sepal_length")
```

```{code-cell} ipython3
from myst_nb import glue

glue("fig", fig, display=False)
```

:::{glue:figure} fig
:::

```{code-cell} ipython3
import plotly.express as px
data = px.data.iris()
data.head()


from bokeh.plotting import figure, show, output_notebook
output_notebook()
```

```{code-cell} ipython3
p = figure()
p.circle(data["sepal_width"], data["sepal_length"], fill_color=data["species"], size=data["sepal_length"])
show(p)
```

