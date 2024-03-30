import numpy as np
import pandas as pd
import datetime as dt

# import data from csv file 
# time is imported separately as a string
data = np.genfromtxt('./data/omni.csv', delimiter=',', skip_header=117, usecols=range(1, 5))
time = np.genfromtxt('./data/omni.csv', delimiter=',', skip_header=117, usecols=0, dtype=str)

# Convert time to datetime
time = [dt.datetime.strptime(t, '%Y-%m-%dT%H:%M:%S.%fZ') for t in time]
time = np.array(time)
# create a temp array to store the data
tempArray = np.array([])
tempTime = np.array([])

for i in range(len(data)):
    if ((data[i, 0] == 999.9).any()):
        print('bZ = 999.9 at index', i)
        print('Time:', time[i])
        print('Data:', data[i])
        continue
    elif ((data[i, 1] == 99.99).any()):
        print('fP = 99.99 at index', i)
        print('Time:', time[i])
        print('Data:', data[i])
        continue
    elif ((data[i,2] == 999).any()):
        print('ssCount = 999 at index', i)
        print('Time:', time[i])
        print('Data:', data[i])
        continue
    else:
        print('Data is good at index', i)
        print('Time:', time[i])
        print('Data:', data[i])
        tempArray = np.append(tempArray, data[i])
        tempTime = np.append(tempTime, time[i])
    print()

data = tempArray
time = tempTime
# save the cleaned data and time to a new csv file

data = data.reshape(-1, 4)
np.savetxt('./data/omni_cleaned_data.csv', data, delimiter=',')
np.savetxt('./data/omni_cleaned_time.csv', time, delimiter=',', fmt='%s')