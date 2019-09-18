#coding:utf-8
#import numpy as np
import pandas as pd
import time

def timetrans(x):
    x.ix[2] = time.strftime('%Y-%m-%d', time.gmtime(x.ix[2]))
    return x

def timetrans2(x):
    return time.strftime("%Y-%m-%d", time.localtime(x));

dataActions = pd.read_csv('./data/actions_sample_20.csv', header=None)
dataSongs = pd.read_csv('./data/songs.csv', header=None)

#dataA = dataActions.ix[:,2].map(timetrans2);
#dataA = dataActions.\
#    apply(timetrans, axis=1)



