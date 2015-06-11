# -*- coding: utf-8 -*-

# Scrapy settings for scrapy_ssSYSU project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'scrapy_ssSYSU'

SPIDER_MODULES = ['scrapy_ssSYSU.spiders']
NEWSPIDER_MODULE = 'scrapy_ssSYSU.spiders'

ITEM_PIPELINES = {
    'scrapy_ssSYSU.pipelines.ScrapySssysuPipeline': 800
}

FILE_NAME = "data.json"

START_URLS = (
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=24', # 软件学院  - 学院概况  - 学院简介
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=25', # 软件学院  - 学院概况  - 管理机构
        'http://ss.sysu.edu.cn/informationsystem/CollegeTeacher.aspx?id=29', # 软件学院  - 学院概况  - 学院领导
        'http://ss.sysu.edu.cn/informationsystem/CollegeTeacher.aspx?id=34', # 软件学院  - 学院概况  - 师资力量
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=35', # 软件学院  - 学院概况  - 学院纪事
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=36', # 软件学院  - 新闻中心  - 学院新闻
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=37', # 软件学院  - 新闻中心  - 招生信息
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=92', # 软件学院  - 新闻中心  - Office hour安排表
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=38', # 软件学院  - 新闻中心  - 学工信息
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=39', # 软件学院  - 新闻中心  - 本科教务
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=40', # 软件学院  - 招生信息  - 最新信息
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=41', # 软件学院  - 招生信息  - 招生简章
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=31', # 软件学院  - 招生信息  - 招生专业
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=44', # 软件学院  - 招生信息  - 招生联系
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=33', # 软件学院  - 教学教务  - 研究生教务
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=45', # 软件学院  - 教学教务  - 本科生教务
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=46', # 软件学院  - 教学教务  - 专业设置
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=51', # 软件学院  - 教学教务  - 联系教务办
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=53', # 软件学院  - 学生工作  - 学工信息
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=54', # 软件学院  - 学生工作  - 学生党建
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=55', # 软件学院  - 学生工作  - 学生团建
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=56', # 软件学院  - 学生工作  - 学生会
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=57', # 软件学院  - 学生工作  - 学生科技
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=95', # 软件学院  - 学生工作  - 研究生会
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=58', # 软件学院  - 学生工作  - 办事指南
        'http://ss.sysu.edu.cn/informationsystem/ArticleList.aspx?id=60', # 软件学院  - 学生工作  - 联系学工办
        'http://ss.sysu.edu.cn/InformationSystem/ArticleList.aspx?id=72' # 软件学院  - 学术科研  - 学术交流
)

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_ssSYSU (+http://www.yourdomain.com)'
