# -*- coding: utf-8 -*-
import scrapy
from scrapy_jwcSYSU.items import jwcsysuItem
class weiboSpider(scrapy.Spider):
  name = "weiboSpider"
  allowed_domains = ["tieba.baidu.com"]
  start_urls = ["http://tieba.baidu.com/魔兽世界?fr=ala0"
  ]

  def parse(self, response):
    print 'response'
    for div in response.css("div[class=threadlist_lz]"):
      item = jwcsysuItem()
      item["newTitle"] = "wow"
      print '!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
      item["newContent"] = div.css("a::(attr=title)").extract()
      item["newHref"] = div.css("a::(attr=href)").extract()
      print item
      yield item
