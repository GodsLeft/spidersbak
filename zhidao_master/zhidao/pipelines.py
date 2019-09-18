# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class ZhidaoPipeline(object):
    def __init__(self):
        self.file = open('item.txt', 'w')

    def process_item(self, item, spider):
        if len(item["question"]) > 1:
            self.file.write(item["title"] + "\t" + item["question"] + "\t" + item["answer"] + "\n")
            self.file.flush()
            return item
        else:
            raise DropItem("The question has no answer: %s" % item["question"])
