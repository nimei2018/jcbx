#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var3.py
# Created Time: 2016年09月28日 星期三 10时46分13秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading

## 创建全局ThreadLocal对象
local_school = threading.local()

def process_student():
    print 'Hello, %s (in %s)' % (local_school.student, threading.current_thread().name)

def process_thread(name):
    ## 绑定ThreadLocal的student
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t1.start()
t1.join()

t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t2.start()
t2.join()

t3 = threading.Thread(target=process_thread, args=('nimei',), name='Thread-C')
t3.start()
t3.join()
