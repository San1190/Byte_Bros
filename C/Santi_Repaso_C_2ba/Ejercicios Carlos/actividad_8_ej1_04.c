#include <stdio.h>

int CalcularFactorial(int);
int ComprobarNumero(int);
void MostrarError();
void MostrarSolucion(int , int );
int SolicitarNumero();





void MostrarError()
{
	printf("ERROR: el número debe estar comprendido entre 0 y 12.\n");	
}



int SolicitarNumero()
{
	int num;
	
	printf("Introduzca un número de 0 a 12 para calcular su factorial: ");
	scanf("%d", &num);
	
	return(num);
	
	
}


int CalcularFactorial(int num)
{
	int i,result;
	
	result = 1;
	for(i = 1 ; i <= num ;i ++)
	{
		result = result* i;
	}
	
	return(result);
	
	
}



int ComprobarNumero(int num)
{
	int bina = 0;
	if( (0 <= num) && (num <= 12))
	{
		bina = 1;
	}
	
	return (bina);
}



void MostrarSolucion(int num,int sol)
{
	printf("%d! = %d", num , sol);
}



int main()
{
	
	int sol,num,bina;
	num = SolicitarNumero();
	bina = ComprobarNumero(num);
	while(bina == 0)
	{
		MostrarError();
		num = SolicitarNumero();
		bina = ComprobarNumero(num);
		

	}
	sol = CalcularFactorial(num);
	MostrarSolucion(num,sol);
	
}
