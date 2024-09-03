import math
import random
import numpy as np

def expran():
    """Generate random numbers from an exponential distribution"""
    return -math.log(random.random())

def sto_heat(current, target):
    """Return the stochastic heat from a given transition"""
    energies = np.array([0, -19.0, 4.0, -2.0]) # units of k_B T
    drive = np.array([
        [0, 0, 0, 0], 
        [0, 0, -25.5, 0],
        [0, 25.5, 0, 0],
        [0, 0, 0, 0]]) # units of k_B T
    return -energies[target] + energies[current] + drive[target, current]

def sto_work(current, target):
    """Return the stochastic work from a given transition"""
    drive = np.array([
        [0, 0, 0, 0], 
        [0, 0, -25.5, 0],
        [0, 25.5, 0, 0],
        [0, 0, 0, 0]]) # units of k_B T
    return drive[target, current]

def atp_hydrolysis_sim(init_state, tmax):
    """
    System parameters have been set. Simulates trajectories for 
    stochastic heat and work via the Gillespie algorithm
    """
    rates = np.array([
        [0, 0.0001, 0, 2.0],
        [20000.0, 0, 10.0, 0],
        [0, 100.0, 0, 0.0002],
        [15.0, 0, 0.1, 0]]) # units of s^-1
    
    t=0.0
    w=0.0
    q=0.0
    state = init_state
    
    dts = []
    time = []
    work = []
    heat = []
    
    while(t < tmax):
        
        # total probability of leaving the state
        if state == 0:
            kout = rates[1,0] + rates[3,0]
        elif state == 1:
            kout = rates[0,1] + rates[2,1]
        elif state == 2:
            kout = rates[1,2] + rates[3,2]
        elif state == 3:
            kout = rates[0,3] + rates[2,3]
        
        # advance the time
        dt = expran()*(1/kout)
        dts.append(dt)
        t += dt
        
        # cumulants are [k_xy/k_out, (k_xy+k_zy)/k_out] but the second term is unnecessary
        if state == 0:
            trans_prob = rates[1,0]/kout
        elif state == 1:
            trans_prob = rates[0,1]/kout
        elif state == 2:
            trans_prob = rates[1,2]/kout
        elif state == 3:
            trans_prob = rates[0,3]/kout
        
        rand = random.random()
        
        if rand < trans_prob:
            if state == 0:
                new_state = 1
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 1:
                new_state = 0
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 2:
                new_state = 1
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 3:
                new_state = 0
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
        else:
            if state == 0:
                new_state = 3
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 1:
                new_state = 2
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 2:
                new_state = 3
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            elif state == 3:
                new_state = 2
                q += sto_heat(state, new_state)
                w += sto_work(state, new_state)
            
        state = new_state
        time.append(t)
        work.append(w)
        heat.append(q)
        
    return time, dts, heat, work