#include <stdio.h>

int main()
{
	int i, j ,p;
	
	p = 97;
	
	for(i = 8; i >= 0; i--)
	{
		if( i >= 1)
		{
			printf("%d ",i);
		}
		
		for( j = 1; j <= 8; j++)
		{
			if (((j+i)% 2 == 0 && i !=0))
			{
				printf("B ");
				
			}
			if (((j+i)% 2 != 0 && i !=0))
			{
				printf("N ");
				
				
			}
	
			if( i == 0)
			{
				if(j == 1)
				{
					printf("  ");
					putchar(p);
				}
				else
				{
					printf(" ");
				
					putchar(p);
				
				
				}
				p+= 1;
					
				
			}
			
		
		
			
			
		}
		printf("\n");
		

	
	}
		
	
	
	
	
	
	
	
	
	
	
	
}
