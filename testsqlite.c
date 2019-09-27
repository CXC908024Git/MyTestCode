#include "std.h"
#include "sqlite3.h"

int callback(void *NotUsed,int argc,char **argv,char **azColName);

int main(int argc,char **argv)
{
	sqlite3 *testdata = NULL;
    char *sql3 = NULL;
	int testsql;
    char name[20]={0};
    char ss[4]={0};
    char act_flag[1+1] = {0};
    int  score;
    char * errmsg;
	char **dbresult;
    char *oneresult;
	int j,nrow,ncolumn,index = 0;
    char dbpath[256]={0};
    
    if(argc < 2)
    {
        printf("参数个数不正确,The Usage:testsqlite model('s' is sel,'a' is add ,'d' is del, 'u' is up) name(if have) score(if have)\n");
        return 1;
    }
    
    strcpy(act_flag,argv[1]);
    strcpy(dbpath,getenv("HOME"));
    strcat(dbpath,"/workspace/database/test.db");
    
    testsql = sqlite3_open(dbpath,&testdata);
	if(testsql == SQLITE_OK)
	{
		printf("数据库打开成功!\n");
	}
    else
	{
		printf("数据库打开失败!\n");
		return -1;
	}

    switch(act_flag[0])
    {
        case 'a':
        case 'A':
            if(argc != 4)
            {
                printf("参数个数不正确,The Usage:testsqlite model('a' or 'A' ) name score\n");
                return 1;
            }
            strcpy(name,argv[2]);
            strcpy(ss,argv[3]);
            score = atoi(ss);
            sql3 = sqlite3_mprintf("insert into tbl_achievement values ('%s','%d')",name,score);
            testsql = sqlite3_exec(testdata,sql3,NULL,NULL,&errmsg); 
            if(testsql == SQLITE_OK)
            {
                printf("新增记录成功!\n");
                sqlite3_free(sql3);
            }
            else
            {
                printf("%s\n",errmsg);
                sqlite3_close(testdata);
                return -1;
            }
            break;
        case 'd':
        case 'D':
            if(argc != 3)
            {
                printf("参数个数不正确,The Usage:testsqlite model('a' or 'A' ) name \n");
                return 1;
            }
            strcpy(name,argv[2]);
            sql3 = sqlite3_mprintf("delete from tbl_achievement where name ='%s'",name);
            testsql = sqlite3_exec(testdata,sql3,NULL,NULL,&errmsg); 
            if(testsql == SQLITE_OK)
            {
                printf("删除记录成功!\n");
                sqlite3_free(sql3);
            }
            else
            {
                printf("%s\n",errmsg);
                sqlite3_close(testdata);
                return -1;
            }
            break;
        case 'u':
        case 'U':
            if(argc != 4)
            {
                printf("参数个数不正确,The Usage:testsqlite model('u' or 'U' ) name score\n");
                return 1;
            }
            strcpy(name,argv[2]);
            strcpy(ss,argv[3]);
            score = atoi(ss);
            sql3 = sqlite3_mprintf("update tbl_achievement set score ='%d' where name ='%s'",score,name);
            testsql = sqlite3_exec(testdata,sql3,NULL,NULL,&errmsg); 
            if(testsql == SQLITE_OK)
            {
                printf("更新记录成功!\n");
                sqlite3_free(sql3);
            }
            else
            {
                printf("%s\n",errmsg);
                sqlite3_close(testdata);
                return -1;
            }
            break;
        case 's':
        case 'S':
        default:
            if(argc == 2)
            {
                testsql = sqlite3_get_table(testdata,"select * from tbl_achievement",&dbresult,&nrow,&ncolumn,&errmsg);
                if(testsql == SQLITE_OK)
                {
                    index = 0;
                    for(int i = 0;i <= nrow; i++)
                    {
                        for(j = 0;j < ncolumn;j++)
                        {
                            printf(" %s",dbresult[index]);
                            index++;
                        }
                        printf("\n");
                    }
                    printf("查询完毕\n");
                    sqlite3_free_table(dbresult);
                }
                else
                {
                    printf("%s\n",errmsg);
                    sqlite3_close(testdata);
                    return -1;
                }
            }
            else
            {
                strcpy(name,argv[2]);
                sql3 = sqlite3_mprintf("select * from tbl_achievement where name ='%s'",name);
                testsql = sqlite3_exec(testdata,sql3,callback,NULL,&errmsg);
                if(testsql == SQLITE_OK)
                {
                    printf("查询完毕\n");
                    sqlite3_free(sql3);
                }
                else
                {
                    printf("%s\n",errmsg);
                    sqlite3_close(testdata);
                    return -1;
                }
            }
            break;
    }
    
    sqlite3_close(testdata);
    return 0;
}

int callback(void *noused,int argc,char **argv,char **colname)
{
    int i;
    for(i = 0;i < argc;i++)
    {
        printf("%s = %s\n",colname[i],argv[i] );

    }
    return 0;
}
