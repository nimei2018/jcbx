#!/usr/bin/env python
# *-* coding:utf-8 *-*


import sys
import re
from time import clock as now


time1 = now()


## 判断参数个数,需要用户输入一个文件名称;$0是第一个参数,表示py脚本文件本身
if len(sys.argv) != 2:
    print "Please enter a filename:"
    sys.exit(1)


## 定义一个空字典用于存储split的值
ip_info = {}


## 存储对dict ip_info again modify的result
new_ip_info = {}


def nginxlog(log_path = sys.argv[1]):
    with open(log_path,'r') as f:

        ## readlines一次读取整个文件,返回一个列表,供我们便利,文件大小必须小于内存
        for line in f.readlines():

            ## 去掉每行首尾空白
            line = line.strip()

            ## 判断是否为空行,如果为空行,跳过当前空行,继续处理下一行
            if not len(line):
                continue


            ## 获取client ip
            #ip = line.split('の')[2]
            #print ip


            ## 获取client access domain
            try:
                domain = line.split('の')[4]
            except IndexError,e:
                #print "error: domain %s" % e
                continue


            ## 获取client acces url
            #url = line.split('の')[5]
            #print url


            #if ip not in ip_info:
            #    ip_info[ip] = {url:1}
            #else:
            #    if url not in ip_info[ip]:
            #        ip_info[ip][url] = 1
            #    else:
            #        ip_info[ip][url] += 1


            ## 判断域名是否在字典中,如果不在字典中,就把域名作为key,对应的value为1
            ## 如果域名在字典中,就把域名对应的value加1
            if domain not in ip_info:
                ip_info[domain] = 1
            else:
                ip_info[domain] += 1


    ## 删除字典中key值是-的元素
    if '-' in ip_info.keys():
        del ip_info['-']


    ## 把字典转变成可迭代的对象,由元组组成的列表
	## 通过lambda函数进行比较,使用sorted进行排序同时取22行,这样下面再次处理就无需耗费太多资源
    old_result = sorted(ip_info.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)[0:23]


    ## 这里使用了re.match()方法匹配IP和IP:PORT,使用re.search(),re.findall(),re.compile()都可以,具体差别请自行了解
	## 这里的原数据是经过处理的,key是域名或IP或IP:PORT,value是key访问次数,所以re的方法可以使用,用re.search会更好
	## 这里使用了严格匹配方法,即,只匹配IP,只匹配IP:PORT,也可以使用模糊匹配
    ## python中字符串前面加上 r 表示原生字符串,有了原生字符串,再也不用担心是不是漏写了反斜杠,写出来的表达式也更直观
    ## 这里为了简单没有使用异常处理,直接用continue;如果想记录日志,使用异常处理同时记录日志
    ## re.search or re.match,如果加group就会出现None错误


    ## re.search()
    for k,v in old_result:
        if re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', k) != None:
            continue
        elif re.search(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)$', k) != None:
            continue

        new_ip_info[k] = v


    ## re.match()
    #for k,v in old_result:
    #    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', k) != None:
    #        continue
    #    elif re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)$', k) != None:
    #        continue

    #    new_ip_info[k] = v


    ## 模糊匹配,同时匹配IP和IP:PORT
    #for k,v in old_result:
    #    if re.match(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', k) != None:
    #        continue

    #    new_ip_info[k] = v


    new_result = sorted(new_ip_info.items(), lambda x, y: cmp(x[1], y[1]), reverse=True)


    for k,v in new_result:
        print '{:10s} {:<10s}'.format(str(v),k)


    f.close()


if __name__ == "__main__":
    nginxlog()
    time2 = now()
    print
    print 'run time is ' + str(time2 - time1) + 's'
