//Progama en C que calcule el doble de un entero pedido a un usuario con un subprogama pero con el paso de parametros por referencia. Se imprimirá el resultado desde el programa principalç

#include <stdio.h>
void DoubNum(int*);
int main()
{
	int num;
	
	printf("Coloca un número: ");
	scanf("%d",&num);
	
	
	DoubNum(&num);
	printf("El doble del número es: %d",num);	
	
	
	
}

void DoubNum(int *a)
{
	*a *=2;
	
}
