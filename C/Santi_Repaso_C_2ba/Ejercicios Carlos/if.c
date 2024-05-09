#include <stdio.h>

int main()
{
	int num;
	
	
	printf("Introduce un número: ");
	scanf("%d",&num);
	
	if (num >= 10)
	{
		printf("Tu número es mayor o igual a 10");
	}
	else
	{
		printf("Tu número es menor a 10");
		
	}

	return 0;

}

