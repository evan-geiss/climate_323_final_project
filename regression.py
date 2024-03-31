# does a lot of the analysis heavy lifting for main.ipynb
# this might get moved back to main, but seemed more resource efficient

import pandas as pd
import numpy as np


# read in data files from ./data/cycles/
bZ = pd.DataFrame()
fp = pd.DataFrame()
ssCount = pd.DataFrame()
dst = pd.DataFrame()

# take dfs and return a list of dataframes for each cycle
def takeData(bZ, fp, ssCount, dst):
    combined = pd.concat([bZ, fp, ssCount, dst], axis=1)
    print('combined:', '\n', combined)


    dfs = [bZ, fp, ssCount, dst]
    
    cycle_21 = pd.DataFrame()
    cycle_22 = pd.DataFrame()
    cycle_23 = pd.DataFrame()
    cycle_24 = pd.DataFrame()
    cycle_25 = pd.DataFrame()
    cycle_dfs = [cycle_21, cycle_22, cycle_23, cycle_24, cycle_25]
    
    for df in dfs:
        cycle_21 = df[df['cycle'] == 21]
        cycle_22 = df[df['cycle'] == 22]
        cycle_23 = df[df['cycle'] == 23]
        cycle_24 = df[df['cycle'] == 24]
        cycle_25 = df[df['cycle'] == 25]
        cycle_dfs = [cycle_21, cycle_22, cycle_23, cycle_24, cycle_25]
    
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