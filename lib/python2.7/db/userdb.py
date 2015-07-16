# -*- coding: utf-8 -*-
# Author: young
# Email: sujy_passion@qq.com
# Date: 2015-6-8
# Description: Provide function for user operation

from config import Users
from config import News
from pubfunc import checkItem
import uuid
import hashlib
from datetime import datetime

#注册用户
def register(data):
    #必须带有的参数
    requireList = ['loginID', 'password']
    #返回的信息
    message = ''
    result = False
    user = {}
    #首先检查是否存在loginID 和 password
    if checkItem(data, requireList):
        #检查是否存在的相同的loginID
        queryCondition = {'loginID': data['loginID']}
        user = Users.find_one(queryCondition)
        if user is not None:
            user = {}#if user is found, clear user. Not to return the uuid.
            result = False
            message = 'loginID has been used!'
        else:
            #开始加入数据库
            newUser = {
                'uuid': uuid.uuid1().hex,
                'loginID': data['loginID'],
                'password': hashlib.sha1(data['password']).hexdigest(),
                'name': data.get('name', ''),
                'subscribe': data.get('subscribe', []),
                'email': data.get('email', ''),
            }
            Users.insert(newUser)
            user = newUser
            result = True

    else:
        #没有足够的参数
        result = False
        message = 'not enough params'
    #返回出去
    return {
        'uuid': user.get('uuid', ''),
        'result': result,
        'message': message,
    }

#登陆用户
def login(data):
    #必须带有的参数
    requireList = ['loginID', 'password']
    #返回的信息
    message = ''
    result = False
    uuid = ""
    user = {}
    #首先检查是否存在loginID 和 password
    if checkItem(data, requireList):
        #检查是否存在的相同的loginID
        queryCondition = {'loginID': data['loginID']}
        user = Users.find_one(queryCondition)
        if user is None:
            result = False
            message = 'no user exist'
        else:
            if data['loginID'] == user['loginID'] and \
            hashlib.sha1(data['password']).hexdigest() == user['password']:
                uuid = user["uuid"]
                #删除敏感信息
                del user['password']
                del user['_id']
                result = True
            else:
                user = {}#if password is wrong, clear user. Not to return the uuid.
                result = False
                message = 'loginID or password error'

    else:
        #没有足够的参数
        result = False
        message = 'not enough params'
    #返回出去
    return {
        'result': result,
        'message': message,
        'uuid': uuid,
        'user': user
    }

# 更新用户信息函数
def update(data):
    #必须带有的参数
    requireList = ['uuid']
    #返回的信息
    message = ''
    result = False
    user = {}
    #是否存在用户
    if checkItem(data, requireList):
        userQueryCondition = {'uuid': data['uuid']}
        user = Users.find_one(userQueryCondition)
        if user is None:
            result = False
            message = 'no user'
        else:
            #不更新uuid
            del data['uuid']
            #跟新密码
            if data.get('password', '') != '':
                data['password'] = hashlib.sha1(data['password']).hexdigest()
            Users.update({'uuid': user['uuid']}, {"$set": data})
            user = Users.find_one(userQueryCondition)
            #删除敏感信息
            del user['password']
            del user['_id']
            result = True
    else:
        #没有足够参数
        result = False
        message = 'not enough params'
    return {
        'result': result,
        'message': message,
        'user': user,
    }


# 查询用户信息
def get(data):
    #必须要的信息
    requireList = ['uuid']
    #返回的信息
    message = ''
    result = False
    user = {}
    #查看是否存在用户
    if checkItem(data, requireList):
        userQueryCondition = {'uuid': data['uuid']}
        #get user
        user = Users.find_one(userQueryCondition)
        if user is None:
            result = False
            message = 'no user'
        else:
            #删除敏感信息
            del user['password']
            del user['_id']
            result = True
    else:
        #没有足够参数
        result = False
        message = 'not enough params'
    return {
        'result': result,
        'message': message,
        'user': user
    }

# 查询用户个数和信息
def getAllUserInfo():
    #返回的信息
    message = ''
    result = False
    userList = []
    count = 0;
    for user in Users.find():
        userInfo = {
            'loginID':user.get('loginID',''),
            'subscribe':user.get('subscribe',[]),
        }
        userList.append(userInfo)
        count += 1
    result = True;
    return {
        'result': result,
        'message': message,
        'userList': userList,
        'userCount': count
    }

# 查询用户个数和信息
def getUserInfo(data):
    #返回的信息
    requireList = ['loginID', 'password']
    #返回的信息
    message = ''
    result = False
    uuid = ""
    user = {}
    #首先检查是否存在loginID 和 password
    if checkItem(data, requireList):
        #检查是否存在的相同的loginID
        queryCondition = {'loginID': data['loginID']}
        user = Users.find_one(queryCondition)
        if user is None:
            result = False
            message = 'no user exist'
        else:
            if data['loginID'] == user['loginID'] and \
            hashlib.sha1(data['password']).hexdigest() == user['password']:
                uuid = user["uuid"]
                #删除敏感信息
                del user['password']
                del user['_id']
                result = True
            else:
                user = {}#if password is wrong, clear user. Not to return the uuid.
                result = False
                message = 'loginID or password error'

    else:
        #没有足够的参数
        result = False
        message = 'not enough params'
    #返回出去
    return {
        'result': result,
        'message': message,
        'user': user
    }
