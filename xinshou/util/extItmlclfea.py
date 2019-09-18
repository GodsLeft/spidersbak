#coding:utf-8
import csv
import pandas as pd
"""
提取商品的基本信息
可推测商品的火爆程度
"""

def extitemlclfea(datafile,itemFea, timeline1, timeline2):
    with open(datafile) as trf,\
        open(itemFea,'w') as itmf:

        tL1 = pd.to_datetime(timeline1)
        tL2 = pd.to_datetime(timeline2)
        itemMap = dict()
        trReader = csv.DictReader(trf)
        for row in trReader:
            tl = pd.to_datetime(row['time'])
            if tl < tL1 or tl > tL2:
                continue

            if row['item_id'] in itemMap:
                item = itemMap[row['item_id']]
                item['bh'+row['behavior_type']] += 1
            else:
                itemMap[row['item_id']] = dict()
                itemMap[row['item_id']]['item_id'] = row['item_id']
                itemMap[row['item_id']]['bh1'] = 0
                itemMap[row['item_id']]['bh2'] = 0
                itemMap[row['item_id']]['bh3'] = 0
                itemMap[row['item_id']]['bh4'] = 0
                itemMap[row['item_id']]['bh'+row['behavior_type']]+= 1

        fieldnames = ['item_id','bh1','bh2','bh3','bh4']
        itWriter = csv.DictWriter(itmf, fieldnames = fieldnames)
        itWriter.writeheader()
        for aitem in itemMap:
            itWriter.writerow(itemMap[aitem])

#extitemlclfea('./data/data.csv','./data/itemlclfea.csv','2014-12-13','2014-12-17')
#extitemlclfea('./data/data.csv','./data/itemlclfea1.csv','2014-12-14','2014-12-18')
#extitemlclfea('./data/data.csv','./data/itemlclfea2.csv','2014-12-15','2014-12-19')
