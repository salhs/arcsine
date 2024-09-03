import numpy as np

def best_fit(x, a, b):
    return a*x + b

def time_over(times, trajectory, a, b):
    """Given a list of times and trajectories from a simulation via Gillespie algorithm
    and the parameters of best fit for the corresponding trajectory average (assuming a linear fit)
    this function computes the fraction of time an individual trajectory is greater than its average

    Args:
        times (list or array): list/array of times from Gillespie algorithm
        trajectory (list or array): list/array of trajectory values from Gillespie algorithm
        a (float): slope
        b (float): intercept

    Returns:
        time_over (list): list of time intervals the trajectory is above the average
        t1 (float): fraction of time a trajectory is greater than its average
    """
    
    time_over = []
    imax = len(times)-1
    i=0
    t = times[0]
    traj = trajectory[0]
    
    # set the last time to the first time
    last_time = times[0]
    
    while i < imax:
        # if the first point is under the average
        if traj < best_fit(t, a, b):
            # continue incrementing i until find a point above the average
            while traj < best_fit(times[i], a, b) and i < imax:
                i += 1
                t = times[i]
                traj = trajectory[i]
            # and replace the last time with the new one
            last_time = times[i]
        else:
            # else if the first point is over the average
            # the last time is the first time
            # keep incrementing by 1 time step until the current is below the average
            while traj > best_fit(t, a, b) and i < imax:
                i += 1
                t = times[i]
                traj = trajectory[i]

            # when the current hits a value below average
            # append the time interval over which the current was above average to time_over
            time_over.append(t-last_time)
    
    t1 = np.sum(time_over)/times[-1] # fraction of time current above average
    
    return time_over, t1