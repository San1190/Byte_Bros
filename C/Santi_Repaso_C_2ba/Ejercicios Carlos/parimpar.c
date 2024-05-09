#include <stdio.h>

int main()
{	
	int num, result;
	
	printf("Coloca un número para saber si es par o impar: ");
	scanf("%d",&num);
	
	result = num%2;
	
	
	
	if (num ==0)
	{
		printf("Tu número es cero ");
		
	}
	else{
		
		if (result == 0)
		{
			printf("Tu número es par");
	
		}
		else
		{
		
			printf("Tu número es impar");
		}
	}		
	return 0;	
		
		
}
