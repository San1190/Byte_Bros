#include <stdio.h>

int main()
{
	
	int num, cont;
	
	printf("Escribe el número con el que quieras la cuenta atrás: ");
	scanf("%d",&num);
	printf("Escribe el intervalo del contador: ");
	scanf("%d",&cont);
	
	while (num > 0)
	{
		
		if (num == 5)
		{
			printf("PREPARADOS\n");
			
		}
		
		else
		{
			printf("%d\n",num);
		}
		
		num-=cont;
		
			
			
			
		
		
		
	}
	printf("Ignición!!!!!!!!!!!!");
	
	return 0;
	
	
	
	
	
	
}
