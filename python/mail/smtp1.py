#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: smtp1.py
# Created Time: 2016年06月28日 星期二 10时51分17秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import smtplib
import string


HOST = "1.1.1.1"
SUBJECT = "Test email from python"
TO = "tomail"
FROM = "frommail"
text = "Python send mail test!!!"
BODY = string.join((
    "From: %s" % FROM,
    "To: %s" % TO,
    "Subject: %s" % SUBJECT,
    "",
    text
), "\r\n")

server = smtplib.SMTP()

server.connect(HOST, "25")

print server.ehlo()
server.starttls()
print server.ehlo()

print 'login start:'
server.login("frommail","IVI66.NET")
print 'login end:'

server.sendmail(FROM, TO, BODY)
server.quit()
