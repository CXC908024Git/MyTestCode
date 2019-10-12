#! /bin/ksh

ps -ef -ostat,uname,pid,command|grep $1
