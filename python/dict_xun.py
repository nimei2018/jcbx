#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: dict_xun.py
# Created Time: 2016年06月13日 星期一 17时08分04秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import re

ip_info = { '1.1.1.1' : 10, '2.2.2.2:80' : 20, 'aaa' : 000, '3.3.3.3:9999' : 30, '-' : 100, 'xxxx' : 10}
new_ip_info = {}


print '原始数据:'
print ip_info
print


if '-' in ip_info.keys():
    del ip_info['-']


print '删除字典中key is -的元素'
print ip_info
print


for k,v in ip_info.items():


     if re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', k) != None:
        print k
        continue
     elif re.match('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)$', k) != None:
        print k
        continue

     new_ip_info[k] = v


print
print '最终result:'
for k,v in new_ip_info.items():
    print k,v
