""" --------------------------------------------------------------------------
            Example of Calculating and Plotting Orbit Argument of Periapsis (ω)
            for the Two Body Problem

            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import numpy as np
from numpy.linalg import norm
import plotly.graph_objects as go
from scipy.spatial.transform import Rotation as R

def plot():

    # Orbit Angle Defintions
    inclination_angle = 50 # degrees
    long_ascend_node_angle = 60 # degrees
    argument_peri_angle = 190 # degrees
    r = R.from_euler('zyz', [argument_peri_angle,inclination_angle,long_ascend_node_angle], 
                    degrees=True)
    rotation = r.as_matrix()

    # Set Equatorial Plane shape
    plane_size = 8
    points = np.array([[ plane_size,    plane_size, 0],
                       [-plane_size,  plane_size, 0],
                       [ plane_size,   -plane_size, 0],
                       [-plane_size, -plane_size, 0]])

    # Establish Central Body Reference Axis
    axes_scale = 2
    node_scale = 2.45 # For figure use only
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
    eccentricy = rotation @ np.array([r_p,0,0]) # This becomes vector direction of eccentricity

    # Angular Momentum
    h_scale = 2
    angular_momentum = h_scale*(np.cross(eccentricy,p_rot_vector)/norm(np.cross(eccentricy,p_rot_vector)))

    # Ascending Node Vector 
    node_vec = np.cross([0,0,1],angular_momentum)

    # Longitude of Ascending Node (Ω)
    long_ascend_node = np.arccos(np.dot([1,0,0],node_vec)/norm(node_vec))
    if node_vec[1] >= 0.0:
        lan = np.degrees(norm(long_ascend_node))
    elif node_vec[1] < 0.0:
        lan = np.degrees(2*np.pi - norm(long_ascend_node))

    # Argument of Periapsis (ω)
    argument_perigee = np.arccos(np.dot(node_vec,eccentricy) / 
                                (norm(eccentricy)*norm(node_vec)))
    # Check ecc_zcomp
    if eccentricy[-1] < 0:
        argument_perigee = np.degrees(2*np.pi - argument_perigee)
    else:
        argument_perigee = np.degrees(argument_perigee)

    # Calc Inclination Angle Arc
    arc_x = np.cos(np.radians(lan)-np.pi/2)*np.sin(np.linspace(0,np.radians(inclination_angle),100))
    arc_y = np.sin(np.radians(lan)-np.pi/2)*np.sin(np.linspace(0,np.radians(inclination_angle),100))
    arc_z = np.cos(np.linspace(0,np.radians(inclination_angle),100))
    arc = np.vstack((arc_x,arc_y,arc_z)).T

    # Calc Longitude of Ascending Node Arc
    arc_lan_x = np.cos(np.linspace(0,np.radians(lan),100))
    arc_lan_y = np.sin(np.linspace(0,np.radians(lan),100))
    arc_lan_z = np.zeros(100)
    arc_lan = np.vstack((arc_lan_x,arc_lan_y,arc_lan_z)).T

    # Calc Arugment of Periapsis Arc
    ap_rot = R.from_euler('yz', [inclination_angle,long_ascend_node_angle], 
                          degrees=True).as_matrix()
    arc_ap_x = np.cos(np.linspace(0,np.radians(argument_perigee),100)+np.pi/2)
    arc_ap_y = np.sin(np.linspace(0,np.radians(argument_perigee),100)+np.pi/2)
    arc_ap_z = np.zeros(100)
    arc_ap = (ap_rot @ np.vstack((arc_ap_x,arc_ap_y,arc_ap_z))).T

    # Draw Orbit and Orbit Centers
    orbit = go.Scatter3d(x=pos[:,0], 
                         y=pos[:,1],
                         z=pos[:,2], mode='lines', name="Reference Orbit",
                         line=dict(width=4,color='grey',dash='dashdot'),hoverinfo='text'
    )
    orbit_rot = go.Scatter3d(x=pos_rot[:,0], 
                             y=pos_rot[:,1],
                             z=pos_rot[:,2], mode='lines', 
                             name="Inclination = {:.1f}°, Ω = {:.1f}° & ω = {:.1f}°".format(inclination_angle,lan, argument_perigee),
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
    draw_incl_arc = go.Scatter3d(x=arc[:,0], 
                                 y=arc[:,1],
                                 z=arc[:,2], 
                                 mode='lines+text', 
                                 name="e = {}".format(e),
                                 text=[""]*int(len(arc_z)/2)+["i"],
                                 textposition="top center",
                                 line=dict(width=4,color='orange'),
                                 hoverinfo='text',showlegend=False
    )
    draw_lan_arc = go.Scatter3d(x=arc_lan[:,0], 
                                y=arc_lan[:,1],
                                z=arc_lan[:,2], 
                                mode='lines+text', 
                                name="e = {}".format(e),
                                text=[""]*int(len(arc_z)*3/4)+["Ω"],
                                textposition="middle right",
                                line=dict(width=4,color='green'),
                                hoverinfo='text',showlegend=False
    )
    draw_ap_arc = go.Scatter3d(x=arc_ap[:,0], 
                               y=arc_ap[:,1],
                               z=arc_ap[:,2], 
                               mode='lines+text', 
                               name="e = {}".format(e),
                               text=[""]*int(len(arc_z)*3/4)+["ω"],
                               textposition="middle right",
                               line=dict(width=4,color='blue'),
                               hoverinfo='text',showlegend=False
    )

    # Draw Reference Planes
    equator_plane = go.Mesh3d(x=points[:,0],y=points[:,1],z=points[:,2],
                              opacity=0.5,
                              color='lightblue',
                              text="Equatorial Plane",
                              hoverinfo="text")

    lower_plane = go.Mesh3d(x=points[:,0],y=points[:,1],z=points[:,2]-6,
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
                          mode="lines", # Removing Text (too busy)
                          line=dict(width=4,color='black'),
                          showlegend=False,text=["", "Z Axis"],
                          textposition="bottom right",hoverinfo='text'
    )

    # Draw Eccentricity Vector
    arg_peri = go.Scatter3d(x=[0,eccentricy[0]],
                            y=[0,eccentricy[1]],
                            z=[0,eccentricy[2]],
                            mode="lines+text",
                            line=dict(width=4,color='blue'),
                            showlegend=False,text=["", "Periapsis"],
                            textposition="top center",hoverinfo='text'
    )
    # Draw Node Vector
    node = go.Scatter3d(x=[0,node_vec[0]*node_scale],
                        y=[0,node_vec[1]*node_scale],
                        z=[0,node_vec[2]*node_scale],
                        mode="lines+text",
                        line=dict(width=4,color='green'),
                        showlegend=False,text=["", "Ascending Node"],
                        textposition="bottom center",hoverinfo='text'
    )
    node_tip_ratio = 0.1
    node_starting_ratio = 0.99
    node_arrow = go.Cone(x=[0 + node_starting_ratio*(node_vec[0]*node_scale - 0)],
                         y=[0 + node_starting_ratio*(node_vec[1]*node_scale - 0)],
                         z=[0 + node_starting_ratio*(node_vec[2]*node_scale - 0)],
                         u=[node_tip_ratio*(node_vec[0]*node_scale - 0)],
                         v=[node_tip_ratio*(node_vec[1]*node_scale - 0)],
                         w=[node_tip_ratio*(node_vec[2]*node_scale - 0)],
                         showlegend=False,
                         showscale=False,
                         colorscale=[[0, 'green'], [1, 'green']]
    )

    # Define Figure and Add Drawings
    fig = go.Figure()
    fig.add_trace(orbit)
    fig.add_trace(orbit_rot)
    fig.add_trace(center)
    fig.add_trace(angular_momentum_vector)
    fig.add_trace(angular_momentum_arrow)
    fig.add_trace(draw_incl_arc)
    fig.add_trace(draw_lan_arc)
    fig.add_trace(draw_ap_arc)
    fig.add_trace(equator_plane)
    fig.add_trace(lower_plane)
    fig.add_trace(axes_x)
    fig.add_trace(axes_y)
    fig.add_trace(axes_z)
    fig.add_trace(node)
    fig.add_trace(node_arrow)
    fig.add_trace(arg_peri)

    # Set Viewing Angle
    camera = dict(eye=dict(x=-0.4, y=0.8, z=0.2))

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
                    title={'text': "<b>Elliptical Orbit: Argument of Periapsis (ω) Change<b>",
                            'y':0.95,
                            'x':0.5,
                            'xanchor': 'center',
                            'yanchor': 'top'},
    )

    return fig
