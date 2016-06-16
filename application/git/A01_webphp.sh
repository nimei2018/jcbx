#!/bin/bash


[ $(id -u) != "1000" ] && { echo "Error: You must be use tomcat to run this script!" && exit 1; }


## common var
production=A01
type='webphp'
ltype=`tr '[A-Z]' '[a-z]'<<< $type`
remote="$production"_"$type"
local="/web/$production/$type/WebRoot"

workdir=/web

## rsync argv
exfile=/bak/gitupdate/exclude_files/excludefile_${production}"_"${type}
passfile=/bak/gitupdate/rsync.password

. /bak/gitupdate/public_functions
