#coding:utf-8
import csv
import pandas as pd

def combinefea(datafile,\
               userlocalfea,userglobalfea,itemFea,\
               allFea,\
               timeline1, timeline2):

    with open(datafile) as trf,\
        open(userlocalfea) as lclf,\
        open(userglobalfea) as glbf,\
        open(itemFea) as itmf,\
        open(allFea,'w') as af:

        lclDict = dict()
        lclReader = csv.DictReader(lclf)
        for row in lclReader:
            lclDict[row['user_id']] = row

        glbDict = dict()
        glbReader = csv.DictReader(glbf)
        for row in glbReader:
            glbDict[row['user_id']] = row

        itmDict = dict()
        itmReader = csv.DictReader(itmf)
        for row in itmReader:
            itmDict[row['item_id']] = row

        fieldnames = ['u_i',\
                      'gbh1','gbh2','gbh3','gbh4','gitm',\
                      'lbh1','lbh2','lbh3','lbh4','litm',\
                      'bhvrT1','bhvrT2','bhvrT3','bhvrT4','cat','time',\
                      'ibh1','ibh2','ibh3','ibh4','label']

        afWriter = csv.DictWriter(af, fieldnames = fieldnames)
        afWriter.writeheader()

        tL1 = pd.to_datetime(timeline1)
        tL2 = pd.to_datetime(timeline2)
        lineDict = dict()
        trReader = csv.DictReader(trf)
        for row in trReader:
            tl = pd.to_datetime(row['time'])
            if tl < tL1 or tl > tL2:
                continue
            lineDict['label'] = 0

            uGlbDict = glbDict[row['user_id']]
            lineDict['u_i'] = row['user_id']+'_'+row['item_id']
            lineDict['gbh1'] = uGlbDict['bhvr_1']
            lineDict['gbh2'] = uGlbDict['bhvr_2']
            lineDict['gbh3'] = uGlbDict['bhvr_3']
            lineDict['gbh4'] = uGlbDict['bhvr_4']
            lineDict['gitm'] = uGlbDict['item_n']

            uLclDict = lclDict[row['user_id']]
            lineDict['lbh1'] = uLclDict['bhvr_1']
            lineDict['lbh2'] = uLclDict['bhvr_2']
            lineDict['lbh3'] = uLclDict['bhvr_3']
            lineDict['lbh4'] = uLclDict['bhvr_4']
            lineDict['litm'] = uLclDict['item_n']

            if row['item_id'] in itmDict:
                iLclDict = itmDict[row['item_id']]
                lineDict['ibh1'] = iLclDict['bh1']
                lineDict['ibh2'] = iLclDict['bh2']
                lineDict['ibh3'] = iLclDict['bh3']
                lineDict['ibh4'] = iLclDict['bh4']
            else:
                lineDict['ibh1'] = 0
                lineDict['ibh2'] = 0
                lineDict['ibh3'] = 0
                lineDict['ibh4'] = 0

            lineDict['bhvrT1'] = 0
            lineDict['bhvrT2'] = 0
            lineDict['bhvrT3'] = 0
            lineDict['bhvrT4'] = 0
            lineDict['bhvrT'+row['behavior_type']] = 1

            lineDict['cat'] = row['item_category']
            delt = (tL2 - tl).total_seconds()/3600
            lineDict['time'] = delt if delt > 0 else 0

            afWriter.writerow(lineDict)
            lineDict.clear()
"""
combinefea('./data/data.csv',\
           './data/userlocalfea.csv','./data/userglobalfea.csv','./data/itemlclfea.csv',\
           './data/allfea.csv',\
           '2014-12-13','2014-12-17')
combinefea('./data/data.csv',\
           './data/userlocalfea1.csv','./data/userglobalfea.csv','./data/itemlclfea1.csv',\
           './data/allfea1.csv',\
           '2014-12-14','2014-12-18')
"""
"""
combinefea('./data/data.csv',\
           './data/userlocalfea2.csv','./data/userglobalfea.csv','./data/itemlclfea2.csv',\
           './data/allfea2.csv',\
           '2014-12-15','2014-12-19')
"""
