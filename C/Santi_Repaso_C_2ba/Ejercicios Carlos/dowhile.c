#include <stdio.h>

int main()
{
		
	int ini, fin, cont;
	
	
	printf("Introduce el número inicial: ");
	scanf("%d",&ini);
	
	printf("Introduce el número final: ");
	scanf("%d",&fin);
	
	cont = ini;
	
	do
	{
		printf("%d\n",cont);
		cont += 1;
		
		
		
	}
	while(fin >= cont);
	
	
	return 0;
	
	
}
