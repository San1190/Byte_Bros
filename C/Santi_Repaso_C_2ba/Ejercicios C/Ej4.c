//Programa en C que pida un número de varias cifras (3426) y compruebe con una función si es capicua o no 
#include <stdio.h>

void Capi(int *pn, int*);
int main()
{
	int num[5], x;
	
	printf("Escribe un número: ");
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
