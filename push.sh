#!/bin/bash
export LANG=zh_CN.UTF8
# File Name: push.sh
# Created Time: 2016年06月16日 星期四 11时49分36秒
# Mail: Jason Bourne@nimei.com
# Author: Jason Bourne


git add .
git commit -am "update $(date +%Y%m%d_%H%M%S_%w)"
git push
