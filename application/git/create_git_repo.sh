#!/bin/bash


[ $(id -u) != "1000" ] && { echo "Error: You must be use tomcat to run this script!" && exit 1; }


[ $# -ne 2 ] && { echo "Usage:$0 \$1=product \$2=role" && exit; }


## def var
CP=$1
ROLE=$2


## init repo
echo "==========init repo=========="
read -p "Please sure rm -rf /web/${CP}/${ROLE} (n/y)": DEL
[[ "$DEL" == "y" || -z "$DEL" ]] && {
rm -rf /web/${CP}/${ROLE}
mkdir -p /web/${CP}/${ROLE}/WebRoot
cd /web/${CP}/${ROLE} && git init
echo '.svn' > .gitignore
git add .
git commit -am "${CP} ${ROLE} repo $(date +%Y%m%d_%H%M%S_%w)"
echo
echo
}


## chou luo repo
echo "==========chou luo repo=========="
read -p "Please sure rm -rf /usr/share/nginx/html/repo/${CP}_${ROLE}.git (n/y)": DEL
[[ "$DEL" == "y" || -z "$DEL" ]] && {
cd /usr/share/nginx/html/repo/
rm -rf ${CP}_${ROLE}.git
git clone --bare /web/${CP}/${ROLE} ${CP}_${ROLE}.git
cd ${CP}_${ROLE}.git/hooks
\cp post-update.sample post-update
git update-server-info
echo
echo
}


## init repo and luo reop establish relations
echo "==========init repo and luo repo establish relations=========="
cd /web/${CP}/${ROLE}/
git remote add origin /usr/share/nginx/html/repo/${CP}_${ROLE}.git
git push --set-upstream origin master
git remote -v
echo
echo


## version numbers write to file
echo "==========version numbers write to file=========="
cd /usr/share/nginx/html/repo/${CP}_${ROLE}.git
V=$(git log | grep 'commit' | awk '{print $2}' | cut -c '1-7')
echo "$V" > /usr/share/nginx/html/release/${CP}_${ROLE}
echo "$V" > /usr/share/nginx/html/release/${CP}_${ROLE}_pre
echo "$V" > /usr/share/nginx/html/test/${CP}_${ROLE}
echo "$V" > /usr/share/nginx/html/test/${CP}_${ROLE}_pre
echo $V
echo
echo


## create update scripts and filter file
echo "==========create update scripts and filter file=========="
cd /bak/gitupdate/
\cp A01_webphp.sh ${CP}_${ROLE}.sh
sed -i "s@production=A01@production=${CP}@g" ${CP}_${ROLE}.sh
sed -i "s@type='webphp'@type=\'${ROLE}\'@g" ${CP}_${ROLE}.sh
chmod +x ${CP}_${ROLE}.sh

cat > /bak/gitupdate/exclude_files/excludefile_${CP}_${ROLE} << EOF
*.svn*
*.git*
init.properties
openIp.lib
openDomain.lib
_generate
_tmp
logs
sql
EOF

echo "/bak/gitupdate/${CP}_${ROLE}.sh"
echo "/bak/gitupdate/exclude_files/excludefile_${CP}_${ROLE}"
cat /bak/gitupdate/exclude_files/excludefile_${CP}_${ROLE}
echo
echo


## pull code
echo "==========pull code=========="
bash ${CP}_${ROLE}.sh
