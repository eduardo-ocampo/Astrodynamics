import numpy as np
import plotly.graph_objects as go

def plot():

    # Angles
    f = np.linspace(0,2*np.pi,1000)
    # Eccentricity List and Associated Colors
    e_list = [0.0, 0.2, 0.4, 0.6, 0.8, 0.9, 0.95]
    colors = ['red','green','blue','darkorange','yellow','orchid','dimgrey']

    # Plot Orbits by Varying Eccentricity
    fig = go.Figure()
    for indx,e in enumerate(e_list):
        
        # Eccentricity
        a = 1.0
        p = a*(1-e**2)
        # Orbit Position
        r = p/(1+e*np.cos(f))
        pos = np.zeros((len(f),3))
        pos[:,0] = r*np.cos(f)
        pos[:,1] = r*np.sin(f)

        # Draw Orbit and Their Centers
        orbit = go.Scatter3d(x=pos[:,0], 
                             y=pos[:,1],
                             z=pos[:,2], mode='lines', name="e = {}".format(e),
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
                      title={'text': "<b>Elliptical Orbit Shape by Eccentricity<b>",
                             'y':0.95,
                             'x':0.5,
                             'xanchor': 'center',
                             'yanchor': 'top'},
                      margin=dict(r=10, l=10,
                                  b=1,  t=50)
    )

    return fig