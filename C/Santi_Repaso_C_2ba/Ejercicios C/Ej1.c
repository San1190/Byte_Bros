
//Programa en c que llene un vector de 5 elementos desde el teclado con un elemento de valor 0 obligado, pase un puntero al vector a una funci�n, 
//y desde all� multiplique por dos cada uno de los elementos. Se imprimir� desde el programa principal

#include <stdio.h>


void Mult(int *);


int main()
{
	int i = 0 ,j = 0 , x[5];
	
	for(i = 0; i <= 5 ; i++)
	{
		printf("Escribe un n�mero para el vector: ");
		scanf("%d",&x[i]);
		
	}
	
	int *pt;
	
	
	pt = &x[0];
	
	Mult(pt);
	
		for(j = 0; j <= 5 ; j++)
	{
		printf("\nLa posici�n %d multiplicada por 2 es %d",j,*pt);
		
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

