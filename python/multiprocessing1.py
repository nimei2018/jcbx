#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: multiprocessing1.py
# Created Time: 2016年07月25日 星期一 17时17分42秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import os

print "Return the current process id (%s)" % os.getpid()

# Fork a child process.
# Return 0 to child process and PID of child to parent process.
pid = os.fork()

if pid == 0:
    print 'Child process id is (%s) and my parent process id is (%s).' % (os.getpid(), os.getppid())
else:
    print 'Parent process id is (%s) and me created a child process id is (%s).' % (os.getpid(), pid)
