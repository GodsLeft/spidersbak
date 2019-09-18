#coding:utf-8
import csv

#这个文件做一些统计量

#统计songs文件
def statissongs(songsfile):
    artistSet = set()
    songSet = set()
    languageSet = set()

    with open(songsfile) as ifile:
        reader = csv.reader(ifile)
        for row in reader:
            songSet.add(row[0])
            artistSet.add(row[1])
            languageSet.add(row[4])

    print "songs:"
    print "artistnum:\t" + str(len(artistSet))
    print "songnum:\t" + str(len(songSet))
    print "langunum:\t" + str(len(languageSet))


#统计action文件
def statisactions(actionfile):
    userSet = set()
    songSet = set()

    with open(actionfile) as ifile:
        reader = csv.reader(ifile)
        for row in reader:
            userSet.add(row[0])
            songSet.add(row[1])

    print "actions:"
    print "usernum:\t" + str(len(userSet))
    print "songnum:\t" + str(len(songSet))

#statissongs('data/songs.csv')
#statisactions('data/actions.csv')
