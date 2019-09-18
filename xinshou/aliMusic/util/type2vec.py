#coding:utf-8
import csv

def type2vec(typefile, vecfile):
    with open(typefile) as ifile,\
        open(vecfile, 'w') as ofile:

        reader = csv.reader(ifile)
        fieldnames = ['uid','sid','gti','aty1','aty2','aty3','ds']
        writer = csv.DictWriter(ofile, fieldnames=fieldnames)
        writer.writeheader()

        line = {'uid':'', 'sid':'', 'gti':'', 'aty1':'0', 'aty2':'0', 'aty3':'0','ds':''}
        for row in reader:
            line['uid'] = row[0]
            line['sid'] = row[1]
            line['gti'] = row[2]
            line['ds'] = row[4]
            line['aty1'] = '0'
            line['aty2'] = '0'
            line['aty3'] = '0'
            line['aty'+row[3]] = 1
            writer.writerow(line)

# 测试，先使用10行的简单文件
#type2vec('data/actions_sample_10.csv', 'data/vec_sample_10.csv')
#type2vec('data/oneuser.csv', 'data/oneuservec.csv')
#type2vec('data/onesong.csv', 'data/onesongvec.csv')
