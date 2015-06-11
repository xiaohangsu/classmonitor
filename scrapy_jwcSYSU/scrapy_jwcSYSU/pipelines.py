# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
from scrapy.contrib.exporter import JsonItemExporter
from db import newdb

import HTMLgenerator
import EmailSender

class jwcsysuJsonExportPipeline(object):
    def __init__(self):
        self.news = set()
        self.updatedNews = set()
        f = open("data.json")
        for line in f:
            self.news.add(line[0:-1])

        f.close()
        self.file = open("data.json", "wb")

    def process_item(self, item, spider):
        self.updatedNews.add(json.dumps(dict(item), ensure_ascii=False).encode('utf-8'))
        line = json.dumps(dict(item), ensure_ascii=False).encode('utf-8') + "\n"
        self.file.write(line)
        return item

    def close_spider(self, spider):
        
        print "Here is Updated News !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        print list(self.updatedNews)
        self.updatedNews -= self.news
        
        self.updatedNews = list(self.updatedNews)
        EmailSender.send_mail("SpiderEmailTest", HTMLgenerator.generate(self.updatedNews))
        self.file.close()
