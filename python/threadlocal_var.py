#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: threadlocal_var.py
# Created Time: 2016年09月22日 星期四 14时58分27秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_3(std)
    do_subtask_4(std)

def do_task_3(std):
    do_subtask_5(std)
    do_subtask_6(std)

def process_studeng(name):
    ## Studeng是一个对象
    ## std是局部变量，但每个函数都要用它，因此必须传递
    std = Student(name)
    do_task_1(std)
    do_task_2(std)
    do_task_3(std)


