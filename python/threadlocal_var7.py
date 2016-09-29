#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var7.py
# Created Time: 2016年09月28日 星期三 14时20分36秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading

rlock = threading.RLock()  ## RLock对象
rlock.acquire()
rlock.acquire()  ## 同一个线程内,程序不会堵塞
rlock.release()
rlock.release()
