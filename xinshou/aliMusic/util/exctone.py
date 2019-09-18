#coding:utf-8

import csv

#抽取一个用户的所有数据，导出到一个文件

def exctoneuser(actionfile, oneuserfile, uid):
    with open(actionfile) as ifile,\
        open(oneuserfile,'w') as ofile:

        reader = csv.reader(ifile)
        writer = csv.writer(ofile)
        for row in reader:
            if row[0] == uid:
                writer.writerow(row)

def exctonesong(actionfile, onesongfile, sid):
    with open(actionfile) as ifile,\
        open(onesongfile, 'w') as ofile:

        reader = csv.reader(ifile)
        writer = csv.writer(ofile)
        for row in reader:
            if row[1] == sid:
                writer.writerow(row)


#抽取一个艺人的所有歌曲上的所有行为
def exctartsall(actionfile, songfile, oneartsfile, artsid):
    with open(actionfile) as afile,\
        open(songfile) as sfile,\
        open(oneartsfile, 'w') as ofile:

        areader = csv.reader(afile)
        sreader = csv.reader(sfile)
        owriter = csv.writer(ofile)

        songSet = set()
        for song in sreader:
            if song[1] == artsid:
                songSet.add(song[0])

        for action in areader:
            if action[1] in songSet:
                owriter.writerow(action)

#抽取一个艺人每天发布歌曲的数量,初始热度,应该制成散点图
def exctartsong(songfile, oneartssong, artsid):
    with open(songfile) as sfile,\
        open(oneartssong, 'w') as ofile:

        sreader = csv.reader(sfile)
        owriter = csv.writer(ofile)

        for row in sreader:
            if row[1] == artsid:
                owriter.writerow(row)

#exctoneuser('data/actions.csv', 'data/oneuser.csv', '75f280b17b481f8194ab1a240c005a82')
#exctonesong('data/actions.csv', 'data/onesong.csv', 'effb071415be51f11e845884e67c0f8c')
#exctartsall('data/actions.csv', 'data/songs.csv', 'data/onearts.csv', '0c80008b0a28d356026f4b1097041689')
