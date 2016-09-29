#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: taskmanager.py
# Created Time: 2016年09月29日 星期四 14时22分30秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import random, time, Queue
from multiprocessing.managers import BaseManager

## 发送任务的队列
task_queue = Queue.Queue()

## 接收结果的队列
result_queue = Queue.Queue()

## 从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass

## 把两个Queue都注册到网络上,callabale参数关联了Queue对象
QueueManager.register("get_task_queue", callable=lambda: task_queue)
QueueManager.register("get_result_queue", callable=lambda: result_queue)

## 绑定端口5000,设置验证码为abc
manager = QueueManager(address=('', 5000), authkey='abc')

## start Queue
manager.start()

## 获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

## 放几个任务
for i in range(10):
    n = random.randint(0, 10000)
    print('Put task %d...' % n)
    task.put(n)

## 从result队列读取结果
print('Try get result...')
for i in range(10):
    r = result.get(timeout=10)
    print('Result: %s' % r)

## 关闭
manager.shutdown()
