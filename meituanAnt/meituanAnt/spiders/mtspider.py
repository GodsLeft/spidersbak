#coding:utf-8
import scrapy
from scrapy.http import Request
from scrapy.selector import Selector
from dianpingAnt.items import DianpingItem
from scrapy.spiders import CrawlSpider
import time
import sys

#class mtspider(scrapy.Spider):
class mtspider(CrawlSpider):
    name = "meituanspider"
    allowed_domains = [
        #"meituan.com"
        "dianping.com"
        #'http://www.dianping.com/search/category/1/10'
    ]

    # 起始url
    start_urls = [
        #"http://www.meituan.com"
        'http://www.dianping.com/search/category/1/10'
    ]

    location = ['r5', 'r2', 'r6', 'r1', 'r3', 'r4', 'r12', 'r10', 'r7', 'r9', 'r13', 'r8', 'r5937', 'r5938', 'r5939',
                'r8846', 'r8847', 'c3580', 'r801', 'r802', 'r804', 'r865', 'r860', 'r803', 'r835', 'r812', 'r842',
                'r846', 'r849', 'r806', 'r808', 'r811', 'r839', 'r854']

    foodtype = ['g101', 'g113', 'g132', 'g112', 'g117', 'g110', 'g116', 'g111', 'g103', 'g114', 'g508', 'g102', 'g115',
                'g109', 'g106', 'g104', 'g248', 'g3243', 'g251', 'g26481', 'g203', 'g107', 'g105', 'g108', 'g215',
                'g247', 'g1338', 'g1783', 'g118']

    def parse_start_url(self, response):
        url = 'http://www.dianping.com/search/category/1/10'
        for lbs in self.location:
            for ft in self.foodtype:
                url = 'http://www.dianping.com/search/category/1/10/%s%s' % (lbs, ft)
                yield Request(url, callback=self.parse_list_first)

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
            #shopurls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
            #item['shopurl'] = 'http://www.dianping.com' + str(shopurls[0])

            yield item

    # 解析下一页的url
    def parse_list_first(self, response):
        selector = Selector(response)
        pg = 0
        pages = selector.xpath('//div[@class="page"]/a/@data-ga-page').extract()

        if len(pages) > 0:
            pg = pages[len(pages) - 2]
            print pg + " #### pg"

        pg = int(str(pg)) + 1

        url = str(response.url)

        for p in range(1, pg):
            ul = url + 'p' + str(p)
            yield Request(ul, callback=self.parse_list)


    #def parse_0(self, response):
    #    item = DianpingItem()
    #    selector = Selector(response)

    #    div = selector.xpath('//div[@id="shop-all-list"]/ul/li')
    #    for dd in div:
    #        shopnames = dd.xpath('div[2]/div[1]/a[1]/h4/text()').extract()
    #        item['shopname'] = shopnames[0]

    #        shopurls = dd.xpath('div[2]/div[1]/a[1]/@href').extract()
    #        item['shopurl'] = 'http://www.dianping.com' + str(shopurls[0])

    #        foodtypes = dd.xpath('div[2]/div[3]/a[1]/span/text()').extract()
    #        item['foodtype'] = foodtypes[0]

