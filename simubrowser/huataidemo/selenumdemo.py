#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
import sys
import io
import time
reload(sys)
sys.setdefaultencoding('utf-8')
#sys.stdout = io.TextIOWrapper(, encoding='utf-8')


def phantomjs_get_webpage(filepath):
    #browser = webdriver.PhantomJS()
    browser = webdriver.Chrome(executable_path='C:\Program Files\\xleftsoft\chromedriver.exe')

    url = 'http://imcc.zhangle.com:8081/webchat/'
    browser.get(url)

    # 填写数据并确认
    time.sleep(3)
    elem = browser.find_element_by_xpath('//div[@name="span_text"]/a[3]')
    elem.click()

    # 这个用来显示截屏，但是不必了
    # browser.get_screenshot_as_file('show.png')  # 这个用来做测试会好一点

    browser.switch_to.frame('msg_text')
    cin = browser.find_element_by_tag_name('body')
    query = u"""股票\n"""
    cin.send_keys(query)

    try:
        browser.switch_to.default_content()
        print "4####"
        dr = WebDriverWait(browser, 5)    # 5s内每隔500毫秒扫描一次页面变化，直到指定的元素
        print "5#####"
        dr.until(lambda browser: browser.find_element_by_xpath('//div[@id="container"]').is_displayed())
        print "6######"
        cout = browser.find_element_by_xpath('//div[@id="container"]/div[last()]')
    except:
        print 'ERROR: too long time not get a response'
        browser.close()
        sys.exit(0)
    #time.sleep(3)  # 这个方法是不太好的
    print cout.text
    #browser.close()

    #alist = cout.find_element_by_xpath('//a')
    #for atext in alist:
    #    print alist.text

    #try:
    #    dr = WebDriverWait(browser, 5)
    #    dr.until(lambda the_driver: the_driver.find_element_by_xpath('//*').is_displayed())
    #except:
    #    print 'shi bai'
    #    sys.exit(0)
    #browser.get_screenshot_as_file('show1.png')
    #htmlpage = browser.page_source.decode('utf-8')
    #IN = open('hello.html', 'w')
    #IN.write(htmlpage.encode('utf-8'))

if __name__ == "__main__":
    phantomjs_get_webpage("a")
