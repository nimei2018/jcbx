#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: dict2.py
# Created Time: 2016年06月14日 星期二 14时38分30秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


print '原始数据字典'
dict = {'name': 'Zara', 'age': 7, 'class': 'First'}
print dict
print '\n'


print "字典转为字符串，返回：<type 'str'> {'age': 7, 'name': 'Zara', 'class': 'First'}"
print type(str(dict)), str(dict)
print '\n'


print "字典可以转为元组，返回：('age', 'name', 'class')"
print tuple(dict)
print

print "字典可以转为元组，返回：(7, 'Zara', 'First')"
print tuple(dict.values())
print '\n'


print "字典转为列表，返回：['age', 'name', 'class']"
print list(dict)
print

print '字典转为列表'
print dict.values
print '\n'


print '2.原始数据元组'
tup=(1, 2, 3, 4, 5)
print tup
print '\n'


print '元组转为字符串，返回：(1, 2, 3, 4, 5)'
print tup.__str__()
print


print '元组转为列表，返回：[1, 2, 3, 4, 5]'
print list(tup)
print '\n'


print '元组不可以转为字典?'
print '\n'


print '3.原始数据列表'
nums=[1, 3, 5, 7, 8, 13, 20]
print nums
print '\n'


print '列表转为字符串，返回：[1, 3, 5, 7, 8, 13, 20]'
print str(nums)
print '\n'


print '列表转为元组，返回：(1, 3, 5, 7, 8, 13, 20)'
print tuple(nums)
print '\n'


print '列表不可以转为字典?'
print '\n'


print '4.原始数据字符串'
print '\n'


print '字符串转为元组，返回：(1, 2, 3)'
print tuple(eval("(1,2,3)"))
print '\n'


print '字符串转为列表，返回：[1, 2, 3]'
print list(eval("(1,2,3)"))
print '\n'


print "字符串转为字典，返回：<type 'dict'>"
print type(eval("{'name':'ljq', 'age':24}"))
print '\n'
