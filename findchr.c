#include "std.h"

#define max_len 1024
int a=3;
int b=4;
int  pos[1024]={0};
static int *findstr(char *p, char dc,int *pot);

int main(int argc,char **argv)
{
	int c = 15;
	int d = 20;
    int cnt =0;
	int m = 0;
    char testm[20+1] = {0};
    char buff[1024+1]={0};
	int count =0;
    memcpy(buff,argv[1],strlen(argv[1]));
	#if 0
	result = f1(c,d);
	if(result)
	{
		printf("f1 cal result is [%d]!\n",result);
    }
    result = f2(c,d);
	if(result)
	{
		printf("f2 cal result is [%d]!\n",result);
    }
	#endif

	FILE *fr = NULL;
	fr=fopen("/app/amesb/test/AEC/testcode/cxc/src/test.txt","w+");
	if(fr == NULL)
	{
    	printf("Open file failed!\n");
        return -1;
	}
    fwrite(buff,1024,1,fr);
    fclose(fr);
    fr=fopen("/app/amesb/test/AEC/testcode/cxc/src/test.txt","a+");
	fgets(testm,strlen(buff)+1,fr);
    fclose(fr);
	char *str = NULL;
    str = testm;
	char ch = argv[2][0];
	int *result=NULL;
    result=findstr(str,ch,pos);
	if(*result != 0)
	{
		for(m=0;m<=max_len-1;m++)
        {
			if(*(result+m) != 0)
			{
				printf("chr position is [%d]\n",*(result+m));
                count+=1;
			}
			else
			{
				break;
			}
		}
	}
	else
    {
    	printf("des chr is NOT FOUND\n");
		return -1;
    }
	printf("des chr共出现[%d]次\n",count);
	return 0;
}

int f1(int x, int y)
{
	int z = 1;
	return(x+y+z+a);
}

int f2(int x, int y)
{
	int z =10;
    return(x+y+z+a);
}

int *findstr(char *p, char dc,int *pot)
{
	int len = 0;
	len = strlen(p);
	int i=0;
    int j=0;
    for(i=0;i<=len-1;i++)
    {
		if(*(p+i) == dc)
		{
			*(pot+j)=i+1;
			j=j+1;
		}
		else
        {
	    	continue;
		}
	}
	return pot;
}
