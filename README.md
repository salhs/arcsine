# Arcsine Laws in Stochastic Systems
Repo for a rotation project in the Biological Complexity Unit.
Arcsine laws for T1, T2, and T3 as defined in [Arcsine Laws in Stochastic Thermodynamics](https://arxiv.org/abs/1712.00795) for a model of ATP hydrolysis by myosin, a colloidal particle, and a minimal biochemical engine from [A Minimal Model for Carnot Efficiency at Maximum Power](https://arxiv.org/pdf/2312.02323).

Repo directory:
- **engine_sim.py** - Simulation of stochastic work and heat for the biochemical engine via Gillespie algorithm
- **atp_hydrolysis_sim.py** - Simulation of stochastic work and heat for myosin model via Gillespie algorithm
- **colloidal_sim.py** - Simulation of the position trajectory for the colloidal particle via numerical evolution of Langevin equation
- **trajectory_avg.py** - Compute average trajectory from simulated trajectories
- **get_prob_distr.py** - Compute T1, T2, and T3 values for trajectories
- **time_over.py** - Compute T1 for a trajectory
- **last_time.py** - Compute T2 for a trajectory
- **max_time.py** - Compute T3 for a trajectory
- **t_distr.py** - Script to run the numerical scheme from start to finish. Returns the T distribution for a given model.
- **ksstat.py** - Compute the Kolmogorov-Smirnov statistic for a given T distribution
  
- **convert_trajectory.py** - Discretise trajectories in time obtained from Gillespie algorithm. This is only used for illustrative purposes.
- **run_data.py** - Script to run the scheme for various parameter values for each model. Computed on a cluster.
- **run_data_engine_eh.py** - Same as above, but for various values of the high energy state in the biochemical engine model.
- **run_data_engine_s.py** - Same as above, for various values of the entropy between the two states in the engine model.  
  
- **ksplots.ipynb** - Jupyter notebook to generate the KS statistic and CDF comparison plots   
- **plots.ipynb** - Jupyter notebook to generate example plots for the definitions of T1, T2, and T3  
   
Each run of `t_distr.py` saves the following .pkl files:  
- `filename_trajs_time` - dictionary of transition times obtained from Gillespie algorithm  
- `filename_trajs_heat` - dictionary of stochastic heat trajectories  
- `filename_trajs_work` - dictionary of stochastic work trajectories  
- `filename_trajs_post` - dictionary of position trajectories  
- `filename_avgtrajs_time` - average trajectory times  
- `filename_avgtrajs_heat` - average stochastic heat trajectory  
- `filename_avgtrajs_work` - average stochastic work trajectory  
- `filename_avgtrajs_post` - average position trajectory  
- `filename_fitparams` - slope and intercept values from line of best fit  
- `filename_tvals` - values for T1, T2, and T3 for each trajectory simulation, i.e. the data for a histogram of T values 

