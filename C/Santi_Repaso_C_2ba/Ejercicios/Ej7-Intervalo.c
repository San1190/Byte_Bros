//Programa en C que pida un número real que pertenezca al intervalo 0 a 10 o al intervalo -20 ,-10. Validar la entrada.

#include <stdio.h>

int main()
{
	int num;
	
	printf("Escriba un número: ");
	scanf("%d",&num);
	
	
		do
		{
			if(((num < 0) || (num > 10)) && ((num > -10) ||(num < -20)))
			{
			printf("Error, debe introducirse un número del 1 al 10 o del -10 al -20");
			printf("\nSeleccione un número:");
			scanf("%d",&num);
			
			}
		}
		while(((num < 0) || (num > 10))  && ((num > -10) ||(num < -20)));
		
		printf("Tú número es: %d",num);

}
