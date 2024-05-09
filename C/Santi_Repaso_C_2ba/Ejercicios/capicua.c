#include <stdio.h>

int ComprNum(int *n1)
{
	int x;
	int cont = 0;
	//printf("%ls",n1);
	for( x = 0; x < 5; x++)
	{
		
		if(*(n1+x) == *(n1+4-x))
		{
			cont+=1;
				
		}
		//printf("\n%d\n",*(n1+x));
		
		
		//printf("\n%d\n",*(n1+4-x));
		
	}
	
	//printf("%d",cont);
	
	
	return (cont);
	
}

int main()
{
	int num[5];
	int i,sol=5;
	
	for(i = 0; i <5; i++)
	{
		printf("Coloca un dígito: ");
		scanf("%d",&num[i]);
		//printf("%d",num[i]);
		
	}
	//int j;
	/*for(j = 0; j <5; j++)
	{
		
		printf("\n%d\n",num[j]);
		
	}*/
	
	

	
	if(sol == ComprNum(num))
	{
		printf("Tu número es capicua");
		
		
	}
	else
	{
		printf("Tu número no es capicua");
		
	}
	
	
	
	
	
	
	
	
	
	
}

