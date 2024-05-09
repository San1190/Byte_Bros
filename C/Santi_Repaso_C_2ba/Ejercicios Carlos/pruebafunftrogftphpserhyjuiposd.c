

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define PI 3.141592

#define RESET_COLOR    "\x1b[0m"
#define NEGRO_T        "\x1b[30m"
#define ROJO_T     "\x1b[31m"
#define VERDE_T        "\x1b[32m"
#define AZUL_T     "\x1b[34m"
#define MAGENTA_T  "\x1b[35m"
#define CYAN_T     "\x1b[36m"
#define AMARILLO_T "\x1b[33m"


int MostrarMenu();
float CalcularLongCir(float radio);
int CalcularResta(int a, int b);
int potencia(int base, int expo);
int Ball();
void SelecOption(int num);


int main()
{
	int num;
	num = MostrarMenu();
	
	
	

	
	SelecOption(num);

	
	return 0;
}


int MostrarMenu()
{
	int num;
	
	printf(AZUL_T"-----------------------------\n");
	printf("------------Menú-------------\n");
	printf("-----------------------------\n");
	printf("Seleccine un número: \n");
	printf("1 = Calculo de longitud de una circunferencia\n");
	printf("2 = Resta entre dos números\n");
	printf("3 = Potencia de un número\n");
	printf("4 = Preguntar al bot sabio lo que opine de tu pregunta\n");
	printf("0 = Salir\n");
	printf("Que quiere seleccionar: ");
	scanf("%d",&num);
	
	
	
	
	return (num);
		
		
	
	
	
}



float CalcularLongCir(float radio)
{
	double op;	

	op = 2*radio*PI;
	
	return(op);
	
}

int CalcularResta(int a, int b)
{
	
	int c;
	
	c = a-b;
	
	
	return(c);
			
}
int potencia(int base, int expo)
{
	int sol,i;
	sol = 1;
	for(i = 1;i <= expo; i++)
	{
		sol*=base;
		
		
	}
	
	return(sol);
	
	
	
}

int Ball()
{
    const char *string_table[] = 
    { 
        "Es cierto.",
        "Es decididamente así.",
        "Sin duda.",
        "Sí definitivamente.",
        "Puedes confiar en ello.",
        "Como yo lo veo, sí.",
        "Es lo mas probable.",
        "Las perspectivas son buena.",
        "Si.",
        "Las señales apuntan a que sí.",
        "Respuesta confusa, intentalo otra vez.",
        "Pregunta de nuevo más tarde.",
        "Mejor no decirtelo ahora.",
        "No puedo  predecirlo ahora.",
        "Concéntrate y pregunta otra vez.",
        "No cuentes con eso",
        "Mi respuesta es no.",
        "Mis fuentes dicen que no.",
        "No es tan bueno",
        "Es muy dudoso."
        
    };
    int table_size = 19; 

    srand(time(NULL)); 

    for (int i = 1; i <= 1; ++i)
    {
        const char *rand_string = string_table[rand() % table_size];
        printf("%2d. %s\n", i,  rand_string);
    }

    return 0;
}

void SelecOption(int num)
{	
	if (num == 1)
	{
		float radio;
		
		printf(VERDE_T "\nIntroduce el radio de la circunferencia(cm): ");
		scanf("%f", &radio);
		printf("Resultado: la longitud de la circunferencia es %.3lfcm", CalcularLongCir(radio));
		
	}
	if(num == 2)
	{
		int minuendo,sustraendo;
		
		printf( ROJO_T  "\nColoca un número: ");
		scanf("%d",&minuendo);
		printf( ROJO_T  "Coloca otro número: ");
		scanf("%d",&sustraendo);
		
		printf("La resta de %d y %d es: %d",minuendo,sustraendo,CalcularResta(minuendo,sustraendo));
	
	}
	if(num == 3)
	{
		int base , expo;
	
		printf( MAGENTA_T "\nEscriba una base: ");
		scanf("%d",&base);
		printf("Escriba un exponente: ");
		scanf("%d",&expo);
		 potencia(base,expo);
		printf("La solción es %d", potencia(base,expo));
			
	}
	if(num == 4)
	{
		char preg;
		printf(CYAN_T"\nEscriba su pregunta:");
		scanf("%s",&preg);
		
		Ball();
		
		
		
	}
	
}

