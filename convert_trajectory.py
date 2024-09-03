import numpy as np

# this is highly inefficient code because 
# for each time point it also needs to check *every previous* interval in the trajectory times

def convert_trajectory(dt, times, dts, points):
    
    check = np.min(dts)
    if check < dt:
        print("please choose a dt at least as small as the smallest trajectory dt")
        
    # sets the new evenly spaced list of times
    new_t = np.arange(times[0],times[-1],dt)
    
    data = []
    for x in new_t:
        for y in range(len(times)):
            # if the time is equal to a trajectory time, append the corresponding trajectory point
            if x == times[y]:
                data.append(points[y])
            # otherwise check if the time is between two trajectory times
            # if it is, append the point corresponding to the earlier point
            elif times[y] < x < times[y+1]:
                data.append(points[y])
    return new_t, data