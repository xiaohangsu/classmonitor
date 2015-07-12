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
        self.currentCatalog = ""
        self.currentCatalogList = []
        
        f = open("data.json")
        for line in f:
            self.news.add(line[0:-1])

        f.close()
        self.file = open("data.json", "wb")

    def process_item(self, item, spider):
        self.updatedNews.add(json.dumps(dict(item), ensure_ascii=False, sort_keys=True).encode('utf-8'))
        line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True).encode('utf-8') + "\n"
        
        if self.currentCatalog != item["newCatalog"] and self.currentCatalog != "":
            newdb.update({'newCatalog': self.currentCatalog, 'newsList': self.currentCatalogList})
            self.currentCatalogList = []
        else :
            self.currentCatalogList.append(dict(item))
        self.currentCatalog = item["newCatalog"]

        self.file.write(line)
        return item

    def close_spider(self, spider):
        
        print "Here is Updated News !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        
        # 去重发送邮件
        self.updatedNews -= self.news
        
        self.updatedNews = list(self.updatedNews)
        #print list(self.updatedNews)
        self.updatedNews.sort()
        EmailSender.send_mail("SpiderEmailTest", HTMLgenerator.generate(self.updatedNews))
        self.file.close()
