#coding:utf-8
import numpy as np
import pandas as pd

def balancedata(x):
    if x['label'] == 0 and np.random.rand() > 0.004*5:
        x['label'] = np.nan
    return x

def timefilter(x):
    if x['time'] > 24:
        x['time'] = np.nan
    return x


dataP = pd.read_csv('./data/labeledfea1.csv',index_col='u_i')
dataT = pd.read_csv('data/labeledfea2.csv', index_col='u_i')

traindata = dataP.\
    apply(balancedata, axis=1).\
    apply(timefilter, axis=1).\
    dropna()

testdata = dataT.\
    apply(timefilter, axis=1).\
    dropna()

