import numpy as np
import os
from t_distr import t_distr

# fixing the values for the engine for now
s = np.log(100) # entropy difference
e_c = 1 # units of k_B T
e_h = 5

init_state = 0 # starting in state U

runs = 1000
tmax = [100, 250, 500, 750, 1000] # units of s

# run each simulation for 5 different t_f to compare resulting K-S statistic behaivour
for max in tmax:
    energies = np.array([e_c, e_h]) # units of k_B T
    
    k_h_plus = 1 # units of s^-1
    k_h_minus = k_h_plus * np.exp(e_h - s)
    k_c_plus = 2
    k_c_minus = k_c_plus * np.exp(e_c - s)

    rates = np.array([k_h_plus, k_h_minus, k_c_plus, k_c_minus])

    drives = np.array([
        [0, -25.5, 0, 0],
        [25.5, 0, 0, 0],
        [0, 0, 0, -e_h+e_c],
        [0, 0, e_h-e_c, 0]
    ]) # units of k_B T
    
    filename1 = 'data_myosin_tmax' + str(max)
    filename2 = 'data_engine_tmax' + str(max)
    filename3 = 'data_colloidal_tmax' + str(max)
    os.makedirs(filename1)
    os.makedirs(filename2)
    os.makedirs(filename3)

    t_distr("myosin", [], [], [], 0, runs, max, filename1)
    t_distr("engine", energies, drives, rates, init_state, runs, max, filename2)
    t_distr("colloidal", [], [], [], 0, runs, max, filename3)