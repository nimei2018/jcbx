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
SUBJECT = u"业务性能数据报表"
TO = ["ccmail","tomail"]
FROM = "frommail"
CC = ["ccmail"]


tolist = ','.join(TO)
cclist = ','.join(CC)


def addimg(src, imgid):
    fp = open(src, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    msgImage.add_header('Content-ID', imgid)
    return msgImage


msgtext = MIMEText("""
    <table width="600" border="0" cellspacing="0" cellpadding="4">
      <tr bgcolor="#CECFAD" height="20" style="font-size:14px">
          <td colspan=2>官网性能数据  <a href="www.ag-777.com">点我点我</a>
          </td>
      </tr>

      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
          <td>
             <img src="cid:io">
          </td>
         <td>
             <img src="cid:key_hit">
          </td>
      </tr>

      <tr bgcolor="#EFEBDE" height="100" style="font-size:13px">
         <td>
            <img src="cid:men">
         </td>
         <td>
            <img src="cid:swap">
         </td>
      </tr>
    </table>""","html","utf-8")


msg = MIMEMultipart('related')
msg.attach(msgtext)
msg.attach(addimg("img/bytes_io.png","io"))
msg.attach(addimg("img/myisam_key_hit.png","key_hit"))
msg.attach(addimg("img/os_mem.png","men"))
msg.attach(addimg("img/os_swap.png","swap"))


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

