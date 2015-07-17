# -*- coding: utf-8 -*-

# this means when you are not sucessful send email. It will send you  an alternative Email

from tools import HTMLgenerator

ERROR_CONTENT = HTMLgenerator.generate(['{"newCatalog": "邮件发送错误","newTitle": "抓取内容可能包含敏感字符,请访问我们的网站.","newHref": "www.baidu.com","newTime": "","newContent": "由于抓取内容可能包含敏感字符,所以无法发送到您的邮箱,请访问我们的网站."}'])