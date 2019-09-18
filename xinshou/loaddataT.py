#coding:utf-8
import numpy as np
import pandas as pd

def balancedata(x):
    if x['label'] == 0 and np.random.rand() > 0.004*5:
        x['label'] = np.nan
    return x

def timefilter(x):
    if x['time'] > 36:
        x['time'] = np.nan
    return x


dataPP = pd.read_csv('./data/labeledfea.csv',index_col='u_i')
dataTT = pd.read_csv('./data/labeledfea1.csv',index_col='u_i')

traindataT = dataPP\
    .apply(balancedata, axis=1)\
    .apply(timefilter, axis=1)\
    .dropna()

testdataT = dataTT\
    .apply(timefilter, axis=1)\
    .dropna()

