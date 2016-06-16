#!/usr/bin/env python
# -*- coding:utf-8 -*-


import re


content = """
第4种:
178.32.5.178:3128
94.23.154.55:3128
178.32.5.190:3128
178.32.5.164:3128
178.32.5.161:3128
212.45.5.172:3128
81.200.26.217:3128
134.121.64.4:3127
222.52.99.131:8081
61.190.28.166:8080
94.232.65.104:3128
137.165.1.111:3127
82.199.113.2:3128
212.23.70.188:3128
92.50.152.62:3128
69.163.96.2:8080
95.31.2.114:3128
82.91.170.116:8080
218.204.240.26:8080
60.63.79.127:8909
114.241.36.11:8909
85.237.46.141:8080
209.97.203.64:8080

第3种:
<td class=ip>41.35.48.134</td><td class=port>8080</td><td class=isssl>Yes</td><td class=proxytype>Transparent</td><td class=cc><img width=20 height=20 src=img/flags/EG.png> EG Egypt</td><td class=registredto>All-01</td><td class=latency><div class=speedbar><div class=fast style="width:86%"></div><div class=value>86%</div></div></td><td class=reliability><div class=speedbar><div class=slow style="width:4%"></div><div class=value>4%</div></div></td><td class=uptime>0.17</td></tr><tr id=453><td class=ip>161.139.195.99</td><td class=port>80</td><td class=isssl>Yes</td><td class=proxytype>Anonymous</td><td class=cc><img width=20 height=20 src=img/flags/MY.png> MY Malaysia</td><td class=registredto></td><td class=latency><div class=speedbar><div class=fast style="width:79%"></div><div class=value>79%</div></div></td><td class=reliability><div class=speedbar><div class=slow style="width:1%"></div><div class=value>1%</div></div></td><td class=uptime>0.18</td></tr><tr id=3699><td class=ip>190.95.206.178</td><td class=port>8080</td>

第1种:
<br>190.74.185.65:8080<br>122.232.228.217:6675<br>201.208.228.243:8080<br>201.243.35.106:8080<br>193.116.157.195:80<br>2.49.91.33:8118<br>190.42.25.190:8080<br>190.207.228.95:8080<br>110.139.100.35:3128<br>200.54.92.187:80<br>180.183.147.93:3128<br>190.207.107.17:8080<br>61.18.76.127:9415<br>189.107.78.42:8080<br>190.42.129.112:8080<br>24.234.146.189:80<br>190.199.150.191:8080<br>190.202.230.192:8080<br>187.78.64.25:8080<br>66.39.5.184:80<br>177.36.242.93:8080<br>92.96.146.148:8118<br>82.99.254.146:8080<br>201.249.114.63:8080<br>209.190.7.250:80<br>190.78.25.207:8080<br>180.243.235.40:8080<br>201.249.20.161:8080<br>190.201.102.213:8080<br>190.198.112.37:8080<br>92.96.192.126:8118<br>92.97.95.150:8118<br>201.211.141.143:8080<br>122.113.39.40:80<br>91.121.115.66:3128<br>190.199.96.186:8080<br>201.210.8.152:8080<br>201.208.110.155:8080<br>217.119.81.106:3128<br>110.77.219.114:3128<br>92.99.136.27:8118<br>41.35.48.91:8080<br>123.100.5.57:8080<br>190.38.185.109:8080<br>186.94.21.83:8080<br>123.153.168.11:6675<br>190.202.124.18:3128<br>195.175.37.8:80<br>201.211.239.149:8080<br>187.78.147.66:8080<br>190.206.155.213:8080<br>190.198.156.244:8080<br>186.93.218.196:8080<br>222.214.130.89:8909<br>212.122.235.220:57<br>201.211.6.20:8080<br>92.99.162.242:8118<br>186.94.255.135:8080<br>190.199.33.200:8080<br>37.59.125.190:3128<br>176.31.99.49:80<br>110.77.213.27:3128<br>60.185.223.143:8909<br>188.255.147.65:6666<br>186.92.119.119:8080<br>186.95.65.79:8080<br>151.100.152.48:80<br>58.222.141.118:3128<br>186.93.105.14:8080<br>110.77.232.124:3128<br>61.138.6.89:8080<br>107.20.182.77:3128<br>125.209.94.12:8080<br>190.77.211.189:8080<br>186.88.67.109:8080<br>125.39.93.69:8888<br>27.8.126.96:6675<br>187.32.63.54:8080<br>203.223.47.246:3128<br>190.79.106.205:8080<br>202.232.97.11:8080<br>190.200.166.5:8080<br>92.99.248.84:8118<br>189.111.209.224:80<br>67.228.176.65:443<br>2.49.209.252:8118<br><br>
<tr class="list_sorted"></tr>

第2种:
<tr><td>201.219.17.45:3128</td><td>transparent </td><td>832 minutes ago</td><td>Ecuador</td></tr><tr><td>79.173.37.19:8080</td><td>transparent </td><td>1431 minutes ago</td><td>Poland</td></tr><tr><td>189.13.207.196:8080</td><td>transparent </td><td>1202 minutes ago</td><td>Brazil</td></tr><tr><td>85.185.95.194:8080</td><td>transparent </td><td>585 minutes ago</td><td>Iran, Islamic Republic of</td></tr><tr><td style="padding-top:10px; padding-bottom:10px" align="center" colspan="4">
<div style="margin: 0 auto; padding: 10px; font-size:15px; background-color:#FFF; color: #483651; text-align:center"><a style="color:#00F" href="http://proxy.lc/"><strong>Personal Premium Proxy</strong></a><!--<br />Think. Feel. Enjoy--></div></td></tr><tr><td>118.97.44.154:8080</td><td>transparent </td><td>873 minutes ago</td><td>Indonesia</td></tr><tr><td>92.99.128.80:8118</td><td>transparent </td><td>842 minutes ago</td><td>United Arab Emirates</td></tr><tr><td>201.251.62.137:8080</td><td>transparent </td><td>607 minutes ago</td><td>Argentina</td></tr><tr><td>202.165.88.109:80</td><td>transparent </td><td>564 minutes ago</td><td>Australia</td></tr><tr><td>177.36.242.97:8080</td><td>transparent </td><td>1052 minutes ago</td><td>Brazil</td></tr><tr><td>89.218.94.166:3128</td><td>transparent </td><td>645 minutes ago</td><td>Kazakstan</td></tr><tr><td>177.36.242.61:8080</td><td>transparent </td><td>992 minutes ago</td><td>Brazil</td></tr><tr><td>92.99.207.231:8118</td><td>transparent </td><td>1040 minutes ago</td><td>United Arab Emirates</td></tr></table>
<div style="width: 780px; text-align:center; margin: 15px 0 15px 0">
"""


def re_findall(content):


    ## 定义多个正则表达式使用列表存储
    patterns = [
        r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}):(\d+)',
        r'ip>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}).*?port>(\d+)',
    ]


    for pattern in patterns:
        print "打印定义的2种获取IP:PORT的正则表达方式 %s" % pattern
        print

        ## re.findall()方法是一个循环,返回的是一个列表;每一次匹配的条件是2个元素,然后组成元组,再由元组组成列表
        matches = re.findall(pattern, content, re.I)
        print matches
        print


        ## 如果matches列表为真,则继续下面操作;列表为真表示列表存在并且非空
        if matches:
            ## 根据上面的正则条件,列表中的元素是元组,每次循环出来的元素是元组;然后再对元组进行取值
            for match in matches:
                print match[0],match[1]
        print


def re_compile(content):


    ## 定义多个正则表达式使用列表存储
    patterns = [
        '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)$',
        '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$',
    ]


    for pattern in patterns:
        print "打印定义的2种获取IP:PORT的正则表达方式 %s" % pattern
        print


        ## re.findall()方法是一个循环,返回的是一个列表;每一次匹配的条件是2个元素,然后组成元组,再由元组组成列表
        matches = re.compile(pattern)
        print matches
        print

        matches.match
        print


if __name__ == "__main__":
    re_findall(content)
if __name__ == "__main__":
    re_findall(content)
