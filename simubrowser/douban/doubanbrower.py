#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def browser_crawl(filetocrawl, fileresult):
    query = open(filetocrawl, 'r').readlines()
    OUT = open(fileresult, 'w')
    browser = webdriver.Chrome()

    for mvname_ori in query:
        url = 'https://movie.douban.com/'
        browser.get(url)

        dr = WebDriverWait(browser,4)
        xpath = '//input[@id="inp-query"]'
        while not isreplay(browser, xpath):
            pass
        cin = browser.find_element_by_xpath(xpath)
        mvname_ori = unicode(mvname_ori.strip(), 'utf-8')
        cin.send_keys(mvname_ori)
        cin.send_keys(Keys.ENTER)

        #xpath = '//div[@class="inp-btn"]/input"]'
        #browser.find_element_by_xpath(xpath).click()


        #xpath = '//div[@class="title"]//a[1]'
        xpath = '//div[@class="sc-dnqmqq eXEXeG"]/div[1]//div[@class ="title"]/a'
        while not isreplay(browser, xpath):
            pass

        cout = browser.find_element_by_xpath(xpath).click()

        xpath = '//div[@id="info"]'
        count = 0
        while not isreplay(browser, xpath): # 当没有回应的时候执行pass
            count += 1
            if count == 10:
                break

        if count < 10:
            xpath = '//div[@id="info"]'
            cout = browser.find_element_by_xpath(xpath).text
            xpath = '//h1'
            mvname = browser.find_element_by_xpath(xpath).text
            print cout
            OUT.write("####\n" + mvname_ori.encode('utf8') + "\n" + mvname.encode('utf8') + "\n" + cout.encode('utf8') + "\n")
    browser.close()
    OUT.close()


def isreplay(browser, xpath):
    dr = WebDriverWait(browser, 4)
    try:
        dr.until(lambda browser: browser.find_element_by_xpath(xpath).is_displayed())
        return True
    except Exception, e:
        return False

if __name__ == '__main__':
    browser_crawl("./data/mvname.txt", "./data/test.txt")