from time_over import time_over
from last_time import last_time
from max_time import max_time

def get_prob_distr(runs, times, trajs, a, b, which_t):
    """
    Args:
        runs (int): number of simulated trajectories
        times (dict): dictionary of list of times of simulated trajectories
        trajs (dict): dictionary of list of simulated trajectory values
        a (float): slope from best fit of average trajectory
        b (float): intercept from best fit of average trajectory
        which_t (int): {1 = computes T1, 2 = computes T2, 3 = computes T3}

    Returns:
        t_vals: list of T values for each trajectory
    """
    
    if which_t == 1:
        t_vals = []
        for x in range(runs):
            timeover, t1 = time_over(times[str(x)], trajs[str(x)], a, b)
            t_vals.append(t1)
        return t_vals
    elif which_t == 2:
        t_vals = []
        for x in range(runs):
            lasttime, t2 = last_time(times[str(x)], trajs[str(x)], a, b)
            t_vals.append(t2)
        return t_vals
    elif which_t == 3:
        t_vals = []
        for x in range(runs):
            maxtime, t3 = max_time(times[str(x)], trajs[str(x)], a, b)
            t_vals.append(t3)
        return t_vals