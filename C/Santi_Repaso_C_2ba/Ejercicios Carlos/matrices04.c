#include <stdio.h>
#include "libmatrices04.h"
#define RESET_COLOR    "\x1b[0m"
#define ROJO_T     "\x1b[31m"
#define MAGENTA_T  "\x1b[35m"

void MostrarMenu()
{
	printf("\n----------------------------\n");
	printf("------------Menú-------------\n");
	printf("-----------------------------\n");
	
	printf("1. MOSTAR MATRICES\n");
	printf("2. RELLENARMATRIZ...\n");
	printf("3. MATRIZ IDENTIDAD...\n");
	printf("4. MATRIZ TRASPUESTA...\n");
	printf("5. SUMAR MATRICES (A + B)\n");
	printf("6. RESTAR MATRICES (A - B)\n");
	printf("7. MULTIPLICAR MATRICES (A * B)\n");
	printf("8. SALIR\n");
	
	
	
}

	
	

void RellenarMatriz(int matriz[][NCOL])
{
	int i, j;
	
	for(i = 0 ;i < NCOL; i++)
	{
		for(j = 0; j < NLIN; j++)
		{
			printf("Introduzca un número para la posición (%d,%d): ", i,j);
			scanf("%d",&matriz[i][j]);
				
		}		

	}
	printf("\n");
		
}

void MatrizTraspuesta(int matriz[][NCOL])
{
		int i,j;
		//int matTraspuesta[NLIN][NCOL];

	for(i = 0 ; NCOL > i; i++)
	{
		
		for(j = 0; NLIN > j; j++)
		{
			matriz[i][j] = matriz[j][i];
		
		}
	} 
	MostrarMatriz(matriz);

}

void InicializarMatrizACero(int matriz[][NCOL])
{
		int i,j;


	for(i = 0 ; NCOL > i; i++)
	{
		
		for(j = 0; NLIN > j; j++)
		{
			matriz[i][j] = 0;
		
		}
	} 
	

}

void CrearMatrizIdentidad(int matriz[][NCOL])
{
	int i, j;
	
	//int matrizid[NLIN][NCOL];
    InicializarMatrizACero(matriz);
	
	for(i = 0 ; NCOL > i; i++)
	{
		for(j = 0; NLIN > j; j++)
		{
			if (i == j)
			{
				matriz[i][j] = 1;
				
				
				
			}		
		}
	} 
	MostrarMatriz(matriz);
	
}

void SumaMatriz(int matriz_A[][NCOL], int matriz[][NCOL])
{
	int i, j;
	int matrizsum[NLIN][NCOL];
	
	for(i = 0 ; NCOL > i; i++)
	{
		for(j = 0; NLIN > j; j++)
		{
			matrizsum[i][j] = matriz_A[i][j] + matriz[i][j];		
		}
	} 
	
	MostrarMatriz(matrizsum);
	
}

void RestaMatriz(int matriz_A[][NCOL], int matriz[][NCOL])
{
	int i, j;
	int matrizres[NLIN][NCOL];
	
	for(i = 0 ; NCOL > i; i++)
	{
		for(j = 0; NLIN > j; j++)
		{
			matrizres[i][j] = matriz_A[i][j] - matriz[i][j];		
		}
	} 
	
	MostrarMatriz(matrizres);
	
}


void MostrarMatriz(int Matriz[][NCOL])
{
	int i,j;
	
	
	printf("\n");
	for(i = 0 ; NCOL > i; i++)
	{
		printf("|");
		for(j = 0; NLIN > j; j++)
		{
			if ((Matriz[i][j] >= 0) && (Matriz[i][j]<10))
			{
				printf("  %d  " ,Matriz[i][j]);	
			}
			else if ((Matriz[i][j] >= 10) && (Matriz[i][j]<100))
			{
				printf("  %d " ,Matriz[i][j]);	
				
				
			}
			else if ((Matriz[i][j] >= 100) && (Matriz[i][j]<1000))
			{
				printf(" %d " ,Matriz[i][j]);
			}
			else if ((Matriz[i][j] >= 1000) && (Matriz[i][j]<=10000))
			{
				printf("%d " ,Matriz[i][j]);
			}
			
			
		
			
		}
		printf("|");
		printf("\n");
	} 
	
}

void MultiplicarMatriz(int matriz_A[][NCOL] ,int matriz_B[][NCOL])
{
	int i , j, k,suma;
	int matrizmult[NLIN][NCOL];
	
	
	for(i = 0 ; NCOL > i; i++)
	{
		
		for(j = 0; NLIN > j; j++)
		{
			suma = 0;
			
			for(k =0; NCOL > k; k++)
			{
				
				suma += matriz_A[i][k] * matriz_B[k][j];
			}
			
			
			matrizmult[i][j] = suma ;
		
		}
	}
	MostrarMatriz(matrizmult);
	
	
	
}
void Iniciar(int matriz_A[][NCOL], int matriz_B[][NCOL])
{
	int num = 0;
	char letra;
	
	
	
	
	
	
	
	while ( num < 8)
	{
		
		MostrarMenu();
		Mensajes(1);
		scanf("%d",&num);
		
		
		while ((num < 1) || (num > 8))
		{
		
		Error(1);
		MostrarMenu();
		Mensajes(1);
		scanf("%d",&num);
			
		}
		
		if (num == 1)
		{
			Mensajes(2);
			MostrarMatriz(matriz_A);
			Mensajes(3);
			MostrarMatriz(matriz_B);
			
			
			
		}
		else if (num == 2)
		{
			
			Mensajes(4);
			scanf("%s",&letra);
			
			if ((letra == 'a' )|| (letra == 'A'))
			{
				Mensajes(2);
				RellenarMatriz(matriz_A);
				
				
				
			}
			else if ((letra == 'b') || (letra == 'B'))
			{
				Mensajes(3);
				RellenarMatriz(matriz_B);
				
			}
			else if ((letra == 't') || (letra == 'T'))
			{
				Mensajes(2);
				RellenarMatriz(matriz_A);
				
				Mensajes(3);
				RellenarMatriz(matriz_B);
				
			}
			else
			{
				Error(2);
					
			}
			
		}
		else if (num == 3)
		{
			
			Mensajes(5);
			scanf("%s",&letra);
			
			if ((letra == 'a' )|| (letra == 'A'))
			{
				Mensajes(2);
				
				CrearMatrizIdentidad(matriz_A);
				
				
				
			}
			else if ((letra == 'b') || (letra == 'B'))
			{
				Mensajes(3);
				CrearMatrizIdentidad(matriz_B);
				
			}
			else if ((letra == 't') || (letra == 'T'))
			{
				Mensajes(2);
				CrearMatrizIdentidad(matriz_A);
				
				Mensajes(3);
				CrearMatrizIdentidad(matriz_B);
				
			}
			else
			{
				Error(2);	
			}
			
			
			
			
			
		}
		else if (num == 4)
		{
			
			Mensajes(6);
			scanf("%s",&letra);
			
			if ((letra == 'a' )|| (letra == 'A'))
			{
				Mensajes(2);
				MatrizTraspuesta(matriz_A);
				
				
				
			}
			else if ((letra == 'b') || (letra == 'B'))
			{
				Mensajes(3);
				MatrizTraspuesta(matriz_B);
				
			}
			else if ((letra == 't') || (letra == 'T'))
			{
				Mensajes(2);
				MatrizTraspuesta(matriz_A);
				
				Mensajes(3);
				MatrizTraspuesta(matriz_B);
				
			}
			else
			{
				Error(2);	
			}
			
			
			
		}
		else if (num == 5)
		{
			Mensajes(7);
			SumaMatriz(matriz_A,matriz_B);

		}
		else if (num == 6)
		{
			Mensajes(8);
			RestaMatriz(matriz_A,matriz_B);
			
		}
		else if (num == 7)
		{
			Mensajes(9);
			MultiplicarMatriz(matriz_A,matriz_B);
		}
		else if(num == 8)
		{
			
			Mensajes(10);
			
		}
		
		/*MostrarMenu();
		Mensajes(1);
		scanf("%d",&num);*/	
	}


	 
}
void Mensajes(int num)
{
	if (num == 1)
	{
		printf("OPCIÓN:");
	}
	else if (num == 2)
	{
		printf("A=\n");
		
		
	}
	else if (num == 3)
	{
		
		printf("\nB=\n");
		
	}
	else if (num == 4)
	{
		
		printf("Seleccione que matriz desea rellenar(A o B o T (todas)):");
		
		
	}
	else if (num ==5)
	{
		printf("Seleccione que matriz desea hacer su identidad(A o B o T (todas)):");	
	}
	else if (num == 6)
	{
		
		printf("Seleccione que matriz desea hacer su traspuesta(A o B o T (todas)):");
		
		
	}
	else if (num == 7)
	{
		
		printf("A + B =\n");
		
		
	}
	else if (num == 8)
	{
		
		printf("A - B =\n");
		
		
	}
	else if (num == 9)
	{
		
		printf("A * B =\n");
		
		
	}
	else if (num == 10)
	{

		printf(MAGENTA_T"\nDesconectando del servidor..."RESET_COLOR);
		
	}
	
}
void Error(int num)
{
	if (num == 1)
	{
		printf(ROJO_T"\nERROR 1:\n" RESET_COLOR "La opción debe estar entre el 1 y el 8\n");
		
	}
	if (num == 2)
	{
		
		printf(ROJO_T"\nERROR 2:\n" RESET_COLOR "Debes introducir: 'a' , 'b' o 'todas'\n");
		
		
	}
}
int main()
{
	int matriz_A[NLIN][NCOL]; /*= { {1,20,3},
								{4,5,60},
								{70,8,9}}; */
	int matriz_B[NLIN][NCOL]; /*= { {9,8,7},
								{6,5,4},
								{3,2,1}};*/
	
	InicializarMatrizACero(matriz_A);
	InicializarMatrizACero(matriz_B);
	
	Iniciar(matriz_A,matriz_B);

	return 0;
	
}




