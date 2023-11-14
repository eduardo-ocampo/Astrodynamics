""" --------------------------------------------------------------------------
            Example of Calculating and Plotting Semi-Major Axis for 
            the Two Body Problem

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import numpy as np
import plotly.graph_objects as go

def plot():

    # Angles
    f = np.linspace(0,2*np.pi,1000)
    # Semi-Major Axis List and Associated colors
    a_list = [0.1,0.2,0.4,0.6,0.8,1.0]
    colors = ['yellow','orchid','green','darkorange','blue','red']

    # Plot Orbits by Varying Semi-Major Axis
    fig = go.Figure()
    for indx,a in enumerate(a_list):
        
        # Eccentricity
        e = 0.6
        p = a*(1-e**2)
        # Orbit Position
        r = p/(1+e*np.cos(f))
        pos = np.zeros((len(f),3))
        pos[:,0] = r*np.cos(f)
        pos[:,1] = r*np.sin(f)

        # Draw Orbit and Their Centers
        orbit = go.Scatter3d(x=pos[:,0], 
                             y=pos[:,1],
                             z=pos[:,2], mode='lines', name="a = {}".format(a),
                             line=dict(width=4,color=colors[indx])
        )
        orbit_center = go.Scatter3d(x=[-a*e], 
                                    y=[0],
                                    z=[0], mode='markers', 
                                    marker_symbol = 'cross',showlegend=False,
                                    marker=dict(size=4,color=colors[indx])
        )
        fig.add_trace(orbit)
        fig.add_trace(orbit_center)

    # Add Central Body as Point Mass
    center = go.Scatter3d(x=[0,0], 
                          y=[0,0],
                          z=[0,0], mode='markers', name = "Centeral Body",
                          marker=dict(size=8,color='black')
    )
    # Hack to add include Orbit Center as part of the Legend
    center_legend = go.Scatter3d(x=[0], 
                                 y=[0],
                                 z=[0], mode='markers', marker_symbol = 'cross',
                                 name = "Orbit Center",
                                 marker=dict(size=5,color='black')
    )

    fig.add_trace(center_legend)   
    fig.add_trace(center)

    # Set Viewing Angle
    camera = dict(eye=dict(x=0.0, y=1.0, z=1.5))

    # Update Figure
    fig.update_layout(scene_camera=camera,
                      legend=dict(orientation="h",
                                  yanchor="bottom"),
                      title={'text': "<b>Elliptical Orbit Shape by Semi-Major Axis<b>",
                             'y':0.95,
                             'x':0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      margin=dict(r=10, l=10,
                                  b=1,  t=50)
    )

    return fig

