# -*- coding: utf-8 -*-
import scrapy
from scrapy_jwcSYSU.items import jwcsysuItem
class tiebaSpider(scrapy.Spider):
  name = "tiebaSpider"
  allowed_domains = ["tieba.baidu.com"]
  start_urls = ["http://tieba.baidu.com/魔兽世界?fr=ala0"
  ]

  def parse(self, response):
    print 'response'
    for div in response.css("a[class=j_th_tit] "):
      item = jwcsysuItem()
      item["newTitle"] = "wow"
      item["newContent"] = div.xpath('@title').extract()[0]
      item["newHref"] = div.xpath('@href').extract()[0]
      print item
      yield item
