#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: dict1.py
# Created Time: 2016年06月14日 星期二 14时10分14秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


print '这个类用来演示如何对自定义对象进行排序:'
print '\n'


class Sortobj:
    a = 0
    b = ''
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def printab(self):
        print self.a, self.b


print '演示对字符串列表进行排序'
samplelist_str = ['blue','allen','sophia','keen']
print samplelist_str
samplelist_str.sort()
print samplelist_str
print '\n'


print '演示对整型数进行排序'
samplelist_int = [34,23,2,2333,45]
print samplelist_int
samplelist_int.sort()
print samplelist_int
print '\n'


print '演示对字典数据进行排序:'
sampledict_str = {'blue':'5555@sina.com',
                  'allen':'222@163.com',
                  'sophia':'4444@gmail.com',
                  'ceen':'blue@263.net'}
print sampledict_str

print '按照dict key进行排序'
print sorted(sampledict_str.items(), key=lambda d: d[0])

print '按照dict value进行排序'
print sorted(sampledict_str.items(), key=lambda d: d[1])
print '\n'


print '构建用于排序的类实例:'
obja = Sortobj(343, 'keen')
objb = Sortobj(56, 'blue')
objc = Sortobj(2, 'aba')
objd = Sortobj(89, 'iiii')


print '实例对象排序前'
samplelist_obj = [obja, objb, objc, objd]
for obj in samplelist_obj:
    obj.printab()
print '\n'


print '按照对象的a属性进行排序'
samplelist_obj.sort(lambda x,y: cmp(x.a, y.a))
for obj in samplelist_obj:
    obj.printab()
print '\n'


print '按照对象的b属性进行排序'
samplelist_obj.sort(lambda x,y: cmp(x.b, y.b))
for obj in samplelist_obj:
    obj.printab()
