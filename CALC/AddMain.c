/*
 * AddMain.c
 *
 *  Created on: Jun 3, 2020
 *      Author: xccai
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "tab.h"
extern int add(int,int);
extern int sub(int,int);
extern int HDtab(int,TblStuPoint*);
extern int lMDCommit(void);
extern int lMDConnect(void);
extern int lMDDisConnect(void);


int main(int argc,char **argv)
{
	int a = atoi(argv[1]);
	int b = atoi(argv[2]);

	int ret = 0;
	ret = lMDConnect();

	int c = add(a,b);
	int d = sub(a,b);

	TblStuPoint tbsp;
	memset(&tbsp,0x00,sizeof(tbsp));
	memcpy(tbsp.id_nbr,"002",sizeof(tbsp.id_nbr));

	if(ret==0)
	{
	    printf("database connect ok!\n");
	    ret = HDtab(1,&tbsp);
	    if(ret==0)
	    {
	       printf("name=[%4.4s],age=[%d],point=[%4.2f]\n",tbsp.name,tbsp.age,tbsp.point);
	       printf("add:%d\n",c);
	       printf("sub:%d\n",d);
	    }
	    else
	    {
	        printf("[%d]\n",ret);
	        return -1;
	    }
	    memset(&tbsp,0x00,sizeof(tbsp));
	    memcpy(tbsp.id_nbr,"001",sizeof(tbsp.id_nbr));
	    ret = HDtab(2,&tbsp);
	    ret = HDtab(3,&tbsp);
	    int cnt = 0;
	    while(1)
	    {
	        ret = HDtab(4,&tbsp);
	        if(ret == 1403)
	        {
	        	printf("Cur over!\n");
	        	printf("cnt=[%d]\n",cnt);
	        	break;
	        }
	        else if(ret != 1403 && ret != 0)
	        {
	        	printf("ret = [%d],FETCH CUR FAILED\n",ret);
	        	return -1;
	        }
	        else
	        {
	        	printf("name=[%4.4s],age=[%d],point=[%4.2f]\n",tbsp.name,tbsp.age,tbsp.point);
	        	cnt++;
	        }
	    }
	    ret = HDtab(5,&tbsp);
	    lMDDisConnect();
	    return 0;
	 }
	 else
	 {
	     printf("test error\n");
	     return -1;
	 }
}


