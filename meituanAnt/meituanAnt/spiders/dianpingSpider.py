#coding:utf-8
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from dianpingAnt.items import DianpingItem
from scrapy.spiders import CrawlSpider
import re

# 这个爬虫目的为了爬取分类信息
class dianpingSpider(CrawlSpider):
    name = "dianpingSpider"
    allowed_domains = [ "dianping.com" ]

    start_urls = [
        #'https://www.dianping.com/shopall/9/0',                  # 这里的9代表一个城市，关于城市可以自己限定几个
        #'https://www.dianping.com/search/category/5/10/g1338',   # 这里的5代表城市，10代表美食类，g1338代表私房菜

        # 美食类
        #'https://www.dianping.com/search/category/5/10',   # 这里的5代表城市，10代表美食类，g1338代表私房菜
        #'https://www.dianping.com/search/category/7/10',    # 深圳
        #'https://www.dianping.com/search/category/8/10',    # 成都
        #'https://www.dianping.com/search/category/9/10',    # 重庆
        #'https://www.dianping.com/search/category/10/10',    # 天津
        #'https://www.dianping.com/search/category/11/10',    # 宁波
        #'https://www.dianping.com/search/category/12/10',    # 扬州
        #'https://www.dianping.com/search/category/13/10',    # 无锡
        #'https://www.dianping.com/search/category/14/10',    # 福州
        #'https://www.dianping.com/search/category/15/10',    # 厦门
        #'https://www.dianping.com/search/category/16/10',    # 武汉
        #'https://www.dianping.com/search/category/17/10',    # 西安

        # 购物类
        #'https://www.dianping.com/search/category/5/20/',
        'https://www.dianping.com/search/category/7/20',    # 深圳
        'https://www.dianping.com/search/category/8/20',    # 成都
        'https://www.dianping.com/search/category/9/20',    # 重庆
        'https://www.dianping.com/search/category/10/20',    # 天津
        'https://www.dianping.com/search/category/11/20',    # 宁波
        'https://www.dianping.com/search/category/12/20',    # 扬州
        'https://www.dianping.com/search/category/13/20',    # 无锡
        'https://www.dianping.com/search/category/14/20',    # 福州
        'https://www.dianping.com/search/category/15/20',    # 厦门
        'https://www.dianping.com/search/category/16/20',    # 武汉
        'https://www.dianping.com/search/category/17/20',    # 西安
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

        pageUrl = selector.xpath('//div[@class="page"]/a/@href').extract()[0]
        for p in range(1, pg):
            newurl = re.sub(r'p[0-9]+', "p"+str(p), response.urljoin(pageUrl))
            yield Request(newurl, callback=self.parse_list)

       # pageUrls = selector.xpath('//div[@class="page"]/a/@href').extract()
       # print pageUrls
       # for pageurl in pageUrls:
       #     url = response.urljoin(pageurl)
       #     yield Request(url, callback=self.parse_list)

    # 解析网页并生成item对象
    def parse_list(self, response):
        item = DianpingItem()
        selector = Selector(response)
        div = selector.xpath('//div[@id="shop-all-list"]/ul/li')
        for dd in div:
            shopnames = dd.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
            item['shopname'] = shopnames[0]

            foodtypes = dd.xpath('div[2]/div[3]/a[1]/span/text()').extract()
            item['foodtype'] = foodtypes[0]
            # shopurls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
            # item['shopurl'] = 'http://www.dianping.com' + str(shopurls[0])

            yield item
