#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: process-to-process.py
# Created Time: 2016年07月27日 星期三 16时52分30秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码
def write(q):
    for value in ['A', 'B', 'C', 'D']:
        print 'write %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码
def read(q):
    while True:
        value = q.get(True)
        print 'read %s from queue.' % value

if __name__ == '__main__':
    # 父进程创建Queue,并传给各个子进程
    #Queue(maxsize=0)
    #    Returns a queue object
    q = Queue()

    #__init__(self, group=None, target=None, name=None, args=(), kwargs={})
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))

    # 启动子进程pw,写入
    # Start child process
    pw.start()

    # 启动子进程pr,读取
    pr.start()

    # 等待pw结束
    # Wait until child process terminates
    pw.join()

    # pr进程里面是死循环,无法等待其结果,只能强行终止
    # Terminate process; sends SIGTERM signal or uses TerminateProcess()
    pr.terminate()
