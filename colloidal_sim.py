import random
import numpy as np

def gasdev():
    """Generate random numbers from a gaussian distribution"""
    r1 = random.random()
    r2 = random.random()

    g1 = np.sqrt(-2 * np.log(r1)) * np.cos(2 * np.pi * r2)
    g2 = np.sqrt(-2 * np.log(r1)) * np.sin(2 * np.pi * r2)
    
    return g1

def colloidal_sim(xinit, dt, tmax):
    """
    Numerical simulation of the Langevin equation for a set
    periodic energy potential
    """
    x=xinit
    t=0.0
    
    traj_t=[t]
    traj_x=[x]
    dts = []
    
    i=0
    
    while t < tmax:
        modx = traj_x[i] % 1
        if modx <= 1/3:
            x = traj_x[i] - dt + np.sqrt(2) * gasdev() * np.sqrt(dt)
        elif modx > 1/3:
            x = traj_x[i] + 3.5 * dt + np.sqrt(2) * gasdev() * np.sqrt(dt)
        
        t = traj_t[i] + dt
        
        i+=1
        
        dts.append(dt)
        traj_x.append(x)
        traj_t.append(t)

    return traj_t, dts, traj_x