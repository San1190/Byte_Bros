//Cambio de datos entre dos variables utilizando un subprograma y paso por referencia de variables

#include <stdio.h>

void CambiarVariables(int *int1, int *int2) //Intercambia las variables
{
	int aux;
	aux = *int1;
	*int1 = *int2;
	*int2 = aux;
	
}

int main()
{
	int num1, num2;
	
	
	printf("Escribe un número: ");
	scanf("%d",&num1);
	printf("Escribe otro número: ");
	scanf("%d",&num2);
	
	printf("\nLos números seleccionados son:\nA = %d \nB = %d ",num1,num2);
	
	CambiarVariables(&num1,&num2);
	printf("\nLos números intercamibados son:\nA = %d \nB = %d ",num1,num2);
	
	return 0;
	
}
