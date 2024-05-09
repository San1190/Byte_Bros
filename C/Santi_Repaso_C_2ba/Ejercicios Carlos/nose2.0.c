#include <stdio.h>

int main()
{
	
	int x,y,z,t;
	int max, min;
	
	printf("Introduzca número 1: ");
	scanf("%d",&x);
	
	printf("Introduzca número 2: ");
	scanf("%d",&y);
	
	printf("Introduzca número 3: ");
	scanf("%d",&z);
	
	printf("Introduzca número 4: ");
	scanf("%d",&t);
	
	
	max = x;
	min = x;
	
	if (max < y)
	{
		max = y;
		
	}
	if (max < z)
	{
		max = z;
		
	}
	if(max < t)
	{
		max = t;
		
		
	}
	
	if (min > y)
	{
		min = y;
		
	}
	if (min > z)
	{
		min = z;
		
	}
	if(min> t)
	{
		min = t;
		
		
	}
	
	
	printf("El número mayor es %d y el menor %d",max,min);
	

	
	return 0;
}
