#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var6.py
# Created Time: 2016年09月28日 星期三 14时14分08秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading

lock = threading.Lock()  ## Lock对象
lock.acquire()
lock.acquire()  ## 多个acquire会产生死锁
lock.release()
lock.release()
