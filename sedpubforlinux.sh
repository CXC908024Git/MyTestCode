#! /bin/bash
#this is for pubfunction of sed command
#Author:xccai
#函数子模块

ask_mode()
{
echo "
请选择sed的操作模式:
0-字符串全篇替换
1-特定行删除
2-特定行行尾追加
3-特定行前追加
4-特定行后追加
5-只匹配特定行的第一次后追加
6-只匹配特定行的最后一次后追加
7-读取文件并插入到匹配的行中
8-将匹配到的行的内容写入文件
9-打印匹配的行"
	while [ 1 ]
	do
	read mode_sel
	if [ ! $mode_sel ];then
		echo "请重新选择操作模式!"
		continue
	fi
	case $mode_sel in
	0)
		sed  "s|cxc|xccai|g" testsedpub.txt >> testtemp 
		mv testtemp testsedpub.txt
		break
		;;
	1)
		sed "2d" testsedpub.txt >> testtemp
		mv testtemp testsedpub.txt
		break    
		;;
	2)
		sed "/kil/s|$|& TAIL|g" testsedpub.txt >> testtemp 
		mv testtemp testsedpub.txt
		break
		;;
	3)
		sed "/kil/i abc\nmnk" testsedpub.txt >> testtemp   
		mv testtemp testsedpub.txt   
		break  
		;;
	4)
		sed "/kil/a xyz\nstu" testsedpub.txt >> testtemp 
		mv testtemp testsedpub.txt
		break
		;;
	5)
		linenum=`grep -n kil testsedpub.txt.base|awk -F ":" '{if(NR==1)print $1}'`
		sed "${linenum}i abconce" testsedpub.txt >> testtemp     
		mv testtemp testsedpub.txt  
		break
		;;
	6)
		linenum=`grep -n kil testsedpub.txt.base|sed -n '$p'|awk -F ":" '{print $1}'`   
		sed "${linenum}a xyzonce" testsedpub.txt >> testtemp  
		mv testtemp testsedpub.txt   
		break
		;;
	7)
		sed "/cxc/r read.md" testsedpub.txt >> testtemp 
		mv testtemp testsedpub.txt
		break
		;;
	8)
		sed -n  "/cxc/w write.md" testsedpub.txt
		break
		;;
	9)
		sed -n "/cxc/p" testsedpub.txt  
		break
		;;
	*)
		echo "暂不支持其它其它模式"
		return 1
		;;
	esac
	done
}

cat /dev/null > testsedpub.txt
cat testsedpub.txt.base > testsedpub.txt
ask_mode
if [ $? -ne 0 ];then
	exit 1
else
	echo "change finshed"
fi
