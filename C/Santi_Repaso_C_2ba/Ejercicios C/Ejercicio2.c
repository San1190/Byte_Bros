//Programa en el que pida un n�mero por teclado y la potencia a la que se quiere elevar. Dicho c�lculo lo realizar� un subprograma. Se imprimir� desde el programa principal.(referencia)

#include <stdio.h>

void Poten(int*,int*);

int main()
{
	int base, pot;
	
	printf("Coloca un n�mero: ");
	scanf("%d",&base);
	
	printf("Coloca la potencia que deseas que el n�mero se eleve: ");
	scanf("%d",&pot);
	
	
	
	Poten(&base,&pot);
	
	printf("\nEl resultado es: %d",base);
	
	
	
	return 0;
	
}

void Poten(int *b,int *p)
{
	int i,sol;
	sol = 1;
	for(i = 0;i < *p; i++)
	{
		sol*=*b;	
		
	}
	*b = sol;
}
