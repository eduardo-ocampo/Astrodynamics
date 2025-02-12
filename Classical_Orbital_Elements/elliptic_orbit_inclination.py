""" --------------------------------------------------------------------------
            Example of Calculating and Plotting Orbit Inclination for 
            the Two Body Problem

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import numpy as np
from numpy.linalg import norm
import plotly.graph_objects as go
from scipy.spatial.transform import Rotation as R

def plot():

    # Inclination Defintion
    inclination_angle = 25 # degrees
    r = R.from_euler('y', inclination_angle, degrees=True)
    rotation = r.as_matrix()

    # Set Equatorial Plane shape
    plane_size = 6
    points = np.array([[ plane_size,    plane_size, 0],
                       [-plane_size-5,  plane_size, 0],
                       [ plane_size,   -plane_size, 0],
                       [-plane_size-5, -plane_size, 0]])

    # Establish Central Body Reference Axis
    axes_scale = 2
    axes = np.array([[1,0,0],
                    [0,1,0],
                    [0,0,1]])
    axes = axes*axes_scale

    # Spacecraft Trajectory
    f = np.linspace(0,2*np.pi,1000) # Angles
    a = 5
    e = 0.55
    p = a*(1-e**2)
    r = p/(1+e*np.cos(f))
    r_p = a*(1-e)
    pos = np.zeros((len(f),3))
    pos[:,0] = r*np.cos(f)
    pos[:,1] = r*np.sin(f)

    # Inclination Rotation
    pos_rot = np.array([rotation @ p for p in pos])
    p_rot_vector = rotation @ np.array([0,p,0])
    r_p_rot_vector = rotation @ np.array([r_p,0,0])

    # Angular Momentum
    h_scale = 2
    angular_momentum = h_scale*(np.cross(r_p_rot_vector,p_rot_vector)/norm(np.cross(r_p_rot_vector,p_rot_vector)))

    # Calc Inclination Angle Arc
    arc_x = np.sin(np.linspace(0,np.radians(inclination_angle),100))
    arc_y = np.zeros(100)
    arc_z = np.cos(np.linspace(0,np.radians(inclination_angle),100))
    arc = np.vstack((arc_x,arc_y,arc_z)).T


    # Draw Orbit and Orbit Centers
    orbit = go.Scatter3d(x=pos[:,0], 
                         y=pos[:,1],
                         z=pos[:,2], mode='lines', name="Reference Orbit \ni = 0°",
                         line=dict(width=4,color='grey',dash='dashdot'),hoverinfo='text'
    )
    orbit_rot = go.Scatter3d(x=pos_rot[:,0], 
                             y=pos_rot[:,1],
                             z=pos_rot[:,2], mode='lines', 
                             name="Inclination = {:.1f}°".format(inclination_angle),
                             line=dict(width=4,color='red')
    )

    # Add Central Body as Point Mass
    center = go.Scatter3d(x=[0,0], 
                          y=[0,0],
                          z=[0,0], mode='markers', name = "Centeral Body",
                          marker=dict(size=12,color='black'),showlegend=False
    )

    # Draw Angular Momentum and Arc from z to h
    angular_momentum_vector = go.Scatter3d(x=[0,angular_momentum[0]],
                                           y=[0,angular_momentum[1]],
                                           z=[0,angular_momentum[2]],
                                           mode="lines+text",
                                           line=dict(width=5,color='orange'),
                                           showlegend=False,text=["", "h"],
                                           textposition="top center",hoverinfo='text'
    )
    # Hack to get arrows:
    # https://stackoverflow.com/questions/66789390/draw-an-arrow-between-two-specific-points-in-a-scatter-plot-with-plotly-graph-ob
    arrow_tip_ratio = 0.4
    arrow_starting_ratio = 0.99
    angular_momentum_arrow = go.Cone(x=[0 + arrow_starting_ratio*(angular_momentum[0] - 0)],
                                     y=[0 + arrow_starting_ratio*(angular_momentum[1] - 0)],
                                     z=[0 + arrow_starting_ratio*(angular_momentum[2] - 0)],
                                     u=[arrow_tip_ratio*(angular_momentum[0] - 0)],
                                     v=[arrow_tip_ratio*(angular_momentum[1] - 0)],
                                     w=[arrow_tip_ratio*(angular_momentum[2] - 0)],
                                     showlegend=False,
                                     showscale=False,
                                     colorscale=[[0, 'orange'], [1, 'orange']]
    )
    draw_arc = go.Scatter3d(x=arc[:,0], 
                            y=arc[:,1],
                            z=arc[:,2], 
                            mode='lines+text', 
                            name="e = {}".format(e),
                            text=[""]*int(len(arc_z)/2)+["i"],
                            textposition="top center",
                            line=dict(width=4,color='blue'),
                            hoverinfo='text',showlegend=False
    )

    # Draw Reference Planes
    equator_plane = go.Mesh3d(x=points[:,0],y=points[:,1],z=points[:,2],
                              opacity=0.5,
                              color='lightblue',
                              text="Equatorial Plane",
                              hoverinfo="text")

    lower_plane = go.Mesh3d(x=points[:,0],y=points[:,1],z=points[:,2]-5,
                            opacity=0.5,
                            color='lightgrey',
                            hoverinfo='text')

    # Draw Reference Axes
    axes_x = go.Scatter3d(x=[0,axes[0,0]],y=[0,axes[0,1]],z=[0,axes[0,2]],
                          mode="lines+text",
                          line=dict(width=4,color='grey'),
                          showlegend=False,text=["", "X Axis"],
                          textposition="bottom center",hoverinfo='text'
    )
    axes_y = go.Scatter3d(x=[0,axes[1,0]],y=[0,axes[1,1]],z=[0,axes[1,2]],
                          mode="lines+text",
                          line=dict(width=4,color='grey'),
                          showlegend=False,text=["", "Y Axis"],
                          textposition="bottom center",hoverinfo='text'
    )
    axes_z = go.Scatter3d(x=[0,axes[2,0]],y=[0,axes[2,1]],z=[0,axes[2,2]],
                          mode="lines+text",
                          line=dict(width=4,color='black'),
                          showlegend=False,text=["", "Z Axis"],
                          textposition="bottom right",hoverinfo='text'
    )


    # Define Figure and Add Drawings
    fig = go.Figure()
    fig.add_trace(orbit)
    fig.add_trace(orbit_rot)
    fig.add_trace(center)
    fig.add_trace(angular_momentum_vector)
    fig.add_trace(angular_momentum_arrow)
    fig.add_trace(draw_arc)
    fig.add_trace(equator_plane)
    fig.add_trace(lower_plane)
    fig.add_trace(axes_x)
    fig.add_trace(axes_y)
    fig.add_trace(axes_z)

    # Set Viewing Angle
    camera = dict(eye=dict(x=0.8, y=0.8, z=0.2))

    # Update Figure
    fig.update_layout(scene = dict(camera = camera,
                                   xaxis = dict(nticks=4, range=[-plane_size-3,plane_size-3],
                                                   showgrid=False,visible=False,zeroline=False),
                                   yaxis = dict(nticks=4, range=[-plane_size,plane_size],
                                                   showgrid=False,visible=False,zeroline=False),
                                   zaxis = dict(nticks=4, range=[-plane_size,plane_size],
                                                   showgrid=False,zeroline=False,visible=False),
                                   aspectmode='cube'),
                      margin=dict(r=10, l=10, b=1, t=10),
                      legend=dict(orientation="h",yanchor="bottom"),
                      title={'text': "<b>Elliptical Orbit: Inclination (i) Change<b>",
                              'y':0.95,
                              'x':0.5,
                              'xanchor': 'center',
                              'yanchor': 'top'},
    )


    return fig
