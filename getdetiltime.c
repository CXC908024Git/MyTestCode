#include "std.h"

int main(void)
{
struct timeval tv;
static char str[30];
char str1[20];
char *ptr;

gettimeofday(&tv,NULL);
ptr = ctime(&tv.tv_sec);
strcpy(str, &ptr[11]);
sprintf(str1,"%ld\n",tv.tv_usec);
printf("%3.3s\n",str1);
snprintf(str+8, sizeof(str)-8, ".%3ld", tv.tv_usec);
printf("%s\n",str);
char   usec[7];
memset(usec,' ',sizeof(usec));
short b=123;
snprintf(usec,7,"%06d", b);
printf("%s\n",usec);
return 0;
}
