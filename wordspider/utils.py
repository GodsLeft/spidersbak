#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
将单词列表当中的单词抽取出来
"""
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup


def getWords(infile, outfile):
    with open(infile, 'r') as IN:
        for line in IN:
            if line.startswith('Word'):
                continue
            word = line.strip().split(" ")[0]
            print word


def getAudio(word, outfile):
    """从百度翻译当中获取值"""
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                            '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'

    url = "http://fanyi.baidu.com/translate#en/zh/" + word
    r = requests.get(url, headers=headers)
    r.encoding = 'utf8'
    soup = BeautifulSoup(r.text, "html.parser")
    # audio = soup.find("input-operate")
    # audio = soup.find("phonetic-transcription")
    # print soup
    # audio = soup.find_all(class_="phonetic-transcription")
    # audio = soup.find_all("span", class_="phonetic-transcription")
    audio = soup.find_all("audio", id="dictVoice")
    print audio


def browser_crawl(filetocrawl, fileresult):
    # query = open(filetocrawl, 'r').readlines()
    # OUT = open(fileresult, 'w')
    browser = webdriver.Chrome(executable_path='/Users/zhuyaguang/soft/chromedriver')

    url = 'http://fanyi.baidu.com/translate'
    browser.get(url)

    dr = WebDriverWait(browser, 4)
    xpath = '//*[@id="baidu_translate_input"]'
    while not isreply(browser, xpath):     # 如果xpath出现了，isreplay为真，while退出循环，否则在此循环
        pass

    for word in filetocrawl:
        xpath = '//*[@id="baidu_translate_input"]'
        cin = browser.find_element_by_xpath(xpath)
        cin.send_keys(word + "\n")

        xpath = '//*[@id="left-result-container"]/div/div/div[1]'
        xpath = '//*[@id="left-result-container"]/div/div/div[1]/div[1]/div[2]'
        while not isreply(browser, xpath):
            pass
        cout = browser.find_element_by_xpath(xpath)
        print cout.text

        # 清空元素
        xpath = '//*[@id="main-outer"]/div/div/div/div[2]/div[1]/div[1]/div/div[2]/a'
        browser.find_element_by_xpath(xpath).click()

    return 0

    # 一下就是之前的爬虫，可以参考
    count = 0
    for question in query:
        count += 1
        if count % 50 == 0:    # 到达指定的次数就要重新刷新网页
            print "now count is: \t" + str(count)
            browser.refresh()

            xpath = '//div[@name="span_text"]/a[3]'
            while not isreply(browser, xpath):
                pass
            browser.find_element_by_xpath(xpath).click()
            # 等待机器人有回答
            # dr.until(lambda browser: browser.find_element_by_xpath('//div[@id="container"]/div[last()]//ul[@class="left_content_time1"]').is_displayed())

        # 输入问题
        uques = unicode(question, 'utf-8')
        time.sleep(1)       # 为了不要过快
        browser.switch_to.frame('msg_text')
        cin = browser.find_element_by_tag_name('body')
        cin.send_keys(uques)

        browser.switch_to.default_content()
        # 等待问题得到回答
        xpath = '//div[@id="container"]/div[last()]//ul[@class="left_content_time1"]'
        while not isreply(browser, xpath):
            pass
        cout = browser.find_element_by_xpath('//div[@id="container"]/div[last()]')
        OUT.write("\n####\n" + question + cout.text)
    print "total crawl:\t" + str(count)
    browser.close()

# 判断机器人是否回答， 这个函数是会等待4秒钟的，所以可以直接在外围重新输入
def isreply(browser, xpath):
    dr = WebDriverWait(browser, 4)
    try:
        dr.until(lambda browser: browser.find_element_by_xpath(xpath).is_displayed())
        return True
    except Exception, e:
        return False


if __name__ == '__main__':
    # getWords("wordlist.md", "hello")
    # getAudio("hello", "hello")
    browser_crawl(["hello", "world"], "world")
