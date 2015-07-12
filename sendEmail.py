# -*- coding: utf-8 -*-
# send Email using EmailSender & HTMLgenerator

from db import newdb, userdb
from tools import EmailSender, HTMLgenerator

def sendEmail():
    users = userdb.getAllUserInfo()
    userList = users["userList"]
    userCount = users["userCount"]
    for user in userList:
        for catalog in user["subscribe"]:
            print newdb.get({"newCatalog": catalog})

sendEmail()