#include <stdio.h>

int main()
{
	int x;
	int y;
	int resultado;
	
	printf("Introduce un número: ");
	scanf("%d", &x);
	printf("Introduce otro número: ");
	scanf("%d", &y);
	
	resultado = x + y ;
	printf("Resultado: %d + %d = %d", x , y , resultado);
	
	
	return 0;
	
	
	
}
