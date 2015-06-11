# -*- coding: utf-8 -*-
import scrapy
from scrapy_jwcSYSU.items import jwcsysuItem

class jwcsysuSpider(scrapy.Spider):
  name = "jwcsysuSpider"
  allowed_domains = ["jwc.sysu.edu.cn"]
  start_urls = ["http://jwc.sysu.edu.cn/information/Index.aspx"
  ]

  def parse(self, response):
    print "Start ScrapyING\n"
    for div in response.css("div[class=art_list]"):
      item = jwcsysuItem()
      item["newTitle"] = div.css("h2 a::text").extract()[0]
      for li in div.css("li"):
        item["newContent"] = li.css("a::text").extract()[0]
        item["newHref"] = li.css("a::attr(href)").extract()[0]
        #print item["newContent"].encode("utf-8") + "\n", item["newHref"].encode("utf-8") + "\n"
        yield item
