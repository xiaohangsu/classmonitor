# -*- coding: utf-8 -*-
import scrapy
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy_ssSYSU.items import ScrapySssysuItem
from scrapy_ssSYSU.settings import START_URLS, RULES

from scrapy.contrib.spiders import Rule,CrawlSpider
from scrapy.contrib.linkextractors import LinkExtractor

class ssSYSUSpider(CrawlSpider):
    name = "ssSYSUSpider"
    allowed_domains = ["ss.sysu.edu.cn"]
    start_urls = START_URLS
    rules = (
        Rule(LinkExtractor(allow=("/informationsystem/Article.aspx?")) ,callback = "parse_item"),
    )


    def parse_item(self, response):
        print "Start Parse--------------- :"
        item = ScrapySssysuItem()
        item["newTitle"] = response.css("div[class=articleTitle]").extract()[0][26:-6]
        item["newHref"] = response.url
        item["newTime"] = response.css("span[id=ctl00_ContentPlaceContent_lblDate]").extract()[0][45:-7]
        item["newContent"] = response.css("div[class=articleContent]").extract()[0]
        item["newCatalog"] = response.css("a[id=ctl00_ContentPlaceContent_ColumnPath1_rtPath_ctl01_lkColumn]").extract()[0][118:-11]
        print "item"
        yield item

