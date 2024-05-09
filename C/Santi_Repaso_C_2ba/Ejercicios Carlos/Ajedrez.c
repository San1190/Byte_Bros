#include <stdio.h>

int main()
{
	int i, j ,p;
	
	p = 97;
	
	for(i = 8; i >= 0; i--)
	{
		printf("%d ",i);
		
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
				
				
				putchar(p);
				
				p+= 1;
			}
			
		
		
			
			
		}
		printf("\n");
		

	
	}
		
	
	
	
	
	
	
	
	
	
	
	
}
