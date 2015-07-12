# -*- coding: utf-8 -*-

#bulid a beautified HTML in HTMLgenerator

#class HTMLgenerator(object):
#    def __init__(self):
header = "<div style='background: #fff; width: 600px; padding: 20px 30px;\
margin: 0 auto;'><div style='padding: 15px 0;'><table border='0' cellspacing='0' cellpadding='0'><tbody>"
footer = "</tbody>\
</table>\
<div style='padding: 15px 0 5px; margin: 0; font: 14px Helvetica, Arial, sans-serif; color: #222; line-height: 1.6;'>联系我们：<a style='font: 14px Helvetica, Arial, sans-serif; color: #943907; margin: 0 5px 0 15px;' \
 href='https://github.com/kiadragon/classmonitor/issues' target='_blank'>GitHub</a> \
  <a style='font: 14px Helvetica, Arial, sans-serif; color: #943907;' href='mailto:sxhdragon@gmail.com' target='_blank'>Email</a> \
  <a style='font: 14px Helvetica, Arial, sans-serif; color: #943907; margin: 0 5px;' href='#' target='_blank'>关于我们</a> \
<div style='height: 20px; padding-top: 20px; font: 14px Helvetica, Arial, sans-serif; text-align: right;'><a style='color: #000;' \
 href='http://www.cocoachina.com' target='_blank'>中国好班长 classmonitor</a></div>"

def generate(updatedList, url=""):
    html = ""
    currentCatalog = ""
    count = 0
    for eOld in updatedList:
        e = eval(eOld)
        count = count + 1
        if currentCatalog != e["newCatalog"]:

            currentCatalog = e["newCatalog"]
            html += ("<td><h3 style='height: 30px; color: #943907; width: 250px; margin: 0; padding: 15px 0 2px; border-bottom: 1px solid #943907; line-height: 30px; font-size: 18px;'>" + \
                e["newCatalog"] + "</h3></td>")
        html +=  ("<tr><td style='border-bottom: 1px dotted #ccc; padding: 15px 0;'><a style='text-decoration: none; font: 14px Helvetica, Arial, sans-serif; color: #0088e7;' href='" + \
            url + e["newHref"] + "' target='_blank'>" + e["newTitle"] + "</a><p style='font: 14px Helvetica, Arial, sans-serif; color: #888; padding: 15px 0 0; margin: 0; line-height: 1.6;'><span style='border-bottom:1px dashed #ccc;' t='5' times=''>" + \
            e["newTime"] + "</span></p></td></tr>")
        if count == 2:
            break
    html =  header + html + footer
    
    f = open("1.html", "wb")
    f.write(html[0:-1])
    f.close()
    return html