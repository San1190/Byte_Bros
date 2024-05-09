#include <stdio.h>

int main()
{
	int grados;
	float resultado;

	printf("Introduce en grados Celsius la temperatura de hoy: ");
	scanf("%d", &grados);

	resultado = ( grados * 1.8 ) + 32;

	printf("La temperatura de hoy es de %d ºC / %.1fºF", grados, resultado);

	return 0;


}
