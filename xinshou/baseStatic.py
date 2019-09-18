#:coding:utf-8
"""
每天的购买量，绘图
每天商品子集的购买量，绘图
"""
import csv

def static(trainfile, tofile):
    with open(trainfile) as trainf,\
        open(tofile, 'w') as tof:

        reader = csv.DictReader(trainf)

# 一些简单的数据描述图
"""
import pandas as pd
import matplotlib.pyplot as plt
# import numpy as np
# from pandas import Series, DataFrame

userData = pd.read_csv('data/userGlobalFea.csv',index_col='user_id')
userData.describe()
userData.ix[:,['bhvr_4']].head(100).plot(kind='bar',stacked=True)

# 横轴代表bhvr_4的次数，纵轴代表多少个用户发生这样的行为
userData.ix[:,['bhvr_4']].head(100).hist(bins=50)

# 两种行为相关性的散点图
plt.scatter(userData['bhvr_1'],userData['bhvr_4'])

# 求任意两列之间的散点图
pd.scatter_matrix(userData,diagonal='kde',color='k',alpha=0.3)

# 每天购买情况统计图
data = pd.read_csv('data/trainP.csv',index_col='time',parse_dates=True)
someCol = data['behavior_type']
buyCol = someCol[someCol == 4]
buyCol.resample('D',how='sum',kind='period').plot()
"""
