#!/bin/bash


PATH=/usr/kerberos/bin:/usr/local/bin:/bin:/usr/bin:/home/tomcat/bin
export PATH


url="http://1.1.1.1:87"
product="E04"
type="webphp"
workdir="/web"
localdir=$workdir/$product
gitlog="/tmp/gitmail.txt"
MAIL_LIST=test1@126.com
MAIL_FORM=test2@126.com
DATE=$(date "+_%Y-%m-%d_%H:%M:%S")
NOIP="127.0.0.1|192.168.0."
IP=$(/sbin/ifconfig | grep 'inet addr:' | egrep -v "$NOIP" | cut -d : -f2 | awk '{print $1}' | head -1)

VERSION1=${workdir}/${product}/${type}/WebRoot/version.txt


if [ -n "$type" ];then
      vfile=$product"_"$type
      workdir=$workdir/$product
      localdir=$workdir/$type

      [ ! -d $workdir ] && mkdir $workdir
else
      vfile=$product
fi


if [ $# -gt 0 ];then
      if [ $* = "test" ];then
           version=$(curl $url/test/$vfile 2> /dev/null | cut -c '1-7')
      else
           version=$(curl $url/release/$vfile 2> /dev/null | cut -c '1-7')
      fi
else
      version=$(curl $url/release/$vfile 2> /dev/null | cut -c '1-7')
fi


git_mail()
{
echo -e "Subject: $IP git status updated for $type $product on $DATE\n`cat $gitlog`" | /usr/sbin/sendmail -f $MAIL_FORM $MAIL_LIST
}


init_repo()
{
if [ -d "$localdir/.git" ];then
	cd $localdir
	git fetch &> /dev/null
else
	[ -d "$localdir" ] && mv $localdir{,"_"$DATE}
	
	cd $workdir 
	if [ -n "$type" ];then
	     git clone --depth 1 $url/repo/$vfile.git $type &> /dev/null

             cd $workdir/$type
             git pull --depth 5 &> /dev/null
	else
	     git clone --depth 1 $url/repo/$product.git &> /dev/null

             cd $workdir/$type
             git pull --depth 5 &> /dev/null
	fi
fi
}


sync_code()
{
cd $localdir
git fetch &> /dev/null

localver=$(git log -1 | head -n 1 | awk '{print $2}' | cut -c '1-7')
if [ $version != $localver ];then
      echo > $gitlog
      git clean -df
      git reset --hard $version

      echo "============the version is: $version\t===============" >> $gitlog
      echo "$product $type changed version from $localver to $version, please check whether tomcat needs restart" >> $gitlog

      echo "modified file list:\n" >> $gitlog
      echo "cd $localdir && git diff --name-only $localver $version"
      git diff --name-only $localver $version >> $gitlog
      git_mail
fi
}


init_repo
sync_code


echo
cat $VERSION1
