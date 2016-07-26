#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: multiprocessing2.py
# Created Time: 2016年07月26日 星期二 11时01分56秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


from multiprocessing import Process
import os

# 子进程执行的代码
def child_proc(name):
    print "Run child process %s, it's process id is (%s)..." % (name, os.getpid())

if __name__ == '__main__':
    print 'Parent process id is %s.' % os.getpid()
    p = Process(target=child_proc, args=('AAA',))
    print 'Process will start.'
    p.start()
    p.join()
    print 'Process end.'
