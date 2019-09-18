# -*- coding:utf-8 -*-

import pandas as pd
#import numpy as np

#from exctone import exctonesong, exctoneuser, exctartsall
#exctoneuser('data/actions.csv', 'data/oneuser.csv', '75f280b17b481f8194ab1a240c005a82')
#exctonesong('data/actions.csv', 'data/onesong.csv', 'effb071415be51f11e845884e67c0f8c')
#exctartsall('data/actions.csv', 'data/songs.csv', 'data/onearts.csv', '0c80008b0a28d356026f4b1097041689')

#from type2vec import type2vec
#type2vec('data/oneuser.csv', 'data/oneuservec.csv')
#type2vec('data/onesong.csv', 'data/onesongvec.csv')
#type2vec('data/onearts.csv', 'data/oneartsvec.csv')

# 这里只调查了一个用户，用户的数据很稀疏
#df = pd.read_csv('data/oneuservec.csv', parse_dates=True)
#df = df.iloc[:,3:]
#dfg = df.groupby('ds').sum()
#dfg.plot()

# 调查一首歌曲的所有行为
def totime(x): return pd.to_datetime(str(x))

def oneplot(vecfile):
    df = pd.read_csv(vecfile) #如果指定的索引不是日期类型，没有意义
    df = df.iloc[:,3:]
    df = df.groupby('ds', as_index=False).sum()
    df['ds'] = df['ds'].apply(totime)
    df = df.set_index(['ds'])
    return df

def oneplot1(vecfile):
    df = pd.read_csv(vecfile, index_col='ds', parse_dates=True)\
        .iloc[:,3:]\
        .reset_index()\
        .groupby('ds').sum()
    return df
'''
#抽取一个艺人的所有的歌曲并进行一些初始热度的统计
from exctone import exctartsong
exctartsong('data/songs.csv','data/oneartsallsong.csv','0c80008b0a28d356026f4b1097041689')
'''

df = pd.read_csv('data/oneartsallsong.csv', index_col=2, parse_dates=True, header=None)
'''
dayplaymean = df.drop([0,1,4,5], axis=1)\
    .reset_index()\
    .groupby(2).mean()
daysongcount = df.drop([1,3,4,5], axis=1)\
    .reset_index()\
    .groupby(2).count()
'''
ll = df.drop([1,4,5], axis=1)\
    .reset_index()\
    .groupby(2)\
    .agg({0:'count', 3:'mean'})


