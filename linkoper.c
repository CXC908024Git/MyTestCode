#include "std.h"

typedef struct Node
{
	int data;
	struct Node *next;
}Node,*pNode;

pNode CreateLink(void);
void PrintList(pNode List);
void SelList(pNode List);
void DelList(pNode List);
void InsList(pNode List);
void UpList(pNode List);

int main(int argc,char **argv)
{
	pNode list;
	list = CreateLink();
	if(list == NULL)
	{
		printf("创建链表失败\n");
		return 1;
	}
    switch(argv[1][0])
    {
        case 'p':
            PrintList(list);
            break;
        case 's':
            SelList(list);
            break;
        case 'd':
            DelList(list);
            break;
        case 'i':
            InsList(list);
            break;
        case 'u':
            UpList(list);
            break;
        default:
            break;
    }
	return 0;
}

pNode CreateLink(void)
{
	int len; //节点个数
	int val; //节点数据
	pNode Head = malloc(sizeof(Node));//创建头节点
    if (Head == NULL)    //  判断头节点是否申请成功
    {
        printf("空间分配失败 \n");
        exit(1);
    }
	pNode Tail = Head; 
	Tail->next = NULL;
	//new节点永远跟随头节点

	printf("请输入需要创建的节点数:\n");
	scanf("%d",&len);
	for (int i = 0; i < len; i++)
	{
        pNode Newnode = malloc(sizeof(Node));    //    分配一个新节点
        if (Newnode == NULL)
		{
            printf("分配新节点失败\n");
            return NULL;
        }
        printf("请输入第 %d 个节点的数据：", i + 1);
        scanf("%d", &val); 

        Newnode->data = val; 
        Tail->next = Newnode;    //尾节点的next指针指向下一个新节点
        Newnode->next = NULL;    //新节点的next指向空，代表链表结束
        Tail = Newnode;          //将新节点地址指向尾节点      
    }
    printf("创建链表成功\n");
    return Head;    //    返回头节点
}

void PrintList(pNode List)
{
    pNode P = List->next;    //    首节点赋值给临时节点P
    printf("遍历链表的值为：");
    if (P == NULL)
	{
       printf("链表为空");
	   exit(0);
	}
    while (P != NULL)        //当临时节点P不为尾节点时，输出当前节点值 
    {
        printf("%d ", P->data);
        P = P->next;
    }
    printf("\n");
}

void SelList(pNode List)
{
	pNode P  = List->next;
	int i,cnt;
	cnt=1;
	printf("请输入需要查询的节点号:\n");
	scanf("%d",&i);
	if(P == NULL)
	{
	   printf("链表为空"); 
	   exit(0);
	}
	while (P != NULL)
	{
		if(cnt==i)
		{
			printf("第[%d]个节点的值为[%d]\n",cnt,P->data);  
			break;
		}
		else
		{
			P = P->next;
			cnt+=1;
		}
	}
}

void DelList(pNode List)
{
	pNode P  = List->next;
	pNode PF,PD; //PD是待删除节点,PF是跟随节点
	PD = P;
	int nbr,i;
	nbr=1;
	printf("请输入需要删除的节点号:\n");
	scanf("%d",&i); 
	if(P == NULL)
	{
       printf("链表为空");
	   exit(0);
	}
	while (P != NULL) 
	{
        if(i==1)
        {
            List->next = P->next;
            free(P);
            break;
        }
        else
        {
            if(nbr==i)
            {
                PF->next = PD->next;
                free(PD);
                break;
            }
            else
            {
                PF = PD;
                PD = PD->next;
                nbr+=1;
            }
        }
	}
	printf("删除节点后");
	PrintList(List);
}

void InsList(pNode List)//在第i个元素的后面插入
{
	pNode P  = List->next;
	pNode PI;//PI是跟随节点
	pNode PN = malloc(sizeof(Node));//PN是新节点
	PI = P;
	int nbr,i,val;
	nbr=1;
	printf("请输入需要插入新节点的位置:\n");
	scanf("%d",&i);
	printf("请输入需要插入新节点的值:\n");
	scanf("%d",&val);
	if(P == NULL)
	{
		printf("链表为空"); 
		exit(0);
	}
	while (P != NULL)
	{
		if(nbr==i)
		{
	        PN->data = val;
			PN->next = PI->next;
			PI->next = PN;
			break;
		}
		else
		{
			nbr+=1;
			PI = PI->next; 
		}
	}
	printf("插入后");
	PrintList(List); 
}

void UpList(pNode List)
{
	pNode P  = List->next;
	pNode PI;//PI是跟随节点
    PI = P;
	int nbr,i;
	int val = 0;
	nbr =1;
	printf("请输入需要更新的节点位置:\n");
	scanf("%d",&i);
	printf("请输入需要更新的值:\n");
	scanf("%d",&val);
	if(P == NULL)   
	{
		printf("链表为空");  
		exit(0);
	}
	while (P != NULL)
	{
		if(nbr==i)
		{
			PI->data = val;
			break;
		}
		else
		{
			nbr+=1; 
			PI = PI->next;
		}
	}
	PI = PI->next;
	printf("更新后");
	PrintList(List);
}
