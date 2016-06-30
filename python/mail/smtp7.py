#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: smtp1.py
# Created Time: 2016年06月28日 星期二 10时51分17秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


HOST = "1.1.1.1"
PORT = "25"
SUBJECT = u"官网业务服务质量周报"
TO = ["tomail"]
FROM = "sendmail"
CC = ["copymail"]


tolist = ','.join(TO)
cclist = ','.join(CC)


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msgtext = MIMEText("<font color=red>官网业务周平均延时图表:<br><img src=\"cid:weekly\" border=\"1\"><br>详细内容见附件.</font>","html","utf-8")
msg = MIMEMultipart('related')
msg.attach(msgtext)
msg.attach(addimg("img/weekly.png","weekly"))


attach = MIMEText(open("doc/week_report.xlsx","rb").read(), "base64", "utf-8")
attach["Content-Type"] = "application/octet-stream"
attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("utf-8")

# qq mail
#attach["Content-Disposition"] = "attachment; filename=\"业务服务质量周报(12周).xlsx\"".decode("utf-8").encode("gb18030")
msg.attach(attach)


msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = tolist
msg['Cc'] = cclist


try:
    server = smtplib.SMTP()
    server.connect(HOST, PORT)
    #server.starttls()
    #server.login("test@gmail.com","123456")
    server.sendmail(FROM, TO + CC, msg.as_string())
    server.quit()
    print "send mail success!"
except Exception, e:
    print "Error: " + str(e)
