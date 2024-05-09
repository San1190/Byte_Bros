#include <stdio.h>

int main()
{
	
	int num1,num2, resto, op;
	
	printf("Introduce un primer número: ");
	scanf("%d", &num1);
	
	printf("Introduce un segundo número: ");
	scanf("%d", &num2);
	
	
	
	
	if (num2 == 0)
	{
		printf("No se puede dividir entre 0");
	}
	
	else
	{
		resto = num1%num2;
		op = num1/num2;
		
		if (resto == 0)
		{
			printf("%d es divisible entre %d y su division es %d", num1,num2, op);
		
		}
		else
		{
		
			printf("%d no es divisible entre %d",num1,num2);
		}
	}
	
	
	 
	
	
	
	
	
	
	
}
