#include <stdio.h>

int main()
{
	
	int n1,n2,n3;
	
	printf("Introduce un primer número: ");
	scanf("%d",&n1);
	
	printf("Introduce un segundo número: ");
	scanf("%d",&n2);
	
	printf("Introduce un tercer número: ");
	scanf("%d",&n3);
	
	if ((n1 == n2) && (n2 == n3))
	{
		printf("Los tres números son iguales");
		
	}
	else if ((n1 == n2)  && (n3 != n2))
	{
		printf("El primer y el segundo número son iguales, y el tercero es diferente");
		
	}
	
	else if ((n1 == n3) && (n2 != n1))
	{
		printf("El primer y el tercer número son iguales, y el segundo es diferente");
		
	}
	
	else if ((n2 == n3) && (n1 != n2))
	{
		
		printf("El segundo y el tercer número son iguales, y el primero es diferente");
		
	}
		
	else
	{
		printf("Los tres números son diferentes");
		
	}
	
	
	
	return 0;
}
