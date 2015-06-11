# -*- coding: utf-8 -*-
# Author: young
# Email: sujy_passion@qq.com
# Date: 2015-6-8
# Description: The configuration of the database
import pymongo


DATABASE_NAME = 'classmonitor'

client = pymongo.MongoClient('localhost', 27017)

database = client[DATABASE_NAME]

Users = database['user']
News = database['new']


