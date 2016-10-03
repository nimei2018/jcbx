#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: udp_socket_client_1.py
# Created Time: 2016年10月03日 星期一 16时31分26秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip, port = ('127.0.0.1', 9999)
print (ip, port)

for data in ['mysql', 'nosql', 'oracle', 'mongo']:
    ## 发送数据
    s.sendto(data, (ip, port))
    #s.sendto(data, ('127.0.0.1', 9999))
    ## 接收数据
    print s.recv(1024)

s.close()
