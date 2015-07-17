# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

from scrapy_ssSYSU.settings import FILE_NAME
from db import newdb
from tools import EmailSender, HTMLgenerator
from newsCatalog import NEWSCATALOG
class ScrapySssysuPipeline(object):
    def __init__(self):
        self.news = set()
        self.updatedNews = set()
        self.newsList = []
        f = open(FILE_NAME)
        for line in f:
            self.news.add(line[0:-1])

        f.close()
        self.file = open(FILE_NAME, "wb")
        for s in NEWSCATALOG["data"][1]["list"]:
            newdb.update({'newCatalog': s, 'newsList': []})

    def process_item(self, item, spider):
        self.updatedNews.add(json.dumps(dict(item), ensure_ascii=False, sort_keys=True).encode('utf-8'))
        line = json.dumps(dict(item), ensure_ascii=False, sort_keys=True).encode('utf-8') + "\n"
        self.newsList.append(dict(item))
        self.file.write(line)
        return item

    def close_spider(self, spider):
        
        print "Here is Updated News !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n"
        for new in self.newsList:
            newdb.add(new)
        #self.updatedNews -= self.news
        self.updatedNews = list(self.updatedNews)
        self.updatedNews.sort()
        EmailSender.send_mail("SpiderEmailTest", HTMLgenerator.generate(self.updatedNews))
        self.file.close()
