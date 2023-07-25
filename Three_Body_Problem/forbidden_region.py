""" --------------------------------------------------------------------------
            Circular Planar Restricted Three-Body Problem: 
                    Functions for calculating zero-velocity or forbidden
                    regions for a given non-dimensional system defined 
                    by its mass ratio
                                                                        
            Copyright (c) Eduardo Ocampo, All Rights Reserved               
            https://www.github.com/thatguyeddieo                            
-------------------------------------------------------------------------- """

import numpy as np

def forbidden_region(jacobi_max,mass_ratio,x_range=[-1.5,1.5],y_range=[-1.5,1.5],
                     linspace_num=200):
    """
    Forbidden region is defined as the region greater than the jacobi_max
    parameter passed in. Assumes a Non-Dimensional system. Sets a default
    region and meshgrid spacing if needed.

    Returns the x-y range of meshgrid space generated using x_range & y_range,
    and the "Forbidden Region". 

    """    
    
    x_min, x_max = x_range
    y_min, y_max = y_range
    
    x_vals = np.linspace(x_min,x_max,linspace_num)
    y_vals = np.linspace(y_min,y_max,linspace_num)

    [X,Y] = np.meshgrid(x_vals,y_vals)

    r1 = np.sqrt((X+mass_ratio)**2+Y**2)
    r2 = np.sqrt((X-1+mass_ratio)**2+Y**2)

    jc = X**2 + Y**2 + 2*(1-mass_ratio)/r1 + 2*mass_ratio/r2
    jc[jc>jacobi_max] = np.nan

    return x_vals, y_vals, jc

def get_jacobi_velocity(x,y,jacobi,mass_ratio):
    """
    For a given Jacobi Constant and x-y coordinate in space, 
    returns the max velocity magnitude associated with that 
    Jacobi Constant.
    
    """
    
    r1 = np.sqrt((x+mass_ratio)**2+y**2)
    r2 = np.sqrt((x-1+mass_ratio)**2+y**2)

    vel_mag = np.sqrt(((x**2 + y**2) + 2*(1-mass_ratio)/r1 + 2*mass_ratio/r2) - jacobi)

    return vel_mag
