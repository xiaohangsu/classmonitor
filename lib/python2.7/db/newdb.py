# -*- coding: utf-8 -*-
# Author: young
# Email: sujy_passion@qq.com
# Date: 2015-6-8
# Description: Provide function for news operation

from config import Users
from config import News
from pubfunc import checkItem
import uuid
import hashlib
from datetime import datetime

# 添加news
def add(data):
    #必须带有的参数
    requireList = ['newTitle', 'newContent', 'newHref', 'newCatalog', 'newTime']
    #返回的信息
    message = ''
    result = False
    user = {}
    #首先检查是否存在标题、内容、链接、时间和分类
    if checkItem(data, requireList):
        addNew = {
            'uuid': uuid.uuid1().hex,
            'newTitle': data['newTitle'],
            'newContent': data['newContent'],
            'newTime': data['newTime'],
            'newHref':data['newHref'],
            'newCatalog': data['newCatalog'],
        }
        News.insert(addNew)
        result = True
    else:
        #没有足够的参数
        result = False
        message = 'not enough params'
    #返回出去
    return {
        'uuid': addNew.get('uuid', ''),
        'result': result,
        'message': message,
    }

# 更新信息函数
def update(data):
    #必须带有的参数
    requireList = ['newCatalog']
    #返回的信息
    message = ''
    result = False
    #是否存在
    if checkItem(data, requireList):
        newsQueryCondition = {'newCatalog': data['newCatalog']}
        delResult = News.delete_many(newsQueryCondition)
        if delResult.acknowledged:
            if len(data['newsList']) > 0:
                for item in data['newsList']:
                    item['uuid'] = uuid.uuid1().hex
                addResult = News.insert_many(data['newsList'])
                if addResult.acknowledged:
                    result = True
                else:
                    message = 'insert new post fail'
            else:
                result = True
                message = 'no insert'
        else:
            message = 'delete old record fail'
            result = False
    else:
        #没有足够参数
        result = False
        message = 'not enough params'
    return {
        'result': result,
        'message': message,
    }

# 查询 信息
def get(data):
    #必须要的信息
    requireList = ['newCatalog']
    #返回的信息
    message = ''
    result = False
    newsList = []
    #查看是否存在用户
    if checkItem(data, requireList):
        newsQueryCondition = {'newCatalog': data['newCatalog']}
        #get news

        for news in News.find(newsQueryCondition):
            print news
            newsList.append({
                "uuid": news["uuid"],
                "newCatalog": news["newCatalog"],
                "newsTime": news["newTime"],
                "newHref": news["newHref"],
                })
        if len(newsList) != 0:
            result = True
            message = 'no user'
        else:
            newsList = []
            result = True
    else:
        #没有足够参数
        result = False
        message = 'not enough params'
    return {
        'result': result,
        'message': message,
        'news': newsList
    }

#根据uuid获取content
def getContent(data):
    #必须要的信息
    requireList = ['uuid']
    #返回的信息
    message = ''
    result = False
    newsContent = ''
    findNews = {}
    #查看是否存在用户
    if checkItem(data, requireList):
        newsQueryCondition = {'uuid': data['uuid']}
        #get news
        findNews = News.find_one(newsQueryCondition)
        if findNews != {}:
            newsContent = findNews.get('newContent', '')
        else:
            newContent = ''
        result = True
    else:
        #没有足够参数
        result = False
        message = 'not enough params'
    return {
        'result': result,
        'message': message,
        'newsContent': newsContent
}


#获取所有catalog种类
def getAllCatalog():
    #返回的信息
    message = ''
    result = False
    catalogList = []
    for new in News.find():
        temp = new.get('newCatalog','')
        if temp != '':
            catalogList.append(temp)
        else:
            continue
    catalogList = set(catalogList)
    catalogList = list(catalogList)
    result = True
    
    return {
        'result': result,
        'message': message,
        'catalog': catalogList
    }

