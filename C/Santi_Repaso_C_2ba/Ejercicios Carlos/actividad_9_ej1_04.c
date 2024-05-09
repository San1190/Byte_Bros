#include <stdio.h>
#define NCOL 3
#define NLIN 3


void RellenarMatriz(int matriz[][NCOL])
{
	int i, j;
	
	for(i = 0 ;i < NCOL; i++)
	{
		for(j = 0; j < NCOL; j++)
		{
			printf("Introduzca nu número para la posición (%d,%d): ", i,j);
			scanf("%d",&matriz[i][j]);
				
		}		

	}
	
		
}
void SumaMatriz(int matriz_A[][NCOL], int matriz[][NCOL])
{
		int i, j;
		int matrizsum[NLIN][NCOL];
	printf("\nLa suma de las matrices es:\n");
	printf("\n");
	for(i = 0 ; NCOL > i; i++)
	{
		printf("| ");
		for(j = 0; NCOL > j; j++)
		{
			matrizsum[i][j] = matriz_A[i][j] + matriz[i][j];
			printf("  %d  ",matrizsum[i][j]);
			
		
			
			
			
		}
		printf(" |");
		printf("\n");
	} 
	
	
	
	
}
void RestaMatriz(int matriz_A[][NCOL], int matriz[][NCOL])
{
		int i, j;
		int matrizres[NLIN][NCOL];
	printf("\nLa resta de las matrices es:\n");
	printf("\n");
	for(i = 0 ; NCOL > i; i++)
	{
		printf("| ");
		for(j = 0; NCOL > j; j++)
		{
			matrizres[i][j] = matriz_A[i][j] - matriz[i][j];
			printf("  %d  ",matrizres[i][j]);
			
		
			
			
			
		}
		printf(" |");
		printf("\n");
	} 
	
	
	
	
}

void MostrarMatriz(int Matriz[][NCOL])
{
	int i,j;
	
	printf("\n");
	for(i = 0 ; NCOL > i; i++)
	{
		printf("| ");
		for(j = 0; NCOL > j; j++)
		{
			printf("  %d  ",Matriz[i][j]);
			
		
			
			
			
		}
		printf(" |");
		printf("\n");
	} 
	
	
	
	
}
int main()
{
	int matriz_A[3][3] = 
	{
		{1,20,3},		
		{4,5,60},
		{70,8,9}
	};
	
	int matriz[NLIN][NCOL];
	
	
	
	RellenarMatriz(matriz);
	
	MostrarMatriz(matriz);
	MostrarMatriz(matriz_A);
	SumaMatriz(matriz_A,matriz);
	RestaMatriz(matriz_A,matriz);
	
	
	
}
