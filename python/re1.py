#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: re1.py
# Created Time: 2016年06月15日 星期三 15时23分14秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import urllib2
import re
import os


URL = 'http://image.baidu.com/channel/wallpaper'
read = urllib2.urlopen(URL).read()
pat =  re.compile(r'src="http://.+?.js">')
urls = re.findall(pat,read)
print urls
print '\n'


for i in urls:
    print 'url替换前:'
    print i

    print 'url替换后:'
	## 方法1
    url= i.replace('src="','').replace('">','')
    print url


	## 方法2
    url2 = re.sub(r'src="', '', i)
    url = re.sub(r'">', '', url2)
    print url


    try:
        iread = urllib2.urlopen(url).read()
        print '读取每个处理过的URL内容存储到临时iread中'

        name = os.path.basename(url)
        print '去除url留下文件名称'
        print name
        print

        with open(name,'wb') as js_name:
            print '将上面读取的URL内容从临时iread写到文件%s中' % name
            js_name.write(iread)
    except:
        print url,"url error"
    print
