#include "std.h"
void main(void)
{
	char buff[10]="123456789";
	FILE *FS[5] = {NULL};
    
    char apple_file_name[100]="app-info";
    char samsung_file_name[100]="sum-info";
    char huawei_file_name[100]="hw-info";
    char Mi_file_name[100]="mi-info";

    FS[0] = fopen(apple_file_name,"a+");
	if (FS[0] == NULL)
    {
        printf("文件打开失败:%s",apple_file_name);
    }
	fwrite(buff,strlen(buff),1,FS[0]);
	FS[1] = fopen(samsung_file_name,"a+");
    if (FS[1]  == NULL)
	{
		 printf("文件打开失败:%s",samsung_file_name);
	}
	fwrite(buff,strlen(buff),1,FS[1]);
    FS[2] = fopen(huawei_file_name,"a+");
	if (FS[2] == NULL)
	{
		printf("文件打开失败:%s",huawei_file_name);
	}
	fwrite(buff,strlen(buff),1,FS[2]);
    FS[3] = fopen(Mi_file_name,"a+");
    if (FS[3] == NULL)
	{
		printf("文件打开失败:%s",Mi_file_name);
	}
	fwrite(buff,strlen(buff),1,FS[3]);
    int result;
    result=close_file(FS,2);
    fwrite(buff,strlen(buff),1,FS[0]);
	fwrite(buff,strlen(buff),1,FS[1]);
	fwrite(buff,strlen(buff),1,FS[2]);
}


int close_file(FILE *fs[],int sum)
{
    int i;
    for(i=0;i<=sum-1;i++)
    {
        fclose(fs[i]);
    }
	printf("共关闭文件[%d]个\n",i);
	return 0;
}
