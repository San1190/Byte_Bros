//Programa en C que pida un n�mero de varias cifras (3426) y compruebe con una funci�n si es capicua o no 
#include <stdio.h>

void Capi(int *pn, int*);
int main()
{
	int num[5], x;
	
	printf("Escribe un n�mero: ");
	scanf("%d",&num);
	
	
	int *pt;
	
	*pt = num;
	
	x = strlen(num);
	
	Capi(&pt,&x);
	
	
}
 void Capi(int *pn, int *x)
 {
 	int i;
 	
 	for(i = 0; i<= x; i++)
 	{
	 
	 }
 	
 	
 }
