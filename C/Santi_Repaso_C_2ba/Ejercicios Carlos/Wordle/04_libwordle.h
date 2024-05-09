#define NFIL 6
#define NCOL 6
#define NUM_LINEAS_ES 1232
#define NUM_LINEAS_EN 1232
#define NUM_LINEAS_VA 1232
#define ARCHIVO_VA "wordl_VA.txt"
#define ARCHIVO_ES "wordl_ES.txt"
#define ARCHIVO_EN "wordl_EN.txt"

#define GREEN   	"\x1b[42m"
#define GREEN_L   	"\x1b[32m"
#define YELLOW  	"\x1b[43m"
#define YELLOW_L  	"\x1b[33m"
#define COLOR_RESET	"\x1b[0m"


void MostrarMensaje(int); //muestra el mensaje correspondiente según su id
void MostrarError(int); //muestra el error correspondiente según su id
void InicializarWordleACero (char [][NCOL]); //rellena toda la matriz con un espacio en blanco
void InicializarMatrizACero (int [][NCOL]); //rellena toda la matriz de ceros
int SeleccionarIdioma(); //pregunta al usuario en qué idioma quiere jugar (1: valenciano | 2: castellano | 3: inglés) 
void EscogerPalabra(char [], int); //escoge una palabra de manera aleatoria del idioma escogido para que el usuario intente adivinarla
void MostrarWordle (char [][NCOL], int [][NCOL]); //muestra por pantalla la matriz con las palabras introducidas y colorea cada letra según su matriz de estado
int ComprobarPalabra(char [][NCOL], int [][NCOL], char [], int); //comprueba cada una de las letras de la palabra introducida con la solución y rellena la matriz de estado asociada 
void Iniciar (char [][NCOL], int [][NCOL], int); //inicia el juego a partir de la matriz de palabras, la matriz de estado asociada y el idioma (1, 2 o 3)
