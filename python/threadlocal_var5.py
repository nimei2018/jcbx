#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var5.py
# Created Time: 2016年09月28日 星期三 13时05分44秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading,time

def doWaiting():
    print 'start waiting:', time.strftime('%H:%M:%S')
    time.sleep(3)
    print 'stop waiting', time.strftime('%H:%M:%S')

thread1 = threading.Thread(target = doWaiting)
thread1.start()
time.sleep(5)      ## 确保线程thread1已经启动

print 'start join'
thread1.join()     ## 将一直堵塞,直到thread1运行结束
print 'end join'
