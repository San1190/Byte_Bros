//Programa en C que sea una función que reciba un número entero n y devuelve 1 si n es impar y divisible por 7 y devuelve 0 en caso contrario

#include <stdio.h>
int ParImp(int);
int main()
{
	int num;
	printf("Escribe un número: ");
	scanf("%d",&num);
	
	if(ParImp(num) == 1)
	{
		printf("Divisible por 7 e impar");
		
	} 
	else
	{
		printf("No es divisible por 7 o no es par");		
		
		
		
	}
		
}

int ParImp(int num)
{
	int i = 0;
	
	if((num % 7 == 0) && (num % 2 != 0))
	{
		i = 1;		
	
	}
	
	return(i);
}
