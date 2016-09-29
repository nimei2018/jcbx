#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: multiprocessing3.py
# Created Time: 2016年07月26日 星期二 11时39分06秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print "Current run task is %s, It's process id is (%s)..." % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print "Task %s runs %0.2f seconds." % (name, (end - start))

if __name__ == '__main__':
    print 'Parent process id is %s.' % os.getpid()
    #Pool(processes=None, initializer=None, initargs=(), maxtasksperchild=None)
    #    Returns a process pool object
    # Pool的默认个数是CPU的核数,我本机是8核,因此若想看到等待结果需要大于8,即,Pool(8),表示同时跑8个进程
    p = Pool(8)
    for i in range(10):
        #apply_async(self, func, args=(), kwds={}, callback=None) method of multiprocessing.pool.Pool instance
        #    Asynchronous equivalent of `apply()` builtin
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
