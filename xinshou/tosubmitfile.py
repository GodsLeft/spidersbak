#coding:utf-8

import csv

def split_(ff, tof):
    with open(ff) as fF,\
        open(tof,'w') as tF:

        fieldnames = ['user_id','item_id']
        tFwriter = csv.DictWriter(tF,fieldnames=fieldnames)
        tFwriter.writeheader()

        liDict = dict({'user_id':'','item_id':''})
        for line in fF:
            u_i = line.split(',')[0]
            liDict['user_id'] = u_i.split('_')[0]
            liDict['user_id'], liDict['item_id'] = u_i.split('_')
            tFwriter.writerow(liDict)

split_('./vs.csv','./tianchi_mobile_recommendation_predict.csv')


