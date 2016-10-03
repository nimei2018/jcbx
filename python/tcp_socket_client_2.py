#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: tcp_socket_slient.py
# Created Time: 2016年09月30日 星期五 13时46分38秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


## 导入socket库
import socket

## 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## 建立tcp连接
s.connect(('www.google.com', 80))

## 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.google.com\r\nConnection: close\r\n\n')

## 接收数据
buffer = []

while True:
    ## 每次最多接收1K字节
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        print 'Now recv data is null'
        print
        break

## 将列表转成字符串
data = ''.join(buffer)
print type(data)
print 'google headder and html:'
print data
print

## 关闭连接
s.close()

## 对字符串做分离/分割操作
header, html = data.split('\r\n\r\n', 1)
print 'google header:'
print header
print
print 'google html:'
print html

## 把接收的数据写入文件
with open('google.html', 'wb') as f:
    f.write(html)
