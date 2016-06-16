#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: dict_xun.py
# Created Time: 2016年06月13日 星期一 17时08分04秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import re

ip_info = { '1.1.1.1' : 10, '2.2.2.2:80' : 20, 'aaa' : 000, '3.3.3.3:9999' : 30}

if '-' in ip_info.keys():
    del ip_info['-']


print ip_info


for k in ip_info.keys():
    print k

    patterns = [
        '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',
        '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)$',
    ]


    for pattern in patterns:
        ips = re.compile(pattern)

        #print ips.match(k).group()
        if ip_info[k] == ips.match(k).group():
            del(ip_info[k])
            #del ip_info[k]

print ip_info
