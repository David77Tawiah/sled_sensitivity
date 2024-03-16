#sled_sensitivity.py
"""
Explores the space of parameters (coefficient of friction and applied force) in
a sled race to find out when the sled will or will not finish the race.
"""
# DO NOT MODIFY the given code and comments.
# Besides math, DO NOT import more modules beyond those already imported.


import matplotlib.pyplot as plt
import random


def get_trajectory(f, Fa, m, dt):
    """
    Returns the times and positions of the sled given the coefficient of
    friction, applied force, mass of the sled, and time step size.  The 
    applied force is constant for the first 75 meters and then changes to 0.  
    Simulation ends when the velocity of the sled reaches zero (or negative).
    
    Parameters:
        fi (float): coefficient of friction
        Fa (float): applied force in Newtons for first 75 meters
        m (float): mass in kg
        dt (float): timestep size in seconds
    Returns as a tuple:
        ts (list): times, each is a float, in seconds
        xs (list): positions, each is a float, in meters 
                   xs[i] is the position of the sled at time ts[i]
        
    If the sled does not move (e.g., due to a low applied force on a heavy 
    sled), then ts and xs are each a list of length 1 storing the initial time
    and position, both of which is 0.
    """
    g = 9.81  # acceleration due to gravity, m/s**2
    t = 0     # initial time, s
    x = 0     # initial position, m
    ts = [t]   # intial time list, s
    xs = [x]   # initial position list, m
    v = 0     # initial velocity at time 0
    F = m*f*g
    a = (Fa-F)/m
    if a>0:
        while v>=0 and xs[-1] <= 75:
            # estimate the times and positions of the sled up to 75 meters
            F = m*f*g
            a = (Fa-F)/m
            v = v + a*dt
            x = x + v*dt + (a*(dt**2))/2
            ts.append(t)
            xs.append(x)
            t+= dt
              
        while v>=0 and xs[-1]>75: 
            Fa = 0
            # estimate the times and postions of the sled after 75 meters 
            F = m*f*g
            a = (Fa-F)/m 
            v = v + a*dt
            x = x + v*dt + (a*(dt**2))/2
            ts.append(t)
            xs.append(x)
            t+= dt
            
            
    return (ts,xs)
    
def will_finish(f, Fa, m, dt):
    """
    Returns True if the sled will finish the 100 meter race given the 
    coefficient of friction, applied force, and mass; otherwise returns False.
    Parameters:
        f (float): coefficient of friction
        Fa (float): applied force in Newtons for first 75 meters
        m (float): mass in kg
        dt (float): timestep size in seconds
    Returns: (bool) True if the sled finishes the race; False otherwise
    """
    ts,xs= get_trajectory(f, Fa, m, dt)
    if  xs[-1] >= 100 :
        # sled will finish the 100 meter race
        return(True)  
    else:
        # sled will not finish 100 meter race
        return(False)
    


#### Script code
if __name__ == '__main__':
    # Code in this if-block executes only if this file is run as a script.
    # Code in this if-block will not execute if this module is imported.
    
    # Perform sensitivity analyses
    
    ######################################################################
    # Single-parameter analysis: effect of coefficient of friction
    # Constants
    dt= .5  # time step size in seconds
    Fa= 100  # applied force in Newtons
    m= 20  # mass of the sled in kg
    
    # Compute and plot trajectories for f = .2, .3, ..., .6
    f_lo= .2
    f_hi= .6 
    ### TODO: add your code below
    plt.figure(1)
    plt.axes()
    plt.xlabel('Time(seconds)')
    plt.ylabel('Postion(meters)')
    plt.title('Position vs Time')
    while f_lo<=f_hi:
        ts,xs = get_trajectory(f_lo, 100, 20, 0.5)
        labeltext = f'f={f_lo: .1f}'
        plt.plot(ts, xs, "o", label=labeltext)
        plt.legend()
        f_lo+=0.1









    ######################################################################
    # Two-parameter analysis: effect of coefficient of friction and applied force
    # Constants
    dt= .5  # time step size in seconds
    m = 20  # mass of the sled in kg 
    
    # Range of f and Fa to investigate
    f_lo= .05  # lowest coefficient of friction (Teflon)
    f_hi= .7  # highest coefficient of friction (rough asphalt)
    Fa_lo= 0    # lowest applied force in N
    Fa_hi= 200  # highest applied force in N
    
    # Randomly sample the parameter space of friction coefficient and applied 
    # force.  Each sample is one randomly generated f value and one randomly 
    # generated Fa value.  Draw each sample as a point on the graph, using 
    # color to indicate whether or not that sample (pair of parameter values) 
    # result in the sled finishing the race. 
    n= 10000
    plt.figure(2)
    plt.axes()
    plt.xlabel('Coefficient of Friction')
    plt.ylabel('Applied Force(N)')
    plt.title('Does the sled finish the race')
    for k in range (n):
        f = random.uniform(0.05, 0.7)
        Fa = random.uniform(0, 200) 
        check= will_finish(f, Fa, m, dt)
        if check == True:
            f_yes = [f]
            Fa_yes = [Fa]
            plt.plot(f_yes, Fa_yes, 'b*')
        else:
            f_no = [f]
            Fa_no = [Fa]
            plt.plot(f_no, Fa_no, 'r*')
    labeltext1  = 'Yes'       
    plt.plot(f_yes[0], Fa_yes[-1], 'b*', label=labeltext1)
    labeltext  = 'No'
    plt.plot(f_no[0], Fa_no[-1], 'r*', label=labeltext)
    plt.legend()
    
            
        
        
 
