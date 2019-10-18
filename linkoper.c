#include "std.h"

typedef struct Node
{
	int data;
	struct Node *next;
}Node,*pNode;

pNode CreateLink(void);
void PrintList(pNode List);

int main(void)
{
	pNode list;
	list = CreateLink();
	if(list == NULL)
	{
		printf("创建链表失败\n");
		return 1;
	}
	PrintList(list);
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
        scanf("%d", &val);    //    输入链表节点的数据

        Newnode->data = val;    //    把数据赋值给节点数据域
        Tail->next = Newnode;    //    末尾节点指针指向下一个新节点
        Newnode->next = NULL;        //    新节点指针指向为空
        Tail = Newnode;    //    将新节点复制给末尾节点        
    }
    printf("创建链表成功\n");
    return Head;    //    返回头节点
}

void PrintList(pNode List)
{
    pNode P = List->next;    //    首节点赋值给临时节点P
    printf("遍历链表的值为：");
    if (P == NULL)
       printf("链表为空");
    while (P != NULL)        //当临时节点P不为尾节点时，输出当前节点值 
    {
        printf("%d ", P->data);
        P = P->next;
    }
    printf("\n");
}
