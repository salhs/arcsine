def last_time(times, trajectory, a, b):
    """
    Args:
        times (list or array): list/array of times from Gillespie algorithm
        trajectory (list or array): list/array of trajectory values from Gillespie algorithm
        a (float): slope
        b (float): intercept

    Returns:
        time_over (list): list of time intervals the trajectory is above the average
        t2 (float): fraction of time until a trajectory crosses the average for the last time
    """
    
    imax = len(times)
    i=2
    last_time = 0
    
    while i < imax:
        # solve for where trajectory intersects average
        t_intersect = (trajectory[-i]-b) / a
        
        # check if that time is within the interval of the trajectory values
        # if it is, that is the last time the trajectory crosses the average
        if times[-i] <= t_intersect <= times[-i+1]:
            last_time = t_intersect
            break
        # otherwise keep moving backwards through the trajectory
        else:
            i += 1
    
    t2 = last_time/times[-1] # fraction of time until crosses trajectory for the last time
    
    return last_time, t2