#! /bin/bash
#进度条打印函数
#locale init
DATENOW=`date +'%Y%m%d'`
#为tar命令创建管道符和core_advance交互
mkfifo /tmp/tarfifo
TARFIFO=/tmp/tarfifo

lsitcnt=`ls -rlt|awk '{if(NR>1) print $9}'|egrep -v "*"`
total_size_list=`ls -rlt|awk '{if(NR>1) print $9}'|egrep -v "*"|xargs du -sH|awk '{print $1}'`
total_size=`echo $total_size_list|awk 'BEGIN{sum_size=0} {for(i=1;i<=NF;i++) sum_size=sum_size+$i} END{print sum_size}'`
let per_size=${total_size}/100

echo "本次需要打包${total_size}B字节文件"

if [ $total_size -eq 0 ]; then
    print_advance 100
    exit $?
fi

print_advance ()
{
	complete=$1
	let percent=$1*100/100
	printf "\r%0${complete}d" | tr '0' '#'   
	echo -n "$percent%已完成"
}

core_advance()
{
    sum_size=0
    while read line
    do
        line_size=`echo $line|xargs du -sH|awk '{print $1}'`
        sum_size=`expr $sum_size + $line_size`
        finsh_cnt=`expr $sum_size \/ $per_size`
        print_advance $finsh_cnt
        #sleep 1 2 > /dev/null
        if [ $finsh_cnt -ge 100 ];then
            print_advance 100
            rm -f $TARFIFO
            break
        fi
    done < $TARFIFO
    echo ""
    return 0
}

core_advance &
sonpid=$!
ls -rlt|awk '{if(NR>1) print $9}'|egrep -v "*"|xargs tar -cvf cxc.$DATENOW.tar >$TARFIFO 2> /dev/null
ret=$?

wait ${sonpid}
exit ${ret}
