# -*- coding: utf-8 -*-
import scrapy
from scrapy_ssSYSU.items import ScrapySssysuItem
from scrapy_ssSYSU.settings import START_URLS

class ssSYSUSpider(scrapy.Spider):
    name = "ssSYSUSpider"
    allowed_domains = ["http://ss.sysu.edu.cn/"]
    start_urls = START_URLS

    def parse(self, response):
        print "Start Parse--------------- :"
        item = ScrapySssysuItem()
        item["newCatalog"] = response.css("a[id=ctl00_ContentPlaceContent_ColumnPath1_rtPath_ctl01_lkColumn]").extract()[0][-15:-11]
        for tr in response.css("tr[bgcolor=White]"):
            #print tr.css("td").extract()[2][-21:-12].encode("utf-8") +"\n"
            item["newTitle"] = tr.css("a::text").extract()[0]
            item["newHref"] = tr.css("a::attr(href)").extract()[0]
            #item["newColumn"] = tr.css("td span::text").extract()[0]
            item["newContent"] = "There should be some text content."
            item["newTime"] = tr.css("td").extract()[2][-21:-12].strip(">")
            yield item
        #print response
