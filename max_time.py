import numpy as np

def best_fit(x, a, b):
    return a*x + b

def max_time(times, trajectory, a, b):
    """
    Args:
        times (list or array): list/array of times from Gillespie algorithm
        trajectory (list or array): list/array of trajectory values from Gillespie algorithm
        a (float): slope
        b (float): intercept

    Returns:
        time_over (list): list of time intervals the trajectory is above the average
        t3 (float): fraction of time until a trajectory reaches its max deviation from the average
    """
    
    differences = []
    
    for x in range(len(trajectory)):
        differences.append(np.abs( trajectory[x] - best_fit(times[x],a,b) ))
        
    # choose the first/smallest time which reach max deviation
    location = np.where(differences == np.max(differences))[0][0]
    max_time = times[location]
    
    t3 = max_time/times[-1] # fraction of time until crosses trajectory for the last time
    
    return max_time, t3