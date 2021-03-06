# -*- coding: utf-8 -*-
from scrapy_jwcSYSU.items import jwcsysuItem
import scrapy
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider

from scrapy_jwcSYSU.settings import START_URLS, RULES
from scrapy.contrib.spiders import CrawlSpider


class jwcsysuSpider(CrawlSpider):
  name = "jwcsysuSpider"
  allowed_domains = ["jwc.sysu.edu.cn"]
  start_urls = START_URLS
  rules = RULES

  def parse_item(self, response):
    item = jwcsysuItem()
    try:
      item["newCatalog"] = response.css("div[class=sec_art_list]").css("a").extract()[2].split("<")[-2].split(">")[-1]
      item["newTitle"] = response.css("div[class=art_content]").css("h1::text").extract()[0]
      item["newContent"] = response.css("div[class=content]").extract()[0]
      item["newHref"] = response.url
      item["newTime"] = response.css("div[class=art_property]").extract()[0][-62:-52]
      return item
    except Exception, e:
      return None

    #print item

  #parse default to parse the Title without Using Rule

