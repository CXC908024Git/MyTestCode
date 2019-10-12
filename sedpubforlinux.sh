#! /bin/bash
#this is for pubfunction of sed command
#Author:xccai
#函数子模块

ask_mode()
{
    echo "请选择sed的操作模式:
0-字符串全篇替换
1-特定行删除
2-特定行行尾追加
3-特定行前追加
4-特定行后追加
5-只匹配特定行的第一次后追加
6-只匹配特定行的最后一次后追加)"
    read mode_sel
    if [ $mode_sel -eq 0 ];then
        sed  "s|cxc|xccai|g" testsedpub.txt >> testtemp
	mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 1 ];then
		sed "2d" testsedpub.txt >> testtemp
		mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 2 ];then
        sed "/kil/s|$|& TAIL|g" testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 3 ];then
        sed "/kil/i abc\nmnk" testsedpub.txt >> testtemp 
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 4 ];then
        sed "/kil/a xyz\nstu" testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 5 ];then
        linenum=`grep -n kil testsedpub.txt.base|awk -F ":" '{if(NR==1)print $1}'`
        sed "${linenum}i abconce" testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 6 ];then
        linenum=`grep -n kil testsedpub.txt.base|sed -n '$p'|awk -F ":" '{print $1}'`
        sed "${linenum}a xyzonce" testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    else
    	echo "暂不支持其它其它模式"
    	return 1
    fi
}

cat /dev/null > testsedpub.txt
cat testsedpub.txt.base > testsedpub.txt
ask_mode
if [ $? -ne 0 ];then
	exit 1
else
	echo "change finshed"
fi
