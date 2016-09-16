#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threading1.py
# Created Time: 2016年09月16日 星期五 16时52分53秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import time,threading


def loop():
    print 'thread %s is running...' % threading.current_thread().name
    n = 0
    while n < 5:
        n = n + 1
        print 'thread %s >>> %s' % (threading.current_thread().name,n)
        time.sleep(1)
    print 'thread %s is ended...' % threading.current_thread().name


print 'thread %s is running...' % threading.current_thread().name
t = threading.Thread(target=loop,name='LoopThread')
t.start()
t.join()
print 'thread %s is ended...' % threading.current_thread().name
