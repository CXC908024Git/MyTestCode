#! /bin/bash
if [ $# -ne 2 ];then
echo "������������ȷ��The Usage:redthead.sh filesrc filedest"
exit 1
fi

cat $1 > temp1
cat $2 >> temp1
mv temp $2

echo "redirect successfully"
