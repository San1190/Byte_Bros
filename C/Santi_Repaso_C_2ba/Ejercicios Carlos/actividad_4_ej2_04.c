#include <stdio.h>

int main()
{
	char letra1[2];
	char letra2[2];
	
	printf("Introduce un caracter: ");
	scanf("%s", letra1);
	
	printf("Introduce otro caracter: ");
	scanf("%s", letra2);
	
	
	printf("Los caracteres son \"%s\" y \"%s\"", letra1 , letra2);
	
	return 0;	
	
	
	
}
