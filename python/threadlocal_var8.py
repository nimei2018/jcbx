#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var8.py
# Created Time: 2016年09月28日 星期三 14时51分32秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading

def hello():
    print "hello,world"

t = threading.Timer(3, hello)
t.start()  ## 3秒后开始执行hello()函数
