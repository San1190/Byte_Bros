#include <stdio.h>
#include <stdlib.h>

int main()
{
	FILE *F = fopen("texto1.txt", "r");
	
/*1
 char texto;
 while(!feof(F))
	{
		texto = fgetc(F);
		
		printf("%c", texto);
		
		
		
		
	}
	
	fclose(F);
		*/
		
	
	
	/*while(fscanf(F, "%[^\n ] ", linea) != EOF)
	{
		//printf("> %s\n", linea);
		
		if (atoi(linea) < 50)
		{
			printf("Es menor a 50\n");
			
			
		}
		else if (atoi(linea) > 50)
		{
			printf("Es mayor a 50\n");
	
		}
		else
		{
			printf("El numeroes 50\n");
			
		}
	}
	
	fclose(F);
	
	printf("TEST: %s", linea);
	*/
	char linea[200];
	char palabra[2000];
	int count=0;
	
	printf("Introduce que palabra quieres buscar:");
	scanf("%s", palabra);
	while(fscanf(F, "%[^\n ] ", linea) != EOF)
	{
		if(strcmp(linea,palabra) == 0)
		{
			count+=1;
		}
		
		
		//printf("> %s\n", linea);
		
	}
	printf("Hay %d '%s'",count, palabra);
	fclose(F);
	
	
	
	
	
	
	
	return 0;
	
	
	
	
	
	
	
}
