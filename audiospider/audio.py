#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
下载音频数据
"""

import urllib
import requests
from bs4 import BeautifulSoup
import os
import time
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# 吞噬星空，仙逆
prefix = 'http://www.ting89.com/down/?1520-{}.html'
name = 'xianni'
count = 2065


# create dir
name_dir = os.path.join('data', name)
if not os.path.exists(name_dir):
    os.mkdir(name_dir)
    os.mkdir(os.path.join(name_dir + 'audio'))
    os.mkdir(os.path.join(name_dir + 'text'))

for i in range(0, count):
    r = requests.get(prefix.format(i))
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, "html.parser")
    
    # get download url
    iframe = soup.find('iframe')
    src = iframe['src']
    idx = src.find('url=')
    url = src[idx + 4:].encode('utf-8')

    # download to file
    ch = "%04d" % (i + 1)
    output_dir = os.path.join(os.path.join(name_dir, 'audio'), ch + '.mp3')
    urllib.urlretrieve(url, output_dir)
    time.sleep(1)

print '{} is finished.'.format(name)

