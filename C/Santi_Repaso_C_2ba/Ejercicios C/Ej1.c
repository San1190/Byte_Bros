
//Programa en c que llene un vector de 5 elementos desde el teclado con un elemento de valor 0 obligado, pase un puntero al vector a una función, 
//y desde allí multiplique por dos cada uno de los elementos. Se imprimirá desde el programa principal

#include <stdio.h>


void Mult(int *);


int main()
{
	int i = 0 ,j = 0 , x[5];
	
	for(i = 0; i <= 5 ; i++)
	{
		printf("Escribe un número para el vector: ");
		scanf("%d",&x[i]);
		
	}
	
	int *pt;
	
	
	pt = &x[0];
	
	Mult(pt);
	
		for(j = 0; j <= 5 ; j++)
	{
		printf("\nLa posición %d multiplicada por 2 es %d",j,*pt);
		
		pt++;
		
	}
	
	return 0;
	
	
}

void Mult(int *pt1)
{
	int i;
	
	for(i = 0; i<=5; i++)
	{
		*pt1 *=2;
		
		pt1++;
		
		
	}
	
	
	
}

