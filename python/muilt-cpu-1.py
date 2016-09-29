#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: muilt-cpu-1.py
# Created Time: 2016年09月16日 星期五 18时52分47秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import threading,multiprocessing

def loop2():
    x = 0
    while True:
        x = x ^ 1
        print x

for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop2)
    t.start()
