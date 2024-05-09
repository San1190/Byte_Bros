#include <stdio.h>

int main()
{
	int num , cuadrado , cubo;
	
	printf("Bienvenido a la calculadora de potencias v1.0 \n\n");
	
	printf("Introduce la base: ");
	scanf("%d", &num);
	
	cuadrado = num * num;
	cubo = cuadrado * num;
	
	printf("Resultado: %d al cuadrado es %d \n",num, cuadrado);
	printf("Resultado: %d al cubo es %d", num, cubo);
	
	return 0;
	
	
	
	
	
}
