#coding:utf-8

#import csv
import datetime

tL = datetime.datetime(2015,7,1,0,0,0)

fr = open('./user_actions.csv')
fwTrain = open('user_actions_train.csv', 'w')
fwTest  = open('user_actions_test.csv', 'w')
for line in fr.readlines():
    fields = line.split(',')
    tm = datetime.datetime.fromtimestamp(int(fields[2]))
    if tm <= tL:
        fwTrain.write(line)
    else:
        fwTest.write(line)

fr.close()
fwTrain.close()
fwTest.close()
