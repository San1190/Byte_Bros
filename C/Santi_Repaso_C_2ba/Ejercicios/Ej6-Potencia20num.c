//Progama en c que calcule el cuadrado de los 20 primeros números con un subprogama el resultado se irá imprimiendo desde el programa principal.

#include <stdio.h>
int Pot(int);
int main()
{
	int i;
	
	for (i = 0; i <20; i++)
	{
		
		printf("%d\n",Pot(i));	
		
	}

	
}

int Pot(int a)
{
	return a *= a;
	
}
