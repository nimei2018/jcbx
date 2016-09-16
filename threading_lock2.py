#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threading_lock1.py
# Created Time: 2016年09月16日 星期五 17时18分21秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import time,threading

# 假定这是我的银行存款
balance = 0

# lock file
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 修改前，先获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 修改后，一定释放锁
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print balance
