//Programa en C que vaya pidiendo enteros por teclado y llenando un vector de 5 elementos, pase un puntero a dicho vector a una función y desde allí recorre el vector con punteros y lo irá imprimiendo

#include <stdio.h>

void VectPrint(int *ptr1)
{
	int i;
	
	for( i= 0; i < 5; i++)
	{
		printf("\nEl número %d de tu vector es: %d",i, ptr1[i]);
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
	
	int *pt1;
	
	pt1 = &num[0];
	
	VectPrint(pt1);
}

	
	
	
	

