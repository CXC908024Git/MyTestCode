#! /bin/bash
#this is for pubfunction of sed command

#函数子模块

ask_mode()
{
    echo "请选择sed的操作模式（0-字符串全篇替换;1-特定行删除;2-特定行行尾追加;3-特定行前追加;4-特定行后追加)"
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
        sed "/kil/i\\
        abc
        " testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 4 ];then
        sed "/kil/a\\
        xyz
        " testsedpub.txt >> testtemp
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
