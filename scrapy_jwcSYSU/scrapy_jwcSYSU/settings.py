# -*- coding: utf-8 -*-

# Scrapy settings for scrapyTest project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors import LinkExtractor

BOT_NAME = 'scrapy_jwcSYSU'

SPIDER_MODULES = ['scrapy_jwcSYSU.spiders']
NEWSPIDER_MODULE = 'scrapy_jwcSYSU.spiders'
ITEM_PIPELINES = {
    'scrapy_jwcSYSU.pipelines.jwcsysuJsonExportPipeline': 800
}

START_URLS = {
    'http://jwc.sysu.edu.cn/StudentMan/Index.aspx', # 中山大学教务处 教务学籍
    'http://jwc.sysu.edu.cn/TeachReseach/Index.aspx', # 中山大学教务处 教学研究
    'http://jwc.sysu.edu.cn/TeachPractice/Index.aspx', # 中山大学教务处 教学实践
    'http://jwc.sysu.edu.cn/Coopration/Index.aspx', # 中山大学教务处 合作交流
    'http://jwc.sysu.edu.cn/zhgl/Index.aspx', # 中山大学教务处 综合管理科
    'http://jwc.sysu.edu.cn/gxyj/Index.aspx', # 中山大学教务处 教学研究科
    'http://jwc.sysu.edu.cn/jxsj/Index.aspx', # 中山大学教务处 教学实践科
    'http://jwc.sysu.edu.cn/departmentnews/Index.aspx', # 中山大学教务处 院务教务信息
}

RULES = [
              Rule(LinkExtractor(allow=("/Item/?")) ,callback = "parse_item", follow=True),
  ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapyTest (+http://www.yourdomain.com)'
