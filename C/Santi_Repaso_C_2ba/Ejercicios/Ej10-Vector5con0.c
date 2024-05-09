//Programa en c que llene un vector de 5 elementos desde el teclado con un elemento de valor 0 obligado, pase un puntero al vector a una función, lo recorra e imprima por pantalla la posición de dicho elemento, si no dice nada se imprime desde donde queráis

#include <stdio.h>

void VectPrint(int *ptr1)
{
	int i;
	
	for( i= 0; i < 5; i++)
	{
		if( ptr1[i] == 0)
		{
			printf("\nEl número 0 está en la posición %d del vector", i+1);			
		}
	
	}
}

int main()
{
	int i, num[5];
	
	
	
	for( i= 0; i < 5; i++)
	{
		printf("Selecciona el número %d del vector: ",i);
		scanf("%d", &num[i]);	
	}
	
	int *p1;
	
	p1 = num;
	
	VectPrint(p1);
}
