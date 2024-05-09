#include <stdio.h>

int main()
{
	
	int ini, fin, cont;
	
	
	printf("Introduce el número inicial: ");
	scanf("%d",&ini);
	
	printf("Introduce el número final: ");
	scanf("%d",&fin);
	
	
	
	cont = ini;
	
	if ( cont % 2 == 0)
	{
		cont+=2;	
		
	}
	else
	{
		cont+= 1;
	}
		
	while (fin >= cont)
		{
			printf("%d\n",cont);
			cont +=2 ;			
		}
		
		
	
	//while (fin > cont)
	//{
		//if ( cont % 2 == 0)
		//{
			//printf("%d\n",cont);
		//}
		//cont +=1 ;
	//}
	
	
	return 0;
	
	
}
