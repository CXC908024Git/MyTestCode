#include "sqlca.h"
#define SELECT      1
#define CUR         2
#define CUR_OPEN    3
#define CUR_FETCH   4
#define CUR_CLOSE   5
#define UPDATE      6

typedef struct{
char id_nbr[8+1];
char name[30+1];
int age;
float point;
}TblStuPoint;

