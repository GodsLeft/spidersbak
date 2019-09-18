# -*- coding: utf-8 -*-
import redis
import os
import argparse
import sys
reload(sys)
sys.setdefaultencoding('utf8')


def generateStartUrls(host):
    input = "tocrawl.txt"
    f = open(input, 'r')
    urls = f.readlines()

    start_urls = ['http://zhidao.baidu.com/search?word='+c.strip()+'&pn=0' for c in urls]

    print "#### len start_urls:\t" + str(len(start_urls))

    r = redis.Redis(host=host, port=6379)
    for i in start_urls:
        r.lpush('zhidaospider:start_urls', i)


def changeSettings(host):
    path = os.getcwd()
    os.chdir(path + '/zhidao')
    f = open('settings.py', 'r')
    lines = f.readlines()
    if not lines[-1].startswith("REDIS_URL = "):
        f = open('settings.py', 'a')
        f.write("REDIS_URL = 'redis://" + host + ":6379'")


def runSpider(host):
    changeSettings(host)
    os.chdir(os.path.dirname(os.getcwd()))
    os.system('scrapy crawl zhidaospider')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-host', action='store', dest='host', default='127.0.0.1',
                        help='The host address for Redis, default is 127.0.0.1')
    parser.add_argument('-input', action='store', dest='input',
                        help='The file listing items you want to crawl')
    parser.add_argument('-master', action='store', dest='master', default='0',
                        help='This defines master machine. By defalut(master=0),it is slave. Otherwise(master=1), it is the master where Redis is configured')
    args = parser.parse_args()
    if args.master == '1':
        generateStartUrls(args.host)
    if (args.master and not args.host) or (args.host and not args.master):
        print 'If master, identify the host address and input file. See python runSpider.py -h'
    runSpider(args.host)