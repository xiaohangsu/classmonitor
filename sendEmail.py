# -*- coding: utf-8 -*-
# send Email using EmailSender & HTMLgenerator

from db import newdb, userdb
from tools import EmailSender, HTMLgenerator

def sendEmail(email, subscribe):
    result = False
    newsList = []
    for s in subscribe: 
        newsList.append(newdb.get({'newCatalog': s})["news"])
    print "send"
    result = EmailSender.send_mail("中国好班长订阅内容", HTMLgenerator.generateForSendEmail(newsList), [email])
    return {"result": result}