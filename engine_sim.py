import math
import random

def expran():
    """Generate random numbers from an exponential distribution"""
    return -math.log(random.random())

def engine_sim(energies, drives, rates, init_state, tmax):
    """
    state 0 = state U
    state 1 = state V
    Given system parameters, simulates stochastic heat and work for
    biochemical engine model via the Gillespie algorithm
    """
    
    k_h_plus = rates[0]
    k_h_minus = rates[1]
    k_c_plus = rates[2]
    k_c_minus = rates[3]
    
    t=0.0
    w=0.0
    q=0.0
    state = init_state
    
    dts = []
    time = []
    work = []
    heat = []
    
    # probability of leaving state U
    kout_U_ATP = k_c_plus
    kout_U_spont = k_h_plus
    kout_U = kout_U_ATP + kout_U_spont
    
    # probability of leaving state V
    kout_V_ATP = k_c_minus
    kout_V_spont = k_h_minus
    kout_V = kout_V_ATP + kout_V_spont

    while t < tmax:
        
        if state == 0:
            kout = kout_U
        elif state ==1:
            kout = kout_V
        
        # advance the time
        dt = expran()*(1/kout)
        dts.append(dt)
        t += dt
        
        # cumulants
        if state == 0:
            trans_prob = kout_U_ATP/kout
        elif state == 1:
            trans_prob = kout_V_ATP/kout
            
        # determine which reaction occurs
        r = random.random()
        
        # if smaller, the ATP transition occurs
        if r < trans_prob:
            if state == 0:
                new_state = 1
                q += -energies[new_state] + energies[state] + drives[new_state, state]
                w += drives[new_state, state]
            elif state == 1:
                new_state = 0
                q += -energies[new_state] + energies[state] + drives[new_state, state]
                w += drives[new_state, state]
        # if larger, the spontaneous transition occurs        
        else:
            if state == 0:
                new_state = 1
                q += -energies[new_state] + energies[state] + drives[new_state+2, state+2]
                w += drives[new_state+2, state+2]
            elif state == 1:
                new_state = 0
                q += -energies[new_state] + energies[state] + drives[new_state+2, state+2]
                w += drives[new_state+2, state+2]

        state = new_state
        time.append(t)
        work.append(w)
        heat.append(q)
    
    return time, dts, heat, work