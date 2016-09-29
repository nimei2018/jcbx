#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var2.py
# Created Time: 2016年09月27日 星期二 18时40分22秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


global_dict = {}

def std_thread(name):
    std = Student(name)
    ## 把std放在全局变量global_dict中
    global_dict[threading.current_thread()] = std
    do_task_1()
    do_task_2()

def do_task_1():
    ## 不传入std,而是根据当前线程查找
    std = global_dict[threading.current_thread()]

def do_task_2():
    ## 任何函数都可以查找出当前线程的std变量
    std = global_dict[threading.current_thread()]



