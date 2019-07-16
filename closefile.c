#include "std.h"
#define AF "apple_fp"  
#define SF "samsung_fp"
#define HF "huawei_fp"
#define MF "Mi_fp"
void main(void)
{
    FILE* apple_fp = NULL;
    FILE* samsung_fp = NULL;
    FILE* huawei_fp = NULL;
    FILE* Mi_fp = NULL;
    
    char apple_file_name[100]="app-info";
    char samsung_file_name[100]="sum-info";
    char huawei_file_name[100]="hw-info";
    char Mi_file_name[100]="mi-info";

    apple_fp = fopen(apple_file_name,"w+");
    samsung_fp = fopen(samsung_file_name,"w+");
    huawei_fp = fopen(huawei_file_name,"w+");
    Mi_fp = fopen(Mi_file_name,"w+");
    int result;
    char *nlist = "AF,SF,HF,MF";
    result=close_file(nlist);
}


int close_file(char *namelist)
{
	char file_name[100];
    char nameseq[5][100]={0};
    int pot[5]={0};
    int cnt1 = 0;
    int cnt2 = 0;
    cnt1 = strlen(namelist);
    int i;
    int j=0;
    for(i=0;i<=cnt1;i++)
    {
    	if(namelist[i]==',')
        {
        	cnt2+=1;
            memcpy(nameseq[j],namelist+pot[j],i-pot[j]);
            fclose(nameseq[j]);
            pot[j]=i;
            j+=1;
		}
    }
	printf("¹²ÓÐ·ûºÅ[%d]¸ö\n",cnt2);
    return 0;
}
