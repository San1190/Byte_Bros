#include <stdio.h>
#define PI 3.141592
int main()
{
	int radio;
	double op;
	
	printf("Introduce el radio de la circunferencia(cm): ");
	scanf("%d", &radio);
	
	op = 2*radio*PI;
	
	printf("Resultado: la longitud de la circunferencia es %.3lfcm", op);
	
	return 0;
}

