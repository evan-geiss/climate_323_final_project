import pandas as pd
import numpy as np
import datetime as dt
from matplotlib import pyplot as plt

# import data from csv fil
bZ = pd.read_csv('./data/cleaned/bZ_cleaned.csv')
fP = pd.read_csv('./data/cleaned/fP_cleaned.csv')
ssCount = pd.read_csv('./data/cleaned/ssCount_cleaned.csv')
dst = pd.read_csv('./data/cleaned/dst_cleaned.csv')

# convert all the time ranges to datetime
bZ['time'] = pd.to_datetime(bZ['time'], format="b'%Y-%m-%d %H:%M:%S'")
fP['time'] = pd.to_datetime(fP['time'], format="b'%Y-%m-%d %H:%M:%S'")
ssCount['time'] = pd.to_datetime(ssCount['time'], format="b'%Y-%m-%d %H:%M:%S'")
dst['time'] = pd.to_datetime(dst['time'], format="b'%Y-%m-%d %H:%M:%S'")

# plot data
fig, axs = plt.subplots(4, figsize=(320,160))
plt.rc('font', size=16)

axs[0].plot(bZ['time'], bZ['bZ'])
axs[0].set_title('Magnetic Field')
axs[0].set_ylabel('bZ')
axs[0].set_xlabel('Time')

axs[1].plot(fP['time'], fP['fP'])
axs[1].set_title('Plasma Flow')
axs[1].set_ylabel('fP')
axs[1].set_xlabel('Time')

axs[2].plot(ssCount['time'], ssCount['ssCount'])
axs[2].set_title('Sunspot Count')
axs[2].set_ylabel('ssCount')
axs[2].set_xlabel('Time')

axs[3].plot(dst['time'], dst['dst'])
axs[3].set_title('DST Index')
axs[3].set_ylabel('dst')
axs[3].set_xlabel('Time')

plt.show()

# save all plots to a single file
plt.savefig('./plots/plots.png')