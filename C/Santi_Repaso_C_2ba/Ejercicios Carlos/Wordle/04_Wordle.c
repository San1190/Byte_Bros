#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h> // getpid
#include <time.h> // time
#include "04_libwordle.h"

void MostrarMensaje(int id)
{
	if (id == 1)
	{
		printf("(1) - Valenciano\n");
		printf("(2) - Espanol\n");
		printf("(3) - English\n");
		printf("Seleccione el idioma (1 - 3): ");
	}
	else if (id == 2)
	{
		printf("Introduce palabra: ");
	}
	else if (id == 3)
	{
		printf("¡ENHORABUENA! Ha resuelto el Wordle de hoy\n");
	}
	else if (id == 4)
	{
		printf("GAME OVER");
	}
}

void MostrarError(int id)
{
	if (id == 1)
	{
		printf("ERROR: número no válido\n");
	}
	else if (id == 2)
	{
		printf("ERROR: tamaño de palabra no válido\n");
	}
}

void InicializarWordleACero (char matriz[][NCOL])
{
		int i,j;


	for(i = 0 ; NCOL > i; i++)
	{
		
		for(j = 0; NFIL > j; j++)
		{
			matriz[i][j] = ' ';
		
		}
	} 

}

void InicializarMatrizACero (int matriz[][NCOL])
{
	int i,j;


	for(i = 0 ; NCOL > i; i++)
	{
		
		for(j = 0; NFIL > j; j++)
		{
			matriz[i][j] = 0;
		
		}
	} 
	
}

int SeleccionarIdioma()
{
	int idioma = 1;
	MostrarMensaje(1);
	scanf("%d",&idioma);
	
	while((idioma>3) || (idioma<1))
	{
		MostrarError(1);
		printf("\n");
		MostrarMensaje(1);
		scanf("%d",&idioma);
	 }

	return(idioma); //devolverá 1 para valenciano, 2 para español o 3 para inglés)
}

void MostrarWordle (char matrizWordle[][NCOL], int matrizEstado[][NCOL])
{
	int i,j;
	
	system("clear");
	
	
	printf("\n");
	for(i = 0; NFIL > i; i++)
	{
		printf("|");
		
		for(j = 0; NCOL-1 > j; j++)
		{
			printf("¯¯");
			if(matrizEstado[i][j] == 0)
			{
				
				printf(" %c "COLOR_RESET,matrizWordle[i][j]);
				
			}
			else if (matrizEstado[i][j] == 1)
			{
				
				
				printf(YELLOW" %c "COLOR_RESET,matrizWordle[i][j]);
				
				
			}
			else if (matrizEstado[i][j] == 2)
			{
				printf(GREEN" %c "COLOR_RESET,matrizWordle[i][j]);
				
				
			}
			printf("¯¯");
			printf("|");
		}
	
		printf("\n");
	} 
	
	

}

int ComprobarPalabra(char matrizWordle[][NCOL], int matrizEstado [][NCOL], char solucion[], int numIntento)
{
	int i,j,x;
	
	for(i = 0; i< NCOL;i++)
	{
		//for(j = 0; j < NFIL; j++)
		//{
			if(matrizWordle[numIntento][i] == solucion[i])
			{
				matrizEstado[numIntento][i] = 2;
			}
			else
			{
				for(x = 0; x <=4; x++)
				{
					if(matrizWordle[numIntento][x] == solucion[numIntento] && matrizEstado[numIntento][x] == 0)
					{
						matrizEstado[numIntento][x] = 1;
					
					}
					else
					{
						matrizEstado[numIntento][x] = 0;
					
					}
					
				}
			}
			
		//}
	}
		
		
		//if(strcmp(mattrizWordle[numIntento-1],solucion) == 0
		
			
			
			
	
	/*
	for(i = 0; i<NCOL; i++)
	{
		if(matrizWordle[numIntento][i] == solucion[i])
			{
				matrizEstado[numIntento][i] = 2;
			}
		else
		{
			for(j = 0; j < 4; j++)
			{
				if(matrizWordle[numIntento][j] == solucion[i])
				{
						matrizEstado[numIntento][j] = 1;
					
				}
				else
				{
						matrizEstado[numIntento][j] = 0;
					
				}
				
			}
			
			
		}
		
		
		*/
		
		
		
	
	
	
	
	int ganar = 0;
	
	//ganar = strcpy(solución,"REINO");
	
	
	return (ganar);	//la función devolverá un 1 si el usuario ha adivinado la palabra y 0 en caso contrario}
}

void EscogerSolucion(char solucion[], int idioma)
{
	char nombreArchivo[13];
	int numLinea=0;
	int lineaAleatoria;
	int lineasArchivo;	//contiene el número de líneas del fichero texto (ver constante)
	
	FILE *F;
	
	if (idioma == 1)
	{
		strcpy(nombreArchivo, "wordl_VA.txt");
		lineasArchivo = NUM_LINEAS_VA;
	}
	else if (idioma == 2)
	{
		strcpy(nombreArchivo, "wordl_ES.txt");
		lineasArchivo = NUM_LINEAS_ES;
	}
	else if (idioma == 3)
	{
		strcpy(nombreArchivo, "wordl_EN.txt");
		lineasArchivo = NUM_LINEAS_EN;
	}
	
	F = fopen(nombreArchivo, "r");
	
	if (!F) 
	{
        exit(EXIT_FAILURE);
    }
    
    srand(getpid());
	//srand(time(NULL));
	lineaAleatoria = rand() % lineasArchivo + 1;
    
    
    while (numLinea<lineaAleatoria && fscanf(F, "%[^\n ] ", solucion) != EOF) 
    {
		numLinea++;
    }

    fclose(F);

	strcpy(solucion, "salon");
} 

void Iniciar (char matrizWordle[][NCOL], int matrizEstado [][NCOL], int idioma)
{
	char palabra[6],solucion[6];
	 int i,x,j;

		 
	EscogerSolucion(solucion,idioma);
	

	
	
	for(i = 0; i <=NCOL; i++)
	{
		 
	
		MostrarMensaje(2);
		scanf("%s",palabra);
		x = strlen(palabra);
		
		
		while( x > 5)
		{
			MostrarError(2);
			MostrarMensaje(2);
			scanf("%s",palabra);
			x = strlen(palabra);
		}
		
		for(j = 0; j<NCOL; j++)
		{
			matrizWordle[i][j] = palabra[j];
			
			ComprobarPalabra(matrizWordle,matrizEstado,solucion, i);
		}
		
		MostrarWordle(matrizWordle, matrizEstado);
	}
	
	
	
	
	

}

int main(int argc, char **argv)
{
	char matrizWordle[NFIL][NCOL];
	int matrizEstado [NFIL][NCOL];
	int idioma;
	
	InicializarWordleACero(matrizWordle);
	InicializarMatrizACero(matrizEstado);
	
	idioma = SeleccionarIdioma();
	
	Iniciar (matrizWordle, matrizEstado, idioma);
	
	return 0;
}

