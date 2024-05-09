#include <stdio.h>


int potencia(int base, int expo)
{
	int sol,i;
	sol = 1;
	for(i = 1;i <= expo; i++)
	{
		sol*=base;
		
		
	}
	
	return(sol);
	
	
	
}


int main()
{
	int  sol, base , expo;
	
	printf("Escriba una base: ");
	scanf("%d",&base);
	printf("Escriba un exponente: ");
	scanf("%d",&expo);
	sol = potencia(base,expo);
	
	
	printf("La solción es %d",sol);
	
	return 0;
	
	
}


