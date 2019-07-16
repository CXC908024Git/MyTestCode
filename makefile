# Makefile

#CC   = cc -brtl
#扫描工具编译
CC   = /app/amesb/parasoft/cpptest/9.2/cpptestscan.sh cc -brtl

#保留使用
CFLAGS  = -g -c
INCLUDE = -I$(TPBUS_HOME)/include $(MQINCL) -I$(TPBUS_HOME)/include/libxml2 -I$(HOME)/test/AEC/testcode/cxc/include
LIBS = -L$(TPBUS_HOME)/lib -ltpbus -ltpCustom -lsqlite3 $(MQLIBS) $(SYSLIBS) 

#-e指定入口,函数中必须要由exit(0)

.SUFFIXES:	.c .o

all:testwc add test0910 test1017 test0114 test0219 test111 test112 testbank test0307 test0418 test0429 test0506 test0610 test0619 test0716 test00

.c.o:
	$(CC) -o $*.o $(CFLAGS) $*.c $(INCLUDE)

testwc: testwc.o
	$(CC)  -o $@ testwc.o

add:add.o
	$(CC)  -o $@ add.o

test0910:test0910.o
	$(CC)  -o $@ test0910.o

test1017:test1017.o
	$(CC) -o $@ test1017.o

test0114:test0114.o
	$(CC) -o $@ test0114.o

clean:
	rm -f *.o


test0219:test0219.o
	$(CC) -o $@ test0219.o


test111:test111.o
	$(CC) -o $@ test111.o


test112:test112.o
	$(CC) -o $@ test112.o


testbank:testbank.o
	$(CC) -o $@ testbank.o


test0307:test0307.o
	$(CC) -o $@ test0307.o


test0418:test0418.o
	$(CC) -o $@ test0418.o


test0429:test0429.o
	$(CC) -o $@ test0429.o


test0506:test0506.o
	$(CC) -o $@ test0506.o


test0610:test0610.o
	$(CC) -o $@ test0610.o


test0619:test0619.o
	$(CC) -o $@ test0619.o


test0716:test0716.o
	$(CC) -o $@ test0716.o


test00:test00.o
	$(CC) -o $@ test00.o
