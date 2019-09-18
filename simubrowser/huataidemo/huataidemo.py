#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')


def browser_crawl(filetocrawl, fileresult):
    query = open(filetocrawl, 'r').readlines()
    OUT = open(fileresult, 'w')
    browser = webdriver.Chrome(executable_path='C:\Program Files\\xleftsoft\chromedriver.exe')

    url = 'http://imcc.zhangle.com:8081/webchat/'
    browser.get(url)

    dr = WebDriverWait(browser, 4)
    xpath = '//div[@name="span_text"]/a[3]'
    while not isreply(browser, xpath):     # 如果xpath出现了，isreplay为真，while退出循环，否则在此循环
        pass
    browser.find_element_by_xpath(xpath).click()

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

if __name__ == "__main__":
    #phantomjs_get_webpage("../data/qq01.txt", "../data/qxa01.txt")
    browser_crawl("../data/qq02.txt", "../data/qxa02.txt")
