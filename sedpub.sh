#! /bin/bash
#this is for pubfunction of sed command
#Author:xccai
#������ģ��

ask_mode()
{
    echo "��ѡ��sed�Ĳ���ģʽ��0-�ַ���ȫƪ�滻;1-�ض���ɾ��;2-�ض�����β׷��;3-�ض���ǰ׷��;4-�ض��к�׷��;5-ֻƥ���ض��еĵ�һ�κ�׷��
         6-ֻƥ���ض��е����һ�κ�׷��)"
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
    elif [ $mode_sel -eq 5 ];then
        linenum=`grep -n kil testsedpub.txt.base|awk -F ":" '{if(NR==1)print $1}'`
        sed "${linenum}a\\
        xyz
        " testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    elif [ $mode_sel -eq 6 ];then
        linenum=`grep -n kil testsedpub.txt.base|sed -n '$p'|awk -F ":" '{print $1}'`
        sed "${linenum}a\\
        xyz
        " testsedpub.txt >> testtemp
        mv testtemp testsedpub.txt
    else
    	echo "�ݲ�֧����������ģʽ"
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
