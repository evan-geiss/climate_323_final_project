# does a lot of the analysis heavy lifting for main.ipynb
# this might get moved back to main, but seemed more resource efficient

import pandas as pd
import numpy as np

# take dfs and return a list of arrays for each cycle
def takeData(bz, fp, ssCount, dst):
    vars = [bz, fp, ssCount, dst]
    
    cycle_21 = np.array([[], [], [], [], []]) # time, bz, fp, ssCount, dst
    cycle_22 = np.array([[], [], [], [], []])
    cycle_23 = np.array([[], [], [], [], []])
    cycle_24 = np.array([[], [], [], [], []])
    cycle_25 = np.array([[], [], [], [], []])
    cycle_dfs = np.array([cycle_21, cycle_22, cycle_23, cycle_24, cycle_25])

    for b in bz:
        for f in fp:
            for s in ssCount:
                for d in dst:
                    for i in range(len(vars[0])):
                        print('i:', i)
                        print('bz:', b[i, 0])
                        print('fp:', f[i, 0])
                        print('ss:', s[i, 0])
                        print('dst:', d[i, 0])
                        print('bz:', b[i, 2])
                        #if (bz[i, 0] == fp[i, 0] == ssCount[i, 0] == dst[i, 0]):
                        #    if (bz[i, 2] == 21):
                        #        cycle_21 = np.vstack((cycle_21, [bz[i, 0], bz[i, 1], fp[i, 1], ssCount[i, 1], dst[i, 1]]))
    return cycle_dfs

# run some basic analysis
# shape, head, info, describe
def basicAnalysis(df):
    print('shape:', df.shape)
    print('head:', '\n', df.head())
    print('info:', '\n', df.info())
    print('describe:', '\n', df.describe())

# run basic analysis on each dataframe
def runBasicAnalysis(cycle_dfs):
    for x in cycle_dfs:
        basicAnalysis(x)

# basic regression analysis function
# correlations should only be done between data in same cycle
# so cycle 21 data should not be compared to cycle 22 data
# correlations are done between each column in the dataframe
def regressionAnalysis(df):
    print('regression analysis for:', '\n', df)
    print('correlation matrix:', '\n', df.corr())
    print('covariance matrix:', '\n', df.cov())

# run regression analysis on each dataframe
def runRegressionAnalysis(dfs):
    for x in dfs:
        regressionAnalysis(x)

# find function for the cyclical nature of the data
# this is a simple function that will find the cycle length
# by finding the difference between the first and last cycle
# and dividing by the number of cycles
def findCycleLength(df):
    print('finding cycle length for:', '\n', df)
    first = df['time'].min()
    last = df['time'].max()
    cycles = df['cycle'].nunique()
    cycleLength = (last - first) / cycles
    print('first:', first)
    print('last:', last)
    print('cycles:', cycles)
    print('cycle length:', cycleLength)