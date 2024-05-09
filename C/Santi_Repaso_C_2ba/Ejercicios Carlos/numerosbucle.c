#include <stdio.h>

int main()
{
	int ini, fin, cont, inter;
	
	
	printf("Introduce el número inicial: ");
	scanf("%d",&ini);
	
	printf("Instroduce el número final: ");
	scanf("%d",&fin);
	
	printf("Introduce el intervalo del bucle: ");
	scanf("%d",&inter);
	
	cont = ini;
	
	while (fin > cont)
	{
		printf("%d\n",cont);
		
		cont += inter;
		
	}
	
		
	return 0;
	
}
