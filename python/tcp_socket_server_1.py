#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: tcp_socket_server_1.py
# Created Time: 2016年10月03日 星期一 14时10分13秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import socket, time, threading

## 创建基于IPV4的socket连接
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## 绑定IP and port
s.bind(('0.0.0.0', 9999))

## 监听端口,传入的参数指定等待连接的最大数量
s.listen(5)
print 'Waiting for connection...'

## 每个连接都必须创建新进程/线程来处理,否则,单线程在处理连接的过程中,
## 无法接受其它客户端的连接
## 建立连接后,服务器首先发一条欢迎消息,然后等待客户端数据,如果客户端数据
## 不为空,那么就加上Hello再发送给客户端;否则客户端发送数据为空或为exit字符串
## 就直接关闭连接
def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')

    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)

    sock.close()
    print 'Connection from %s:%s closed.' % addr

## 通过永久循环接受来自客户端的连接,accept()会等待并返回一个客户端的连接
while True:
    ## 接受一个新连接
    sock, addr = s.accept()

    ## 创建线程来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
