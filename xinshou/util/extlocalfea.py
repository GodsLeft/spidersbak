# coding:utf-8
import csv
import pandas as pd

"""
目的：生成用户的局部特征
"""

def extlocalfea(datafile, localfeafile, timeline1, timeline2):
    """提取局部特征，用户的四类行为个数，购买商品种类个数"""
    tL1 = pd.to_datetime(timeline1)
    tL2 = pd.to_datetime(timeline2)
    with open(datafile) as trfile,\
            open(localfeafile, 'w') as fnfile:

        fieldnames = ['user_id', 'bhvr_1', 'bhvr_2', 'bhvr_3', 'bhvr_4', 'item_n']
        reader = csv.DictReader(trfile)
        writer = csv.DictWriter(fnfile, fieldnames=fieldnames)
        writer.writeheader()
        user_dict = {'user_id': '', 'bhvr_1': 0, 'bhvr_2': 0, 'bhvr_3': 0, 'bhvr_4': 0, 'item_n': 0}
        itemSet = set()
        flag = 1
        for row in reader:
            tl = pd.to_datetime(row['time'])
            if tl < tL1 or tl > tL2: #为了conbine
                continue

            if row['user_id'] == user_dict['user_id']:
                user_dict['bhvr_'+row['behavior_type']] += 1
                itemSet.add(row['item_id'])
            else:
                if flag == 1:
                    flag -= 1
                else:
                    user_dict['item_n'] = len(itemSet)
                    writer.writerow(user_dict)
                itemSet.clear()
                user_dict['user_id'] = row['user_id']
                user_dict['bhvr_1'] = 0
                user_dict['bhvr_2'] = 0
                user_dict['bhvr_3'] = 0
                user_dict['bhvr_4'] = 0
                user_dict['item_n'] = 0
                itemSet.add(row['item_id'])
                user_dict['bhvr_'+row['behavior_type']] += 1
        user_dict['item_n'] = len(itemSet)
        writer.writerow(user_dict)


#extlocalfea('data/data.csv','data/userlocalfea.csv', '2014-12-13','2014-12-17')
#extlocalfea('data/data.csv','data/userlocalfea1.csv', '2014-12-14','2014-12-18')
#extlocalfea('data/data.csv','data/userlocalfea2.csv', '2014-12-15','2014-12-19')
