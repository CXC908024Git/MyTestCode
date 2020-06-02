/*
 * AddMain.c
 *
 *  Created on: Jun 3, 2020
 *      Author: xccai
 */
#include <stdio.h>
#include <stdlib.h>
extern int add(int,int);
extern int sub(int,int);

int main(int argc,char **argv)
{
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);

	int c = add(a,b);
	int d = sub(a,b);

	printf("和为:%d\n",c);
	printf("差为:%d\n",d);
}


