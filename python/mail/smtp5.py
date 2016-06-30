#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: smtp1.py
# Created Time: 2016年06月28日 星期二 10时51分17秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import smtplib
from email.mime.text import MIMEText


HOST = "1.1.1.1"
PORT = "25"
SUBJECT = u"官网流量数据报表"
TO = "tomail"
FROM = "frommail"


msg = MIMEText("""
    <table width="800" border="0" cellspacing="0" cellpadding="4">
      <tr>
        <td bgcolor="#CECFAD" height="20" style="font-size:14px">官网数据  <a href="www.w66.com">更多>></a></td>
      </tr>
      <tr>
        <td bgcolor="#EFEBDE" height="100" style="font-size:13px">
        1) 访问量信息<br>
           &nbsp;&nbsp;日访问量:<font color=red>152433</font><br>
           &nbsp;&nbsp;访问次数:23651<br>
           &nbsp;&nbsp;页面浏览量:45123<br>
           &nbsp;&nbsp;点击数:545122<br>
           &nbsp;&nbsp;数据流量:504Mb<br>

        2) 状态码信息<br>
           &nbsp;&nbsp;500:105<br>
           &nbsp;&nbsp;404:3264<br>
           &nbsp;&nbsp;503:214<br>

        3) 访客浏览器信息<br>
           &nbsp;&nbsp;IE:50%<br>
           &nbsp;&nbsp;firefox:10%<br>
           &nbsp;&nbsp;chrome:30%<br>
           &nbsp;&nbsp;other:10%<br>

        4）页面信息<br>
        &nbsp;&nbsp;/index.php 42153<br>
        &nbsp;&nbsp;/view.php 21451<br>
        &nbsp;&nbsp;/login.php 5112<br>
       </td>
      </tr>
    </table>""","html","utf-8")


print msg
msg['Subject'] = SUBJECT
msg['From'] = FROM
msg['To'] = TO
print msg


try:
    server = smtplib.SMTP()
    server.connect(HOST, PORT)
    #server.starttls()
    #server.login("test@gmail.com","123456")
    server.sendmail(FROM, TO, msg.as_string())
    server.quit()
    print "send mail success!"
except Exception, e:
    print "Error: " + str(e)

