//Programa en C que multiplique dos enteros pedidos al usuario. El producto se calculará en un subprograma
#include <stdio.h>
int MultNum(int,int);




int main()
{
	int num1,num2;
	
	printf("Coloca un número: ");
	scanf("%d",&num1);
	
	printf("Coloca otro número: ");
	scanf("%d",&num2);
	
	printf("\nLa multiplicación de ambos números es: %d", MultNum(num1,num2));
	
	
	
}
int MultNum(int a, int b)
{
	return a*b;
}
