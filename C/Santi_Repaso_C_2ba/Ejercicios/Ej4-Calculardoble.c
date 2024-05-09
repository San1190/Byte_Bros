//Progama en C que calcule el doble de un número pedido al usuario.Se hará en un subprograma.Se deberá imprimir el resultado desde el progama principal

#include <stdio.h>

int DoubNum(int);
int main()
{
	
	int num;
	
	printf("Coloca un número: ");
	scanf("%d",&num);
	
	printf("El doble del número es: %d", DoubNum(num));	
}

int DoubNum(int a)
{
	return a*2;
	
	
}
