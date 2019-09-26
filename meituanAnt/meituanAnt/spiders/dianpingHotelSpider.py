#coding:utf-8
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from dianpingAnt.items import DianpingItem
from scrapy.spiders import CrawlSpider
import re

# 这个爬虫目的为了爬取分类信息
class dianpingHotelSpider(CrawlSpider):
    name = "dianpingHotelSpider"
    allowed_domains = [ "dianping.com" ]

    start_urls = [
        # hotel
        'https://www.dianping.com/shenzhen/hotel',   # 每页展示15条，14页的数据
        'https://www.dianping.com/beijing/hotel',   # 每页展示15条，14页的数据
        'https://www.dianping.com/shanghai/hotel',   # 每页展示15条，14页的数据
        'https://www.dianping.com/guangzhou/hotel',
        'https://www.dianping.com/nanjing/hotel',
        'https://www.dianping.com/zhengzhou/hotel',
        'https://www.dianping.com/wuhan/hotel',
        'https://www.dianping.com/tianjin/hotel',
        'https://www.dianping.com/wulumuqi/hotel',
        'https://www.dianping.com/haerbin/hotel',
    ]

    def parse_start_url(self, response):
        # url = 'https://www.dianping.com/shopall/9/0',  # 这里的9代表一个城市，关于城市可以自己限定几个
        for url in self.start_urls:
            yield Request(url, callback=self.parse_list_first)


    # 解析下一页的url
    # 在这里应当获取当前页面的下一页，而不是获取全部页面，否则会无法解析 "..." 这个符号
    def parse_list_first(self, response):
        selector = Selector(response)
        pg = 0
        pages = selector.xpath('//div[@class="page"]/a/@data-ga-page').extract()
        if len(pages) > 0:
            pg = pages[len(pages) - 2]
        pg = int(str(pg)) + 1

        pageUrl = selector.xpath('//div[@class="page"]/a/@href').extract()[1]
        for p in range(1, pg):
            newurl = re.sub(r'p[0-9]+', "p"+str(p), response.urljoin(pageUrl))
            #print newurl
            yield Request(newurl, callback=self.parse_list)


    # 解析网页并生成item对象
    def parse_list(self, response):
        item = DianpingItem()
        selector = Selector(response)

        div = selector.xpath('//div[@class="content"]/ul/li')
        for dd in div:
            shopname = dd.xpath('div[1]/div[1]/h2/a/text()').extract()
            item['shopname'] = shopname[0]
            #print shopname[0]

            types = dd.xpath('div[1]/div[1]/p[2]/span[1]/text()').extract()
            item['foodtype'] = types[0]
            #print types[0]

            yield item
