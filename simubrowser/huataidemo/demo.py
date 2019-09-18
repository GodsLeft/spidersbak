#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
#sys.stdout = io.TextIOWrapper(, encoding='utf-8')


def phantomjs_get_webpage(filepath):
    #browser = webdriver.PhantomJS()

    query = open('../data/qq00.txt', 'r').readlines()
    OUT = open('../data/qxa00.txt', 'w')
    browser = webdriver.Chrome(executable_path='C:\Program Files\\xleftsoft\chromedriver.exe')

    url = 'http://imcc.zhangle.com:8081/webchat/'
    browser.get(url)

    # time.sleep(4)
    dr = WebDriverWait(browser, 4)
    dr.until(lambda thebrowser: thebrowser.find_element_by_xpath('//div[@name="span_text"]/a[3]').is_displayed())
    elem = browser.find_element_by_xpath('//div[@name="span_text"]/a[3]')
    elem.click()

    count = 0
    for question in query:
        count += 1
        if count % 100 == 0:    # 到达指定的次数就要重新刷新网页
            print "now count is: \t" + str(count)
            browser.refresh()
            dr.until(lambda thebrowser: thebrowser.find_element_by_xpath('//div[@name="span_text"]/a[3]').is_displayed())
            browser.find_element_by_xpath('//div[@name="span_text"]/a[3]').click()
            # 等待机器人有回答
            dr.until(lambda browser: browser.find_element_by_xpath('//div[@id="container"]/div[last()]//ul[@class="left_content_time1"]').is_displayed())

        # 输入问题
        uques = unicode(question, 'utf-8')
        time.sleep(1)       # 为了不要过快
        browser.switch_to.frame('msg_text')
        cin = browser.find_element_by_tag_name('body')
        cin.send_keys(uques)

        browser.switch_to.default_content()
        # 等待问题得到回答
        dr.until(lambda browser: browser.find_element_by_xpath('//div[@id="container"]/div[last()]//ul[@class="left_content_time1"]').is_displayed())
        cout = browser.find_element_by_xpath('//div[@id="container"]/div[last()]')
        OUT.write("\n####\n" + question + cout.text)
    browser.close()

# 判断机器人是否回答
def isreply(browser, xpath):
    dr = WebDriverWait(browser, 4)
    try:
        dr.until(lambda browser: browser.find_element_by_xpath(xpath).is_displayed())
        return True
    except Exception, e:
        return False

if __name__ == "__main__":
    phantomjs_get_webpage("a")