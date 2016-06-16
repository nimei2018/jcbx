#!/bin/bash

# common
/sbin/iptables -F
/sbin/iptables -F -t nat
/sbin/depmod -a
/sbin/modprobe ip_tables
/sbin/modprobe ip_conntrack
/sbin/modprobe ip_nat_ftp
/sbin/modprobe ip_conntrack_ftp
/sbin/iptables -A INPUT -i  lo -j ACCEPT
/sbin/iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT

# sshd
#/sbin/iptables -A INPUT -p tcp -m tcp --dport 22 -j ACCEPT

# port
/sbin/iptables -A INPUT -p tcp -m tcp --dport 53 -j ACCEPT
/sbin/iptables -A INPUT -p udp -m udp --dport 53 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 80 -j ACCEPT
/sbin/iptables -A INPUT -p udp -m udp --dport 161 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 443 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 873 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 1111 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 1935 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 5659 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 1243 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 8888 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 9999 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 8080 -j ACCEPT
/sbin/iptables -A INPUT -p tcp -m tcp --dport 11211 -j ACCEPT

#### IDC
/sbin/iptables -A INPUT -s 192.168.0.0/16 -j ACCEPT
/sbin/iptables -A INPUT -s 10.5.0.0/16 -j ACCEPT
/sbin/iptables -A INPUT -s 10.0.0.0/8 -j ACCEPT

#ping
/sbin/iptables -A INPUT -p icmp -j ACCEPT
/sbin/iptables -A INPUT -m state --state INVALID,NEW -j DROP
/sbin/iptables -P INPUT DROP

# save restart
/etc/rc.d/init.d/iptables save
/etc/rc.d/init.d/iptables restart
