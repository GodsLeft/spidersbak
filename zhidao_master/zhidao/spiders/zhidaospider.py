# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from scrapy.http import Request
from scrapy.selector import Selector
from zhidao.items import SearchItem
from scrapy_redis.spiders import RedisCrawlSpider
import time
import scrapy


class ZhidaospiderSpider(RedisCrawlSpider):
    name = 'zhidaospider'
    redis_key = 'zhidaospider:start_urls'

    def parse(self, response):
        global start_time
        start_time = time.time()

        html = Selector(response)
        base_url = 'http://zhidao.baidu.com'
        start_url = response.url
        #print "#### start url:\t" + start_url
        urls = html.xpath('//div[@id="wgt-list"]/dl/dt/a/@href').extract()  # 获得当前页面的问题与答案的列表url，通常每页有10个
        # print "#### urls length:\t" + str(len(urls))

        start_url = ''.join(start_url)
        crawlednum = start_url.split("=")[-1]
        if crawlednum.isdigit():
            crawlednum = int(crawlednum)             # 这里的i表明，到当前页面为止，搜索了多少索引项，i只会是10的整倍数，因为一页只有10个索引
        else:
            crawlednum = 1

        if crawlednum > 30:           # 所以这里设置3的话，就会爬取10条
            return
        if len(urls) == 0:          # 当前索引页面当中没有内容
            return

        for Url in urls:            # 解析当前页面当中的问题与答案
            #print "#### zhidao_parse\t" + Url
            yield Request(url=Url, callback=self.zhidao_parse)      # 解析页面当中的一个标题

        nextPageUrl = html.xpath('//div[@class="pager"]/a/@href').extract()         # 获得所有页面的url，这个实际上是获取一个页面列表，获取第2/3/4/5...下一页，尾页url
        nextPageText = html.xpath('//div[@class="pager"]/a/text()').extract()       # 获得url对应的文本

        if len(nextPageUrl) == 0:
            return
        if len(nextPageText) == 0:
            return

        #if nextPageText and '下一页'.decode('utf8') in nextPageText[-2].encode('utf8'):       # 解析下一页，将下一页的链接作为输入，递归调用parse
        nextindex = self.get_nextpage_index(nextPageText)

        if nextPageText and nextindex != -9999:       # 解析下一页，将下一页的链接作为输入，递归调用parse
            nextPage = base_url + nextPageUrl[nextindex].encode('utf8')
            yield Request(url=nextPage, callback=self.parse)

    def get_nextpage_index(self, lst):
        for pageText in lst:
            if '下一页' in pageText:
                return lst.index(pageText)

        return -9999;


    def zhidao_parse(self, response):
        # self.logger.info("LLLL ")
        html = Selector(response)
        title = html.xpath('//form[@name="search-form"]/input/@value').extract()        # 提取上面搜索框的内容
        question = html.xpath('//span[@class="ask-title "]/text()').extract_first()     # 页面当中对应的问题
        answer1 = html.xpath('//div[@accuse="aContent"]//text()').extract()             # 对应的直接答案，可以改进为只寻找最佳答案
        bestans = html.xpath('//pre[@accuse="aContent"]//text()').extract()             # 最佳答案
        item = SearchItem()

        if question is None:
            question = ""
        item['question'] = question

        item['title'] = ''.join(title)

        bestans = ''.join(bestans).encode('utf-8').replace("\n","").replace("\r","").replace("\t"," ")

        item['answer'] = ''.join(answer1).encode('utf-8').replace("\n","").replace("\r","").replace("\t"," ")

        if len(bestans) > 0:
            item['answer'] = "BEST" + bestans

        print item['title'] + "####" + item['question'] # + "####" + item['answer']
        return item

