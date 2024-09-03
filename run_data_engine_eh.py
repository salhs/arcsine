import numpy as np
import os
from t_distr import t_distr

# values for the engine
s = [5, 10, 20, 40, 80] #np.log(n_v/n_u)=np.log(100)
e_c = 1 # units of k_B T
e_h = [6] #5

init_state = 0 # starting in state U

runs = 1000
tmax = [100, 250, 500, 750, 1000]

for e_hval in e_h:
    sval = np.log(100)
    directory = 'data_slog100_eh' + str(e_hval)
    os.makedirs(directory)
    for max in tmax:
        energies = np.array([e_c, e_hval]) # units of k_B T

        # favouring the ATP based reaction
        k_h_plus = 1 # units of s^-1
        k_h_minus = k_h_plus * np.exp(e_hval - sval)
        k_c_plus = 2
        k_c_minus = k_c_plus * np.exp(e_c - sval)

        rates = np.array([k_h_plus, k_h_minus, k_c_plus, k_c_minus])

        drives = np.array([
            [0, -25.5, 0, 0],
            [25.5, 0, 0, 0],
            [0, 0, 0, -e_hval+e_c],
            [0, 0, e_hval-e_c, 0]
        ]) # units of k_B T
        
        t_distr("engine", energies, drives, rates, init_state, runs, max, directory)