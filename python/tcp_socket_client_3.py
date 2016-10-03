#!/usr/bin/env python
# -*- coding=utf-8 -*-
# File Name: tcp_socket_client_3.py
# Created Time: 2016年10月03日 星期一 14时36分20秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('10.140.50.119', 9999))

print s.recv(1024)

for data in ['mysql', 'nosql', 'oracle', 'mongo']:
    s.send(data)
    print s.recv(1024)

s.send('exit')
s.close()
