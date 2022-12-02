import numpy as np
from matplotlib import pyplot as plt
# from numpy import unravel_index

# constants
D = 10              # no of devices
T = 100             # no of time slots
C = 1               # considering only 1 channel for now
R = 4               # no of relays
beta = 3            # for SINR equation
P = 180             # transmit power in dBm
episodes = 100  # no of simulation runs
frames = 50     # ...
alpha = 0.1         # learning rate
gamma = 0.5         # discount factor

for d in range(D):
    # initialise D Q-Tables (1 for each of the D devices) with zeros
    Q = []
    for i in range(d):
        Q[i] = np.zeros((T, C))
    
    for f in range(frames):
        feedback = [0 for _ in range(T)] # T feedback bits (one for each timeslot)
        for t in range(T):
            transmitting_devices = [0 for _ in range(d)]
            # those iot devices will transmit:
            # for whom q value corresponding to timeslot t is maximum
            # ie, in the q table.. value for row t must be max
            # similarly find which channel c to transmit in 
            for i in range(d): # for each iot device
                # check entry of row t in its q table
                max_index = Q[d].argmax()
                my_tuple = unravel_index(Q[d].argmax(), Q[d].shape)
                if t == my_tuple[0]:
                    transmitting_devices[d] = 1
                # if it's the max among all rows then transmit
                # transmitting_device[d] = 1 -> changed it from 0 to 1 to indicate that device d transmitted

            # now we know which devices transmitted
            # we can assign power and distance (dist will be random value btw 0 and 10 km)
            # we will get sinr using the formula
            # sort sinr values
            # keep decoding one by one till the  sinr value is below 2**beta - 1
            # Relays employ SIC to decode possible superimposed messages transmitted at same channel
            sinr = # find SINR
            if sinr >= math.pow(2, beta) - 1:
                # transmission successful: set feedback bit to 1
            else: 

                # transmission unsuccessful: set feeback bit to -1 

    # now the relays transmit T feedback bits (one for each timeslot).
    # These feedback bits indicate whether the transmission was successful
    # Based on this feedback bit we will update the Q Tables

    for i in range(d):
        # update Q-Table of device i

        reward = #check feedback bit
        Q[i][timeslot][channel] = (1-alpha)*(Q[i][timeslot][channel]) + alpha*(reward + max(Q[])) 
            

    # now find normalised throughput. formula:
    normalised_throughput = beta*(devices*messages)/(T*C*total_messages)
    # devices: no. of devices that successfully trans

    # enter this normalised throughput in an array of size D
    # plot the values in this array against the number of devices
    # normalised throughput on y axis and d on x axis
    throughputs = []
    throughputs[d] = normalised_throughput

# plot
x = np.arrange(1, D+1)
y = throughputs[x]
plt.title("Throughput vs D, with R = 4 relays and C = 1 channels") 
plt.xlabel("Number of Devices (D)") 
plt.ylabel("Normalised Throughput [bps/Hz]") 
plt.plot(x,y,"ob") 
plt.show()