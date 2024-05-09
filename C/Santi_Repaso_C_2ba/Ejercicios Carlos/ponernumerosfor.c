#include <stdio.h>

int main()
{
	int i, x,salir = 0;
	
	for(i= 1; (i <10 && salir == 0);i++)
	{
		printf("Escribe el %dº numero:", i);
		scanf("%d",&x);
		if (x == 13)
		{
			salir = 1;
			printf("ERROR");
			//break;
			//i = 100000;
			
		}
		else
		{
			printf("Tú número es %d\n", x);
			
			
		}
	}
	
	
	return 0;
	
	
	
}
