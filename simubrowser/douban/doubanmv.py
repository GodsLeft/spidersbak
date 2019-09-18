#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re
import urllib2
from lxml import etree

# 下载并打印网页，动态网页无法解析
def askurl(url):
    request = urllib2.Request(url)
    try:
        response = urllib2.urlopen(request)
        html = response.read()
        print html

        selector = etree.HTML(html)
        lst = selector.xpath('//div[@class="title"]/a/@href')
        print lst
    except urllib2.URLError, e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

    return html

def getData(baseurl):
    findLink = re.compile()


if __name__ == "__main__":
    askurl('https://movie.douban.com/subject_search?search_text=%E6%88%98%E7%8B%BC&cat=1002')
