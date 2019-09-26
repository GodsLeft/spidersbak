# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item

#class MeituanantItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    pass

class DianpingItem(Item):
    shopname = Field()
    foodtype = Field()
    #shoplevel = Field()
    #shopurl = Field()
    #commentnum = Field()
    #avgcost = Field()
    #taste = Field()
    #envi = Field()
    #service = Field()
    #loc = Field()
