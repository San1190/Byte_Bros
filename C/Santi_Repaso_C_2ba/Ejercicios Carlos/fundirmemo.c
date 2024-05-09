#include <stdio.h>

void FunRara(int a , int *b)
{
	a++;
	(*b)++;
	
	printf("%d\n", a);
	printf("%d\n",*b);
	

	
	
}
int main()
{
	int num1 = 5;
	int num2 = 5;
	
	FunRara(num1,&num2);
	
	
	printf("%d\n", num1);
	printf("%d\n",num2);
	
	
	return 0;
}
