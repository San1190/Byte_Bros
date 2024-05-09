#include <stdio.h>

int main()
{
	
	int x,y,z,t;
	int max1,max2, min1,min2;
	
	printf("Introduzca número 1: ");
	scanf("%d",&x);
	
	printf("Introduzca número 2: ");
	scanf("%d",&y);
	
	printf("Introduzca número 3: ");
	scanf("%d",&z);
	
	printf("Introduzca número 4: ");
	scanf("%d",&t);
	
	if((x > y) || (x < y))
	{
		max1= x; 
		min1 = x;
	}
	else
	{
		max1 = y;	
		min1 = y;
		
	}
	if ( z > t)
	{
		max2 = z;
		min2 = z;
		
		
		
	}
	else
	{
		max2 = t;
		min2 = t;
	}
	
	if (max1 < max2)
	{
		printf("El número mayor es %d",max1);
	}
	else
	{
		printf("El número mayor es %d", max2);
		}
	if (min1> min2)
	{
		printf("El número menor es %d",max1);
	}
	else
	{
		printf("El número menor es %d", max2);
		}
	
	return 0;
	
	
	
}

