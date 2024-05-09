#include <stdio.h>

int main()
{
	int fi, i,x, y;
	printf("Número de términos a mostrar de la sucesión de Fibonacci: ");
	scanf("%d",&fi);
	
	x = 1;
	y = 0;
	while (fi <= 1)
	{
		
		printf("ERROR: por favor introduzca un número mayor o igual que 1");
		
		printf("\nNúmero de términos a mostrar de la sucesión de Fibonacci: ");
		scanf("%d",&fi);
	}
	
	
	for(i = 0; i < fi; i+=2)
	{
		
		printf("%d,",y);
		printf("%d,",x);
		
		y+= x;
		x+= y;
	}
	
  return 0;

	
	
}
