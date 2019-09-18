#coding:utf8
import re
from huataidemo.huataidemo import browser_crawl


# 解析文档qxa文件，写新问题到文件当中，这时候的问题还没有去重
def qxa2qqtmp(qxafile, qqtmp):
    mode = re.compile('^\d+\. .*')  # 匹配数字起始的行
    IN = open(qxafile, 'r').readlines()
    OUT = open(qqtmp, 'w')
    for line in IN:
        if re.search(mode, line):
            index = line.find(' ')          # 找到第一个空格
            OUT.write(line[index+1:])
    OUT.flush()
    OUT.close()

def qqtmp2qq(qqall, qqtmp, qq):
    with open(qqall, 'r') as QQA, open(qqtmp, 'r') as QQT, open(qq, 'w') as QQW:
        qqalines = set([line.strip() for line in QQA.readlines()])
        qqtlines = set([line.strip() for line in QQT.readlines()])
        qqlines = qqtlines - qqalines
        for line in qqlines:
            QQW.write(line + "\n")

def qq2qqall(oldfile, newfile):
    # oldfile是已经爬取过的question， newfile是新的刚爬取过答案的question
    newlines = None
    oldlines = None
    with open(newfile, 'r') as NEWF, open(oldfile, 'r') as OLDF:
        global newlines, oldlines
        newlines = set([ line.strip() for line in NEWF.readlines() ])
        oldlines = set([ line.strip() for line in OLDF.readlines() ])
        print "newlines:\t" + str(len(newlines))
        print "oldlines:\t" + str(len(oldlines))

    with open(oldfile, 'w') as OLDF:        # 将两个文件的交集写入qqall文件
        alllines = oldlines | newlines
        print "alllines:\t" + str(len(alllines))
        for line in alllines:
            OLDF.write(line + "\n")


if __name__ == "__main__":
    # qq2qqall("../data/qqall.txt", "../data/qq00.txt")  # 将qq00归并到qqall
    # qq2qqall("../data/qqall.txt", "../data/qq01.txt")  # 将qq01归并到qqall

    # qxa2qqtmp("../data/qxa01.txt", "../data/tmpqq01.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq01.txt", "../data/qq02.txt")
    # browser_crawl("../data/qq02.txt", "../data/qxa02.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq02.txt")

    # qxa2qqtmp("../data/qxa02.txt", "../data/tmpqq02.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq02.txt", "../data/qq03.txt")
    # browser_crawl("../data/qq03.txt", "../data/qxa03.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq03.txt")

    # qxa2qqtmp("../data/qxa03.txt", "../data/tmpqq03.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq03.txt", "../data/qq04.txt")
    # browser_crawl("../data/qq04.txt", "../data/qxa04.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq04.txt")

    # qxa2qqtmp("../data/qxa04.txt", "../data/tmpqq04.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq04.txt", "../data/qq05.txt")
    # browser_crawl("../data/qq05.txt", "../data/qxa05.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq05.txt")

    # qxa2qqtmp("../data/qxa05.txt", "../data/tmpqq05.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq05.txt", "../data/qq06.txt")
    # browser_crawl("../data/qq06.txt", "../data/qxa06.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq06.txt")

    # qxa2qqtmp("../data/qxa06.txt", "../data/tmpqq06.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq06.txt", "../data/qq07.txt")
    # browser_crawl("../data/qq07.txt", "../data/qxa07.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq07.txt")

    # qxa2qqtmp("../data/qxa07.txt", "../data/tmpqq07.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq07.txt", "../data/qq08.txt")
    # browser_crawl("../data/qq08.txt", "../data/qxa08.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq08.txt")

    # qxa2qqtmp("../data/qxa08.txt", "../data/tmpqq08.txt")
    # qqtmp2qq("../data/qqall.txt", "../data/tmpqq08.txt", "../data/qq09.txt")
    # browser_crawl("../data/qq09.txt", "../data/qxa09.txt")
    # qq2qqall("../data/qqall.txt", "../data/qq09.txt")

    # 全新的开始
    #browser_crawl("../data/qq10.txt", "../data/qxa10.txt")
    #qq2qqall("../data/qqall.txt", "../data/qq10.txt")
    #qxa2qqtmp("../data/qxa10.txt", "../data/tmpqq10.txt")
    #qqtmp2qq("../data/qqall.txt", "../data/tmpqq10.txt", "../data/qq11.txt")

    #browser_crawl("../data/qq11.txt", "../data/qxa11.txt")
    #qq2qqall("../data/qqall.txt", "../data/qq11.txt")
    #qxa2qqtmp("../data/qxa11.txt", "../data/tmpqq11.txt")
    #qqtmp2qq("../data/qqall.txt", "../data/tmpqq11.txt", "../data/qq12.txt")

    #browser_crawl("../data/qq12.txt", "../data/qxa12.txt")
    #qq2qqall("../data/qqall.txt", "../data/qq12.txt")
    #qxa2qqtmp("../data/qxa12.txt", "../data/tmpqq12.txt")
    #qqtmp2qq("../data/qqall.txt", "../data/tmpqq12.txt", "../data/qq13.txt")

    #browser_crawl("../data/qq13.txt", "../data/qxa13.txt")
    #qq2qqall("../data/qqall.txt", "../data/qq13.txt")
    #qxa2qqtmp("../data/qxa13.txt", "../data/tmpqq13.txt")
    #qqtmp2qq("../data/qqall.txt", "../data/tmpqq13.txt", "../data/qq14.txt")

    #browser_crawl("../data/qq14.txt", "../data/qxa14.txt")
    #qq2qqall("../data/qqall.txt", "../data/qq14.txt")
    #qxa2qqtmp("../data/qxa14.txt", "../data/tmpqq14.txt")
    #qqtmp2qq("../data/qqall.txt", "../data/tmpqq14.txt", "../data/qq15.txt")

    browser_crawl("../data/qq15.txt", "../data/qxa15.txt")
    qq2qqall("../data/qqall.txt", "../data/qq15.txt")
    qxa2qqtmp("../data/qxa15.txt", "../data/tmpqq15.txt")
    qqtmp2qq("../data/qqall.txt", "../data/tmpqq15.txt", "../data/qq16.txt")

