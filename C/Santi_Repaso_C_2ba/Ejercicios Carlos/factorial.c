#include <stdio.h>

int main()
{
	int i, num , result;
	
	printf("Escribe un número para hacer su factorial: ");
	scanf("%d",&num);
	
	result = 1;
	for(i = 1 ; i <= num ;i ++)
	{
		result = result* i;
	}
	
	printf("%d! = %d", num , result);
	
	return 0;
	
	
	
}
