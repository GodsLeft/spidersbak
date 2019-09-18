#coding:utf-8
import csv
import pandas as pd
"""
将特征打上标签
"""
def tolabelfea(trainP, allFea, allLabelFea, timeline1, timeline2):
    with open(trainP) as trP,\
            open(allFea) as alF,\
            open(allLabelFea, 'w') as albF:

        tL1 = pd.to_datetime(timeline1)
        tL2 = pd.to_datetime(timeline2)
        labelSet = set()
        trReader = csv.DictReader(trP)
        for row in trReader:
            tl = pd.to_datetime(row['time'])
            if tL2 > tl > tL1:
                if row['behavior_type'] == '4': #这里我觉得可以是3或者4，有一定的相关性
                    labelSet.add(row['user_id']+'_'+row['item_id'])

        fieldnames = ['u_i',
                      'gbh1', 'gbh2', 'gbh3', 'gbh4', 'gitm',
                      'lbh1', 'lbh2', 'lbh3', 'lbh4', 'litm',
                      'bhvrT1', 'bhvrT2', 'bhvrT3', 'bhvrT4', 'cat', 'time',
                      'ibh1', 'ibh2', 'ibh3', 'ibh4', 'label']
        lbWriter = csv.DictWriter(albF, fieldnames=fieldnames)
        lbWriter.writeheader()

        afReader = csv.DictReader(alF)
        for row in afReader:
            if row['u_i'] in labelSet:
                row['label'] = 1
            lbWriter.writerow(row)

#tolabelfea('data/data.csv','data/allfea.csv','./labeledfea.csv','2014-12-17','2014-12-18')
#tolabelfea('data/data.csv','data/allfea1.csv','./labeledfea1.csv','2014-12-18','2014-12-19')
#tolabelfea('data/data.csv','data/allfea2.csv','./labeledfea2.csv','2014-12-19','2014-12-20')
