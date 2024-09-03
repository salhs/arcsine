from engine_sim import engine_sim
from atp_hydrolysis_sim import atp_hydrolysis_sim
from colloidal_sim import colloidal_sim
import numpy as np

def trajectory_avg(model, energies, drives, rates, init_state: int, runs: int, tmax: float):
    """
    Args:
        model (string) = "myosin", "engine", "colloidal"
        
        Corresponding to the engine model, otherwise leave empty:
        energies (array or list) = energy of U and V states
        drives (array) = external driving from ATP hydrolysis. columns = current state, rows = target state
        rates (array or list) =  transition rates for the forward and reverse reaction paths between U and V
        
        init_state (int or float):
            myosin: {0: unbound myosin, 1: ATP bound, 2: ADP+P bound, 3: ADP bound}
            engine: {0: U state, 1: V state}
            colloidal: x position
            
        runs (int): the number of times you'd like to generate a trajectory for stochastic work and heat
        tmax (float): the maximum time you'd like to evolve until

    Returns:
        runs_time = trajectory times
        runs_heat = stochastic heat trajectories
        runs_work = stochastic work trajectories
        runs_post = colloidal particle trajectories
        time = average trajectory time
        avg_heat = average stochastic heat trajectory
        avg_work = average stochastic work trajectory
        avg_post = average position trajectory
    """
    
    # initialise dictionaries
    runs_time = {}
    runs_heat = {}
    runs_work = {}
    runs_post = {}
    
    # populate dictionaries with trajectory simulations
    i=0
    while i < runs:
        if model == "myosin":
            time, dts, heat, work = atp_hydrolysis_sim(init_state, tmax)
            runs_heat[str(i)] = heat
            runs_work[str(i)] = work
            runs_time[str(i)] = time
        elif model == "engine":
            time, dts, heat, work = engine_sim(energies, drives, rates, init_state, tmax)
            runs_heat[str(i)] = heat
            runs_work[str(i)] = work
            runs_time[str(i)] = time
        elif model == "colloidal":
            time, dts, position = colloidal_sim(init_state, 0.01, tmax)
            runs_post[str(i)] = position
            runs_time[str(i)] = time
        i += 1
        
    # initialise data for average trajectory
    avg_heat = []
    avg_work = []
    avg_post = []
    time = []
    step = np.full(runs,0)

    # find length of the trajectory with the shortest number of steps
    min_len = [len(runs_time[str(min_l)]) for min_l in range(runs)]
    
    # while the largest step value is less than the length of the shortest trajectory
    while np.max(step) < np.min(min_len):
        # find the trajectory at the smallest time
        findmin = [runs_time[str(key)][s] for key, s in zip(range(runs),step)]   
        mintimes = np.where(findmin==np.min(findmin))[0]
        
        if model == "engine" or model== "myosin":
            # get the average between the trajectories for that time interval for heat
            getavg_heat = [runs_heat[str(key)][s] for key, s in zip(range(runs),step)]

            # get the average between the trajectories for that time interval for heat
            getavg_work = [runs_work[str(key)][s] for key, s in zip(range(runs),step)]

            # append averages and corresponding time
            avg_heat.append(np.mean(getavg_heat))
            avg_work.append(np.mean(getavg_work))
            
        elif model == "colloidal":
            # get the average between the trajectories for that time interval for position
            getavg_post = [runs_post[str(key)][s] for key, s in zip(range(runs),step)]
            avg_post.append(np.mean(getavg_post))
            
        time.append(np.min(findmin))
        
        # update the new step positions
        for mint in mintimes:
            step[mint] += 1
        
    return runs_time, runs_heat, runs_work, runs_post, time, avg_heat, avg_work, avg_post