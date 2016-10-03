#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: udp_socket_server_1.py
# Created Time: 2016年10月03日 星期一 16时28分24秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('0.0.0.0', 9999))
print 'Bind udp port on 9999...'

while True:
    ## 接收数据
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)
