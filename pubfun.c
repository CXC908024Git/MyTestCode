#include "std.h"

extern char *DATETIME(char *famt)
{
	time_t t;
    struct tm *t_buf;
    char result[32+1]={0};
	char *timep = NULL;
	timep = result;

    time(&t);
    t_buf = localtime(&t);
    if(!memcmp(famt,"yyyymmdd", 8))
	{
		sprintf(result, "%04d%02d%02d",t_buf->tm_year + 1900, t_buf->tm_mon + 1, t_buf->tm_mday);
	}
    else if(!memcmp(famt,"yyyymmddHHMMSS", 17))
	{
 	 	sprintf(result, "%04d%02d%02d %02d:%02d:%02d",t_buf->tm_year + 1900, t_buf->tm_mon + 1, t_buf->tm_mday,
            t_buf->tm_hour, t_buf->tm_min, t_buf->tm_sec);
    }
    else
	{
		sprintf(result, "%04d-%02d-%02d %02d:%02d:%02d",t_buf->tm_year + 1900, t_buf->tm_mon + 1, t_buf->tm_mday,
            t_buf->tm_hour, t_buf->tm_min, t_buf->tm_sec);
	}
    return timep;
}

extern char *itoa(int num)
{
	int buf[11];
    char str[12]={0};
    char *p=NULL;
    p=str;
    int temp,i=0,j=0;
    temp=(num<0)?(-num):num;
    while(temp!=0)
    {
        buf[i]=(temp % 10)+'0';
        temp=temp/10;
        i++;
    }
    if(num<0)
    {
        str[0]='-';
        j++;
    }
    while((--i)>=0)
    {
        str[j]=buf[i];
        j++;
    }
    return p;
}
