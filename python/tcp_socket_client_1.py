#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: tcp_socket_slient.py
# Created Time: 2016年09月30日 星期五 13时46分38秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import socket  ## 导入socket库

## 创建一个socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## 建立tcp连接
s.connect(('www.sina.com.cn', 80))

## 发送数据
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\n')

## 接收数据
buffer = []
while True:
    d = s.recv(1024)  ## 每次最多接收1K字节
    if d:
        buffer.append(d)
    else:
        print 'now recv data is null.'
        break

data = ''.join(buffer)
print data

## 关闭连接
s.close()

header, html = data.split('\r\n\r\n', 1)
print header

## 把接收的数据写入文件
with open('sina.html', 'wb') as f:
    f.write(html)
