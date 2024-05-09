// Incluimos las librerias necesarias
#include <iostream> // Para la entrada y salida de datos
#include  <vector> // Para usar vectores (arrays)
#include <tuple> // Para usar tuplas
#include <string> // Para usar strings, aunque al usar namespace std no es necesario
#include <sstream> // Para operaciones de entrada y salida en cadenas de texto
#include <iomanip> // Para manipular la salida de datos
#include <cstring> // Para trabajar con cadenas de caracteres estilo C

// Librerias de funciones
#include <algorithm> // Para usar funciones de la libreria algorithm
#include <typeinfo> // Para usar la función type
#include <cmath> // Para funciones matemáticas
#include <chrono> // Para mediciones de tiempo
#include <random> // Para generación de números aleatorios
#include <bitset> // Para trabajar con bits


/*
Funciones interesantes de cada libreria, no pongo todas con ejemplos porque sería muy largo
    Biblioteca <cmath>:
        pow(base, exponente): Calcula la potencia de un número.
        log(x): Calcula el logaritmo natural de un número.
        log10(x): Calcula el logaritmo en base 10 de un número.
        exp(x): Calcula la función exponencial de un número.
        ceil(x): Redondea hacia arriba un número decimal.
        floor(x): Redondea hacia abajo un número decimal.
        round(x): Redondea un número decimal al entero más cercano.

    Biblioteca <chrono>:
        chrono::system_clock::now(): Obtiene el tiempo actual del sistema.
        chrono::steady_clock::now(): Obtiene el tiempo actual de un reloj estable. (no se ajusta por cambios de tiempo)
        chrono::duration_cast<tipo>(duracion): Convierte la duración de un período de tiempo a otro tipo de duración. Por ejemplo, chrono::seconds,
        chrono::milliseconds, chrono::microseconds, chrono::nanoseconds, etc.: Tipos de duración específicos. Por ejemplo, chrono::seconds(5) representa 5 segundos.

    Biblioteca <random>:
        random_device: Genera un número aleatorio utilizando el generador de números aleatorios del sistema.
        mt19937, mt19937_64: Generadores de números aleatorios basados en el algoritmo Mersenne Twister.
        uniform_int_distribution<int>, uniform_real_distribution<double>: Distribuciones uniformes para números enteros y reales, respectivamente.
        normal_distribution<double>: Distribución normal para números reales.
        shuffle(inicio, fin, generador): Mezcla los elementos en el rango especificado utilizando el generador de números aleatorios.

    Biblioteca <iomanip>:
        setw(ancho): Establece el ancho del campo de salida.
        setprecision(precision): Establece la precisión de salida para números de punto flotante.
        fixed, scientific: Especificadores de formato para mostrar números de punto flotante en notación fija o científica.

    Biblioteca <string>:
        toupper(c): Convierte un carácter a mayúscula.
        tolower(c): Convierte un carácter a minúscula.
        find(subcadena): Encuentra la primera ocurrencia de una subcadena dentro de otra cadena.
        replace(pos, longitud, nueva_subcadena): Reemplaza una porción de la cadena con otra subcadena.
        substr(pos, longitud): Extrae una porción de la cadena.
        getline(istream, cadena): Lee una línea completa desde la entrada estándar.

    Biblioteca <algorithm> (ya incluida pero con más funciones):
        min(a, b), max(a, b): Devuelve el mínimo o máximo entre dos valores.
        accumulate(inicio, fin, valor_inicial): Suma todos los elementos en el rango especificado.
        count(inicio, fin, valor): Cuenta las ocurrencias de un valor en el rango especificado.
        find(inicio, fin, valor): Busca la primera ocurrencia de un valor en el rango especificado.
        reverse(inicio, fin): Invierte el orden de los elementos en el rango especificado.

    Biblioteca <cstring>:
        strcpy(destino, origen): Copia una cadena de caracteres en otra.
        strcat(destino, origen): Concatena una cadena de caracteres al final de otra.
        strlen(cadena): Obtiene la longitud de una cadena de caracteres.
        strcmp(cadena1, cadena2): Compara dos cadenas de caracteres.
        strchr(cadena, caracter): Busca la primera ocurrencia de un carácter en una cadena.
        strstr(cadena, subcadena): Busca la primera ocurrencia de una subcadena en una cadena.
        memset(destino, valor, longitud): Establece un valor en un bloque de memoria.
        memcpy(destino, origen, longitud): Copia un bloque de memoria en otro.
        memmove(destino, origen, longitud): Copia un bloque de memoria en otro, incluso si se superponen.
        
*/

// Le decimos a c++ que vamos a usar la entrada y salida de datos estandar (terminal)
using namespace std; // Para no tener que escribir std::cout o std::cin, entre otras clases y metodos

// Predeclaramos las funciones declaradas despues del main
void funcion();
tuple<int, int> funcion2(int a, int b);
vector<string> split(string cadena, char separador);
string strip(string cadena);
void ejemplos_binario();
void iteraccion_memoria();



// Funcion principal, se ejecuta al iniciar el programa
int main() { // Si no hubiesemos usado using namespace std, seria std::int main()

    // Declaramos las variables
    int numero1, numero2, resultado; // Enteros
    vector<int> numeros = {1, 2, 3, 4, 5}; // Arrays
    tuple<int, string, double> tupla = {1, "Hola", 3.14}; // Tuplas
    // Pedimos al usuario que introduzca los numeros
    cout << "Introduce el primer numero: ";
    std::cin >> numero1;
    std::cout << "Introduce el segundo numero: ";
    std::cin >> numero2;
    // Realizamos la suma
    resultado = numero1 + numero2;
    // Mostramos el resultado
    std::cout << "El resultado de la suma es: " << resultado << std::endl;

    // Llamamos a la función
    funcion();

    // Llamamos a la función 2
    auto [a, b] = funcion2(1, 2); // auto es para que c++ infiera el tipo de dato
    cout << a << " " << b << endl; // Mostramos los valores de la tupla


    // Bucle for
    for (int i = 0; i < 5; i++) {
        cout << numeros[i] << " ";
    }

    // Bucle while
    int i = 0;
    while (i < 5) {
        cout << numeros[i] << " ";
        i++;
    }

    // Bucle do while
    i = 0;
    do {
        cout << numeros[i] << " ";
        i++;
    } while (i < 5);

    // Bucle for each, como en Java
    for (int numero : numeros) {
        cout << numero << " ";
    }

    // Bucle for each con iteradores, usa la clase iterator para declarar el iterador it y recorrer el vector
    for (vector<int>::iterator it = numeros.begin(); it != numeros.end(); it++) { // .begin() y .end() son metodos de la clase vector
        cout << *it << " ";
    }

    // Bucle for each con auto, c++ infiere el tipo de dato
    for (auto numero : numeros) {
        cout << numero << " " << endl;
    }

    /*
    Ahora empieza la chicha :)
    Punteros
    Los punteros son variables que almacenan direcciones de memoria
    En c++ se declaran con el tipo de dato seguido de un asterisco
    */
    int *puntero; // Declaramos un puntero
    int variable = 5; // Declaramos una variable
    puntero = &variable; // Asignamos la dirección de memoria de la variable al puntero
    cout << "El valor de la variable es: " << variable << ", la dirección de memoria es: " << puntero << endl; // Mostramos el valor de la variable

    // Ahora vamos a modificar el valor de la variable a través del puntero
    *puntero = 10; // Modificamos el valor de la variable a través del puntero
    cout << "El valor de la variable es: " << variable << ", la dirección de memoria es: " << puntero << endl; // Mostramos el valor de la variable

    // Ahora vamos a crear un puntero a un array
    int *punteroArray; // Declaramos un puntero
    int array[5] = {1, 2, 3, 4, 5}; // Declaramos un array
    punteroArray = array; // Asignamos la dirección de memoria del array al puntero

    // Mostramos los valores del array a través del puntero
    for (int i = 0; i < 5; i++) {
        cout << *(punteroArray + i) << " " << endl; // *(puntero + i) es lo mismo que puntero[i], como en ensamblador, Direccion base + desplazamiento
    }

    // Ahora vamos a crear un puntero a un array de dos dimensiones
    int (*punteroArray2D)[3]; // Declaramos un puntero
    int array2D[2][3] = {{1, 2, 3}, {4, 5, 6}}; // Declaramos un array de dos dimensiones
    punteroArray2D = array2D; // Asignamos la dirección de memoria del array al puntero

    // Mostramos los valores del array a través del puntero
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < 3; j++) {
            cout << *(*(punteroArray2D + i) + j) << " " << endl; // *(*(punteroArray2D + i) + j) es lo mismo que puntero[i][j]
        }
        cout << endl;
    }

    // Funciones lambda 
    auto suma = [](int a, int b) -> int { return a + b; }; // Declaramos una función lambda que suma dos números que entran como parámetros
    cout << suma(1, 2) << endl; // Mostramos el resultado de la función lambda

    // Funciones lambda con captura
    int x = 5; // x es una variable que vamos a capturar (capturar es pasar una variable a la función lambda sin pasarla como parámetro)
    auto suma2 = [x](int a, int b) -> int { return a + b + x; }; // Declaramos una función lambda que suma dos números y una variable que entra como parámetro
    cout << suma2(1, 2) << endl; // Mostramos el resultado de la función lambda

    // Ahora vamos a crear una función lambda que recibe otra función como parámetro
    auto ejecutar = [](auto funcion) { funcion(); }; // Declaramos una función lambda que recibe otra función como parámetro
    ejecutar(funcion); // Llamamos a la función lambda y le pasamos la función funcion, mostrara "Hola mundo"

    // Ahora vamos a pasar a funciones interesantes a conocer
    // Funciones de la libreria algorithm
    vector<int> numeros2 = {5, 4, 3, 2, 1}; // Declaramos un vector
    cout << "El vector sin ordenar es: ";
    for (int numero : numeros2) {
        cout << numero << " "; // Mostramos el vector sin ordenar
    }
    sort(numeros2.begin(), numeros2.end()); // Ordenamos el vector, parametros: principio y final del vector
    cout << "El vector ordenado es: ";
    for (int numero : numeros2) {
        cout << numero << " "; // Mostramos el vector ordenado
    }

    // Mas funciones de la libreria algorithm
    vector<int> numeros3 = {1, 2, 3, 4, 5}; // Declaramos un vector
    cout << "El vector sin invertir es: ";
    for (int numero : numeros3) {
        cout << numero << " "; // Mostramos el vector sin ordenar
    }
    reverse(numeros3.begin(), numeros3.end()); // Invertimos el vector, parametros: principio y final del vector
    cout << "El vector invertido es: ";
    for (int numero : numeros3) {
        cout << numero << " "; // Mostramos el vector ordenado
    }

    // Funciones de la libreria algorithm con vectores de tuplas
    vector<tuple<int, string, double>> tuplas = {{1, "Hola", 3.14}, {2, "Adios", 6.28}}; // Declaramos un vector de tuplas
    cout << "El vector de tuplas sin ordenar es: ";
    for (tuple<int, string, double> tupla : tuplas) {
        cout << get<0>(tupla) << " " << get<1>(tupla) << " " << get<2>(tupla) << " "; // Mostramos el vector de tuplas sin ordenar usando get<posicion>(tupla)
    }
    sort(tuplas.begin(), tuplas.end()); // Ordenamos el vector de tuplas, parametros: principio y final del vector
    cout << "El vector de tuplas ordenado es: ";
    for (tuple<int, string, double> tupla : tuplas) {
        cout << get<0>(tupla) << " " << get<1>(tupla) << " " << get<2>(tupla) << " "; // Mostramos el vector de tuplas ordenado usando get<posicion>(tupla)
    }
    
    // Otra función interesante es type, que nos devuelve el tipo de dato de una variable
    cout << "El tipo de dato de la variable es: " << typeid(variable).name() << endl; // Mostramos el tipo de dato de la variable

    // Otra función interesante es sizeof, que nos devuelve el tamaño en bytes de una variable
    cout << "El tamaño en bytes de la variable es: " << sizeof(variable) << endl; // Mostramos el tamaño en bytes de la variable

    // Bucle for each con auto y manipulación de cadenas
    for (auto numero : numeros) {
        cout << to_string(numero) << " "; // Convertir int a string, de la libreria string
    }

    string cadena = "12345";
    int numero = stoi(cadena) + 5; // Convertir string a int, de la libreria string
    cout << "numero pasado a int: " << numero << endl;

    // Bucle for each con auto y manipulación de la salida
    for (auto numero : numeros) {
        cout << setw(5) << numero << " "; // Establecer el ancho de los espacios, de la libreria iomanip
    }

    // Bucle for each con auto y manipulación de la salida de punto flotante
    double pi = 3.14159;
    cout << setprecision(3) << pi << endl; // Establecer la precisión de salida, de la libreria iomanip

    // Operaciones de cadena
    string texto = "Hola mundo";
    cout << "Longitud de la cadena: " << texto.length() << endl; // Obtener la longitud de la cadena
    cout << "Cadena invertida: ";   
    reverse(texto.begin(), texto.end()); // Invertir la cadena
    cout << texto << endl;


    // Funciones matemáticas
    cout << "Raíz cuadrada de 25: " << sqrt(25) << endl; // Raíz cuadrada
    cout << "Valor absoluto de -10: " << abs(-10) << endl; // Valor absoluto
    cout << "Sen(45°): " << sin(45) << endl; // Seno (en radianes)

    // Mediciones de tiempo
    auto start = chrono::high_resolution_clock::now(); // Tiempo de inicio
    // Código cuya ejecución queremos medir
    auto end = chrono::high_resolution_clock::now(); // Tiempo de finalización
    chrono::duration<double> duration = end - start; // Duración de la ejecución en segundos
    cout << "Tiempo transcurrido: " << duration.count() << " segundos" << endl;

    // Generación de números aleatorios
    random_device rd; // Dispositivo aleatorio
    mt19937 gen(rd()); // Generador de números aleatorios
    uniform_int_distribution<> dis(1, 100); // Distribución uniforme entre 1 y 100    
    cout << "Número aleatorio entre 1 y 100: " << dis(gen) << endl;

    vector<int> numerosAleatorios;
    for (int i = 0; i < 10; i++) {
        numerosAleatorios.push_back(dis(gen)); // Generar un número aleatorio y agregarlo al vector
    }
    cout << "Números aleatorios entre 1 y 100: ";
    for (int numero : numerosAleatorios) {
        cout << numero << " ";
    }
    cout << endl;
    // Aleatoriezamos el vector
    shuffle(numerosAleatorios.begin(), numerosAleatorios.end(), gen); // Mezclar los elementos del vector
    
    cout << "Números aleatorios mezclados: ";
    for (int numero : numerosAleatorios) {
        cout << numero << " ";
    }
    sort(numerosAleatorios.begin(), numerosAleatorios.end()); // Ordenar los elementos del vector
    cout << "Números aleatorios ordenados: ";
    for (int numero : numerosAleatorios) {
        cout << numero << " ";
    }


    // Probamos strip y split
    string cadena2 = "  Hola mundo  ";
    cout << "Cadena sin espacios en blanco: " << strip(cadena2) << endl; // Eliminar espacios en blanco
    string cadena3 = "Hola,mundo,desde,C++";
    cout << "Cadena original: " << cadena3 << endl;
    vector<string> subcadenas = split(cadena3, ','); // Dividir la cadena en subcadenas
    cout << "Subcadenas: ";
    cout << "{";
    for (string subcadena : subcadenas) {
        cout << subcadena << ", ";
    }
    cout << "}" << endl;


    // Ejemplos de operaciones binarias, descomenta para probar
    // ejemplos_binario();

    // Retornamos 0 al finalizar el programa
    return 0;
}


// Declaramos una nueva función
void funcion() {
    std::cout << "Hola mundo" << std::endl;
}

tuple<int, int> funcion2(int a, int b) {
    return {a, b};
}

// Función para dividir una cadena en subcadenas usando un separador
vector<string> split(string cadena, char separador) {
    vector<string> resultado; // Vector que almacenará las subcadenas resultantes
    stringstream ss(cadena); // stringstream es una clase que se utiliza para operaciones de entrada y salida en cadenas de texto, ss es un objeto de esta clase
    string elemento; // Variable para almacenar cada subcadena individualmente
    while (getline(ss, elemento, separador)) { // getline lee una línea completa desde la entrada estándar y la divide en subcadenas usando el separador especificado
        resultado.push_back(elemento); // Agrega la subcadena al vector de resultados
    }
    return resultado; // Devuelve el vector de subcadenas resultantes
}

// Elimina los espacios en blanco al principio y al final de una cadena
string strip(string cadena) {
    size_t inicio = cadena.find_first_not_of(" \t\n"); // size_t es un tipo de dato que se usa para almacenar tamaños de objetos y esquinas de matrices
    size_t fin = cadena.find_last_not_of(" \t\n"); // find_first_not_of y find_last_not_of buscan el primer y último carácter que no sea un espacio, tabulador o salto de línea
    return cadena.substr(inicio, fin - inicio + 1); // substr extrae una subcadena de la cadena original, como String.substring() en Java
}

void ejemplos_binario() {
    int a = 5; // 101
    int b = 3; // 011
    
    int resultado_and = a & b; // 001 (1)
    int resultado_or = a | b;  // 111 (7)
    int resultado_xor = a ^ b; // 110 (6)
    int resultado_not = ~a;    // 11111111111111111111111111111010 (bits restantes dependen del tamaño de int)
    int resultado_left_shift = a << 1; // 1010 (10)
    int resultado_right_shift = a >> 1; // 10 (2)

    // Hexadecimal
    int hexadecimal = 0x1A; // 26 en decimal
    int numero_hexadecimal = 0x1F; // 31 en decimal
    unsigned int numero_unsigned_hexadecimal = 0xFFFF; // 65535 en decimal

    // Octal
    int octal = 012; // 10 en decimal
    int numero_octal = 077; // 63 en decimal

    cout << resultado_and << endl;
    cout << resultado_or << endl;

    cout << "Hexadecimal: " << hexadecimal << endl;
    cout << "Número hexadecimal: " << numero_hexadecimal << endl;
    cout << "Número hexadecimal sin signo: " << numero_unsigned_hexadecimal << endl;

    cout << "Octal: " << octal << endl;
    cout << "Número octal: " << numero_octal << endl;

    // Cargamos una direccion de memoria en un puntero
    int *puntero = (int*)malloc(sizeof(int)); // Reservamos memoria para un entero

    // Cambiamos el valor de la variable a través del puntero
    *puntero = 0x08; // El tercer bit de la variable se establece en 1, 00001000 en binario

    cout << "Valor de la variable: " << *puntero << endl;
    cout << "Valor de la variable en binario: " << bitset<8>(*puntero) << endl; // Mostramos el valor de la variable en binario
    cout << "Dirección de memoria de la variable: " << puntero << endl;



}

void iteraccion_memoria() {
    // Asignar memoria dinámicamente para una lita de enteros
    int *arreglo = (int*)malloc(5 * sizeof(int));
    
    // Asignar memoria dinámicamente para una lista de enteros inicializado en 0
    int *arreglo_cero = (int*)calloc(5, sizeof(int));
    
    // Reasignar memoria dinámicamente para el arreglo de enteros
    arreglo = (int*)realloc(arreglo, 10 * sizeof(int));
    
    // Liberar la memoria asignada dinámicamente
    free(arreglo);
    free(arreglo_cero);
}