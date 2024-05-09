/*#include <stdio.h>

int main()
{
	int max , min , i, x;
	
	printf("Introduce el extremo inferior del intervalo: ");
	scanf("%d",&min);
	
	printf("Introduce el extremo superior del intervalo: ");
	scanf("%d",&max);
	
	x = 0;
	
	if(min <= max)
	{
		for(i= min; i <= max; i++)
		{
			if(i % 3 == 0)
			{
				if ((i >= max) ||(i >= max-1)|| (i >= max-2))
				{
					printf("%d",i);
				}
				else
				{
					printf("%d,",i);
				}
				
				x+=1;
				
				
			}
			
			
		
		
		}
	
		
		printf("\nCantidad de múltiplos de 3: %d",x);
	}
	else
	{
		printf("ERROR: el extremo inferior debe ser <= que el superior.");
		
		
		
		
	}
	return 0;
	
}
*/
#include <stdio.h>

int main()
{
	int max , min , i, x;
	
	printf("Introduce el extremo inferior del intervalo: ");
	scanf("%d",&min);
	
	printf("Introduce el extremo superior del intervalo: ");
	scanf("%d",&max);
	
	
	while(max < min)
	{
		printf("ERROR: el extremo inferior debe ser <= que el superior.\n");
		
		printf("Introduce el extremo inferior del intervalo: ");
		scanf("%d",&min);
	
		printf("Introduce el extremo superior del intervalo: ");
		scanf("%d",&max);
		
	}
	
	x = 0;
	
	for(i= min; i <= max; i++)
		{
			if(i % 3 == 0)
			{
				if ((i >= max) ||(i >= max-1)|| (i >= max-2))
				{
					printf("%d",i);
				}
				else
				{
					printf("%d,",i);
				}
				
				x+=1;
				
				
			}
			
			
		
		
		}
	
		
		printf("\nCantidad de múltiplos de 3: %d",x);
		return 0;
	}


	

