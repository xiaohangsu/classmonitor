# -*- coding: utf-8 -*-

#bulid a beautified HTML in HTMLgenerator

#class HTMLgenerator(object):
#    def __init__(self):
header = "<div id=email-body>"
footer = "</div>"

def generate(updatedList, url=""):
    html = ""
    for eOld in updatedList:
        e = eval(eOld)
        print url + e["newHref"]
        print "\n"
        html +=  ("<a title='" +  e["newTitle"] + "' href='" + url + e["newHref"] + "'  >" + e["newContent"] + "</a><br/>")
    html =  header + html + footer
    return html