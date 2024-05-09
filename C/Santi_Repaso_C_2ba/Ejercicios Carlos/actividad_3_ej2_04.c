#include <stdio.h>
#include <math.h>
int main()
{
	double base , expo , resultado;
	
	
	printf("Bienvenido a la calculadora de potencias v2.0 \n\n");
	
	printf("Introduce la base: ");
	scanf("%lf", &base);
	
	printf("Introduce el exponente: ");
	scanf("%lf", &expo);
	
	resultado = pow(base, expo);
	
	printf("Resultado: %.2lf elevado a %.2lf es %.0lf", base, expo, resultado);
	
	return 0;
	
	



	

	
}
