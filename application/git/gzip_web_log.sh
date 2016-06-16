#!/bin/bash


[ $# -ne 2 ] && {
    echo "Usage:$0 \$1=product_name \$2=role [A04 webphp]"
    exit
}


CP=$1
ROLE=$2
DATE1=$(date +%Y%m%d%H%M%S)
DATE2=$(date +%Y%m%d)
PHP_LOG1=/log/${CP}/${ROLE}/log
#[ ! -d ${PHP_LOG1} ] && mkdir -p ${PHP_LOG1}
DIR1=/log/record
[ ! -d ${DIR1} ] && mkdir $DIR1
LOG1=${DIR1}/gzip_web_log_${DATE2}.txt
USER=www


#nginx ${CP} ${ROLE} logs


NUM1=$(find ${PHP_LOG1} -maxdepth 1 -user ${USER} -group ${USER} -type f -mtime +2 -name "${CP}_${ROLE}_*.log" | sort | wc -l)
[ $NUM1 -ne 0 ] && {
echo "START ${DATE1} gzip ${CP} ${ROLE} logs......" >> ${LOG1}

find ${PHP_LOG1} -maxdepth 1 -user ${USER} -group ${USER} -type f -mtime +30 -name "${CP}_${ROLE}_*.log" | sort | xargs rm -f
sleep 2
find ${PHP_LOG1} -maxdepth 1 -user ${USER} -group ${USER} -type f -mtime +2 -name "${CP}_${ROLE}_*.log" | sort | xargs gzip

ls -lthr --time-style=long-iso ${PHP_LOG1} | grep '^-' | sort -rk 6 >> ${LOG1}
echo "END ${DATE1} gzip ${CP} ${ROLE} logs......" >> ${LOG1}
echo "" >> ${LOG1}
echo "" >> ${LOG1}
}
