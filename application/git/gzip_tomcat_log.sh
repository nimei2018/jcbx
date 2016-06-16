#!/bin/bash


DATE1=$(date +%Y%m%d%H%M%S)
DATE2=$(date +%Y%m%d)
TOMCAT_LOG1=/opt/tomcat7/logs
TOMCAT_LOG2=/opt/tomcat7/logs/access
LOG=/tmp/gzip_tomcat_logs_${DATE2}.txt


#tomcat catalina logs

NUM1=$(find ${TOMCAT_LOG1} -maxdepth 1 -user tomcat -group tomcat -type f -mtime +2 -name 'catalina.*.out' | sort | wc -l)
[ $NUM1 -ne 0 ] && {
echo "START ${DATE1} gzip tomcat catalina logs...." >> ${LOG}

find ${TOMCAT_LOG1} -maxdepth 1 -user tomcat -group tomcat -type f -mtime +30 -name 'catalina.*.out' | sort | xargs rm -f
sleep 2
find ${TOMCAT_LOG1} -maxdepth 1 -user tomcat -group tomcat -type f -mtime +2 -name 'catalina.*.out' | sort | xargs gzip

ls -lthr ${TOMCAT_LOG1} | grep '^-' >> ${LOG}
echo "END ${DATE1} gzip tomcat catalina logs...." >> ${LOG}
echo "" >> ${LOG} 
echo "" >> ${LOG}
}


#tomcat access logs

NUM2=$(find ${TOMCAT_LOG2} -maxdepth 2 -user tomcat -group tomcat -type f -mtime +2 -name '*.txt' | sort | wc -l)
[ $NUM2 -ne 0 ] && {
echo "START time ${DATE1} gzip tomcat access logs...." >> ${LOG}

find ${TOMCAT_LOG2} -maxdepth 2 -user tomcat -group tomcat -type f -mtime +30 -name '*.txt' | sort | xargs rm -f
sleep 2
find ${TOMCAT_LOG2} -maxdepth 2 -user tomcat -group tomcat -type f -mtime +2 -name '*.txt' | sort | xargs gzip

ls -lthr ${TOMCAT_LOG2}/*/ >> ${LOG}
echo "END time ${DATE1} gzip tomcat access logs...." >> ${LOG}
echo "" >> ${LOG}
echo "" >> ${LOG}
}
