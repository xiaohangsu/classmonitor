# -*- coding: utf-8 -*-
# send Email using EmailSender & HTMLgenerator

from db import newdb, userdb
from tools import EmailSender, HTMLgenerator

def sendEmail():
    print newdb.get({"newCatalog":"学院概况"})
    print userdb.getAllUserInfo()

sendEmail()