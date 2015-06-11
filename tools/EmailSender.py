# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
mailto_list=["709916025@qq.com", "suruoyanmashiro@qq.com", "602028597@qq.com", "7940175@qq.com"] 
mail_host="smtp.163.com"  #设置服务器
mail_user="kiadragon"    #用户名
mail_pass="20019110"   #口令 
mail_postfix="163.com"  #发件箱的后缀
  
def send_mail(sub,content):  #to_list：收件人；sub：主题；content：邮件内容
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"   #这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content,_subtype='html',_charset='utf-8')    #创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub    #设置主题
    msg['From'] = me  
    msg['To'] = ";".join(mailto_list)  
    try:  
        s = smtplib.SMTP()  
        s.connect(mail_host)  #连接smtp服务器
        s.login(mail_user,mail_pass)  #登陆服务器
        s.sendmail(me, mailto_list, msg.as_string())  #发送邮件
        s.close()
        print "Send Email Successed!"  
        return True
    except Exception, e:  
        print str(e)
        print "Send Email Failed!" 
        return False