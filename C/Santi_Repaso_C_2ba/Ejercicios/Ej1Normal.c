//Cambio de datos entre dos varibales


#include <stdio.h>

int main()
{
	int num1,num2,aux;
	
	printf("Escribe un número: ");
	scanf("%d",&num1);
	printf("Escribe otro número: ");
	scanf("%d",&num2);
	
	printf("\nLos números seleccionados son:\nA = %d \nB = %d ",num1,num2);
	
	aux = num1;
	num1 = num2;
	num2 = aux;
	printf("\nAhora con las variables cambiadas:\nA = %d \nB = %d ",num1,num2);
	
	return 0;
}
