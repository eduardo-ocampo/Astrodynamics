""" --------------------------------------------------------------------------
            Example of Calculating and Plotting Non-Dimensional Circular 
            Restricted Three-Body Problem (CR3BP) Force Potential

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import math
import numpy as np
import plotly.graph_objects as go

# Dimensional
# --------------------------------------------------------------
def force_potential():

    # Newtonian constant of gravitation
    # https://ssd.jpl.nasa.gov/astro_par.html 
    G = 6.6743e-20 # km^3 kg^-1 s^-2

    # Earth-Moon System Parameters
    # ----------------------------------------------------------
    # https://ssd.jpl.nasa.gov/planets/phys_par.html
    # Earth Mass
    m1 =  5.972e24 # kg
    # Moon Mass
    m2 =  7.349e22 # kg
    mu = m2/(m1+m2)

    # Distance Between Bodies
    R = 384472.282 # km

    n = np.sqrt(G*(m1+m2)/R**3) # Mean Motion

    # Compute Pseudo-Potential
    # ----------------------------------------------------------
    min_range = -5e5
    max_range =  5e5
    x = np.linspace(min_range, max_range, 150)
    y = np.linspace(min_range, max_range, 150)
    X, Y = np.meshgrid(x, y)

    V = -1*((n**2)*(X**2+Y**2) +\
            ((G*m1)/(np.sqrt((X+(m2/(m1+m2))*R)**2+Y**2))) +\
            ((G*m2)/(np.sqrt((X-(m1/(m1+m2))*R)**2+Y**2))) )

    # Plot Props
    # ----------------------------------------------------------
    z_axis_min = -5.0
    z_axis_max =  0.0
    plane_size = 5.5e5

    # Cut singularity for better looking plot
    potent_min = -4
    V[V<potent_min] = np.nan

    # Plotly Figure
    # ----------------------------------------------------------
    title = "<b>Pseudo-Potential for Earth-Moon System<sup>*</sup></b> <br>" + \
                                     "R={:.2e} km, μ ={:.6f}".format(R,mu)

    # Draw Potential Surface
    potential = go.Surface(z=V, x=X, y=Y,
                        hoverinfo='text',colorscale ='viridis',
                        text="Pseudo-Potential for Earth-Moon System")

    # Draw Reference Bodies
    earth_pos = go.Scatter3d(x=[0],y=[0],z=[-2],name = "Earth",
                            mode='markers+text',showlegend=False,
                            marker=dict(size=14,color='royalblue'))

    moon_pos = go.Scatter3d(x=[R],y=[0],z=[-2],name = "Moon",
                            mode='markers',showlegend=False,
                            marker=dict(size=6,color='dimgrey'))

    # Define Figure and Add Drawings
    fig = go.Figure()
    fig.add_trace(potential)
    # Update Contour Trace
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", 
                                      project_z=True))     
    fig.add_trace(earth_pos)
    fig.add_trace(moon_pos)

    # Set Viewing Angle
    camera = dict(eye=dict(x=1.1, y=-0.7, z=0.6),
                center=dict(z=-0.3))

    # Update Figure
    fig.update_layout(title={'text': title,
                            'xanchor': 'center','yanchor': 'top',
                            'y':0.9,'x':0.5,},
        scene = dict(camera = camera,
                     xaxis = dict(title="X-Coord. [km]",nticks=8,
                                 titlefont=dict(size=10),
                                 range=[-plane_size,plane_size],
                                 showgrid=True,showbackground=False,
                                 visible=True,zeroline=True),
                     yaxis = dict(title="Y-Coord. [km]",nticks=8,
                                 titlefont=dict(size=10),
                                 range=[-plane_size,plane_size],
                                 showgrid=True,showbackground=False,
                                 visible=True,zeroline=True),
                     # TODO: Figure out how to render latex using Plotly
                     # https://plotly.com/python/LaTeX/
                     zaxis = dict(title="V",range=[z_axis_min,z_axis_max],
                                  visible=True,showgrid=False,zeroline=True,
                                  showaxeslabels=False,showticklabels=False),
                     aspectmode='cube'),
    )

    # Add annotation
    fig.add_annotation(dict(x=0, y=-0.12, xanchor='left',
                            showarrow=False,font=dict(size=9),
                            text="*Bodies Not to Scale",
                            xref="paper",yref="paper"))

    return fig

# Non-Dimensional
# --------------------------------------------------------------
def non_dim_force_potential():

    # Mass Ratio
    # ----------------------------------------------------------
    mu = 0.09
    
    # Compute Pseudo-Potential
    # ----------------------------------------------------------
    min_range = -1.5
    max_range =  1.5
    x = np.linspace(min_range, max_range, 200)
    y = np.linspace(min_range, max_range, 200)
    X, Y = np.meshgrid(x, y)

    V = -1*(0.5*(X**2+Y**2) +\
            ((1-mu)/(np.sqrt(((X+mu)**2)+Y**2))) +\
            (mu/(np.sqrt(((X-1+mu)**2)+Y**2)))  )

    # Plot Props
    # ----------------------------------------------------------
    z_axis_min = -3.0
    z_axis_max = -1.1

    # Cut singularity for better looking plot
    potent_min = -3.5
    V[V<potent_min] = np.nan

    fig = go.Figure(data=[go.Surface(z=V, x=X, y=Y,colorscale ='plasma')])
  
    # Plotly Figure
    # ----------------------------------------------------------
    title = "<b>Pseudo-Potential for Non-Dimensional System<sup>*</sup></b> <br>" + \
                                     "μ ={:.3}".format(mu)

    # Draw Potential Surface
    potential = go.Surface(z=V, x=X, y=Y,
                        hoverinfo='text',colorscale ='plasma',
                        text="Pseudo-Potential for Non-Dimensional System")

    # Draw Reference Bodies
    primary_body = go.Scatter3d(x=[-mu],y=[0],z=[-1.5],name = "Primary Body",
                            mode='markers+text',showlegend=False,
                            marker=dict(size=18,color='black'))

    second_body = go.Scatter3d(x=[1-mu],y=[0],z=[-1.5],name = "Secondary Body",
                            mode='markers',showlegend=False,
                            marker=dict(size=8,color='darkviolet'))

    # Define Figure and Add Drawings
    fig = go.Figure()
    fig.add_trace(potential)
    # Update Contour Trace
    fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                      highlightcolor="limegreen", 
                                      project_z=True))     
    fig.add_trace(primary_body)
    fig.add_trace(second_body)
    
    # Set Viewing Angle
    camera = dict(eye=dict(x=1.1, y=-0.7, z=0.9),
                  center=dict(z=-0.1))
    # Update Figure
    fig.update_layout(title={'text': title,
                            'xanchor': 'center','yanchor': 'top',
                            'y':0.9,'x':0.5,},
        scene = dict(camera = camera,
                     xaxis = dict(title="X-Coord.",nticks=8,
                                 titlefont=dict(size=10),
                                 showgrid=True,showbackground=False,
                                 visible=True,zeroline=True),
                     yaxis = dict(title="Y-Coord.",nticks=8,
                                 titlefont=dict(size=10),
                                 showgrid=True,showbackground=False,
                                 visible=True,zeroline=True),
                     zaxis = dict(title="ṽ",visible=True,
                                  showgrid=False,zeroline=True,
                                  showaxeslabels=False,showticklabels=False),
        )
    )

    # Add annotation
    fig.add_annotation(dict(x=0, y=-0.12, xanchor='left',
                            showarrow=False,font=dict(size=9),
                            text="*Bodies Not to Scale",
                            xref="paper",yref="paper"))

    return fig