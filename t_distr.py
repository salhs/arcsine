import numpy as np
import pickle
from trajectory_avg import trajectory_avg
from get_prob_distr import get_prob_distr

def cumulative_distr(t):
    """Analytical CDF"""
    return 2/np.pi * np.arcsin(np.sqrt(t))

def prob_distr(t):
    """Analytical PDF"""
    return 1/np.pi * 1/(np.sqrt(t * (1-t)))

def t_distr(model, energies, drives, rates, init_state, runs, tmax, directory):
    """Returns lists of all T values for simulated trajectories for a given model and saves the data in the specified directory"""
    
    print("Beginning computing trajectory average for "+model)
    
    runs_time, runs_heat, runs_work, runs_post, time, avg_heat, avg_work, avg_post = trajectory_avg(model, energies, drives, rates, init_state, runs, tmax)
    
    print("Successfully completed computing trajectory average")
    
    if model == "engine" or model == "myosin":
        slope_heat, intercept_heat = np.polyfit(time, avg_heat, 1)
        slope_work, intercept_work = np.polyfit(time, avg_work, 1)
    
        print("Beginning computing T1 values")
        t1_work = np.array(get_prob_distr(runs, runs_time, runs_work, slope_work, intercept_work, 1))
        t1_heat = np.array(get_prob_distr(runs, runs_time, runs_heat, slope_heat, intercept_heat, 1))

        print("Beginning computing T2 values")
        t2_work = np.array(get_prob_distr(runs, runs_time, runs_work, slope_work, intercept_work, 2))
        t2_heat = np.array(get_prob_distr(runs, runs_time, runs_heat, slope_heat, intercept_heat, 2))

        print("Beginning computing T3 values")
        t3_work = np.array(get_prob_distr(runs, runs_time, runs_work, slope_work, intercept_work, 3))
        t3_heat = np.array(get_prob_distr(runs, runs_time, runs_heat, slope_heat, intercept_heat, 3))
        
        filename = "data_" + model + "_" + str(runs) + "runs_" + str(tmax) + "tmax"
    
        data1 = {"trajectories": [runs_time, runs_heat, runs_work]}
        filename1a = directory + "/" + filename + "_trajs_time.pkl"
        filename1b = directory + "/" + filename + "_trajs_heat.pkl"
        filename1c = directory + "/" + filename + "_trajs_work.pkl"
        with open(filename1a, 'wb') as f:
            pickle.dump(runs_time, f)
        with open(filename1b, 'wb') as f:
            pickle.dump(runs_heat, f)
        with open(filename1c, 'wb') as f:
            pickle.dump(runs_work, f)
            
        data2 = {"avg trajectories": [time, avg_heat, avg_work]}
        filename2a = directory + "/" + filename + "_avgtrajs_time.pkl"
        filename2b = directory + "/" + filename + "_avgtrajs_heat.pkl"
        filename2c = directory + "/" + filename + "_avgtrajs_work.pkl"
        with open(filename2a, 'wb') as f:
            pickle.dump(time, f)
        with open(filename2b, 'wb') as f:
            pickle.dump(avg_heat, f)
        with open(filename2c, 'wb') as f:
            pickle.dump(avg_work, f)

        data3 = {"fit params": [slope_heat, intercept_heat, slope_work, intercept_work]}
        filename3 = directory + "/" + filename + "_fitparams.pkl"
        with open(filename3, 'wb') as f:
            pickle.dump(data3, f)

        data4 = {"t vals": [t1_work, t1_heat, t2_work, t2_heat, t3_work, t3_heat]}
        filename4 = directory + "/" + filename + "_tvals.pkl"
        with open(filename4, 'wb') as f:
            pickle.dump(data4, f)

        print("Successfully wrote all data for "+model)
        
    elif model == "colloidal":
        slope_post, intercept_post = np.polyfit(time, avg_post, 1)
    
        print("Beginning computing T1 values")
        t1_post = np.array(get_prob_distr(runs, runs_time, runs_post, slope_post, intercept_post, 1))

        print("Beginning computing T2 values")
        t2_post = np.array(get_prob_distr(runs, runs_time, runs_post, slope_post, intercept_post, 2))

        print("Beginning computing T3 values")
        t3_post = np.array(get_prob_distr(runs, runs_time, runs_post, slope_post, intercept_post, 3))
        
        filename = "data_" + model + "_" + str(runs) + "runs_" + str(tmax) + "tmax"
    
        data1 = {"trajectories": [runs_time, runs_post]}
        filename1a = directory + "/" + filename + "_trajs_time.pkl"
        filename1d = directory + "/" + filename + "_trajs_post.pkl"
        with open(filename1a, 'wb') as f:
            pickle.dump(runs_time, f)
        with open(filename1d, 'wb') as f:
            pickle.dump(runs_post, f)

        data2 = {"avg trajectories": [time, avg_post]}
        filename2a = directory + "/" + filename + "_avgtrajs_time.pkl"
        filename2d = directory + "/" + filename + "_avgtrajs_post.pkl"
        with open(filename2a, 'wb') as f:
            pickle.dump(time, f)
        with open(filename2d, 'wb') as f:
            pickle.dump(avg_post, f)

        data3 = {"fit params": [slope_post, intercept_post]}
        filename3 = directory + "/" + filename + "_fitparams.pkl"
        with open(filename3, 'wb') as f:
            pickle.dump(data3, f)

        data4 = {"t vals": [t1_post, t2_post, t3_post]}
        filename4 = directory + "/" + filename + "_tvals.pkl"
        with open(filename4, 'wb') as f:
            pickle.dump(data4, f)

        print("Successfully wrote all data for "+model)
    
    return data1, data2, data3, data4