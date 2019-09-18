#coding:utf-8

import csv
import random

#随机获取一定量的数据
def randsample(actfile, samplefile, percent):
    with open(actfile) as ifile,\
        open(samplefile,'w') as ofile:

        reader = csv.reader(ifile);
        writer = csv.writer(ofile);

        for row in reader:
            if random.random() < percent:
                writer.writerow(row)

randsample('data/actions.csv', 'data/action_10p.csv', 0.01)
