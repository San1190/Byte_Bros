#include<stdio.h>
//Voy a explicar todo c desde lo más básico hasta lo más avanzado

//Comentario de una línea

/*
Comentario de varias líneas
*/

//Definición de constantes
#define PI 3.14159
#define NOMBRE "Juan"

//Definición de variables globales
int x = 5;
int y = 10;

//Definición de funciones
void funcion1(int a, int b){
    printf("La suma de %d y %d es %d\n", a, b, a+b);
}

int funcion2(int a, int b){
    return a+b;
}

int main(){
    //Definición de variables locales
    int a = 5;
    int b = 10;
    int c;

    //Llamada a funciones
    funcion1(a, b);
    c = funcion2(a, b);
    printf("La suma de %d y %d es %d\n", a, b, c);

    //Estructuras de control
    if(a > b){
        printf("a es mayor que b\n");
    }else if(a < b){
        printf("a es menor que b\n");
    }else{
        printf("a es igual a b\n");
    }

    switch(a){
        case 1:
            printf("a es 1\n");
            break;
        case 2:
            printf("a es 2\n");
            break;
        default:
            printf("a no es ni 1 ni 2\n");
    }

    for(int i = 0; i < 10; i++){
        printf("i = %d\n", i);
    }

    while(a < 10){
        printf("a = %d\n", a);
        a++;
    }

    do{
        printf("a = %d\n", a);
        a++;
    }while(a < 10);

    //Operadores aritméticos
    printf("a + b = %d\n", a+b);
    printf("a - b = %d\n", a-b);
    printf("a * b = %d\n", a*b);
    printf("a / b = %d\n", a/b);
    printf("a %% b = %d\n", a%b);

    //Operadores de asignación
    a += b;
    printf("a += b: a = %d\n", a);
    a -= b;
    printf("a -= b: a = %d\n", a);
    a *= b;
    printf("a *= b: a = %d\n", a);
    a /= b;
    printf("a /= b: a = %d\n", a);
    a %= b;
    printf("a %%= b: a = %d\n", a);

    //Operadores de comparación
    if(a == b){
        printf("a es igual a b\n");
    }
    if(a != b){
        printf("a es distinto de b\n");
    }
    if(a > b){
        printf("a es mayor que b\n");
    }
    if(a < b){
        printf("a es menor que b\n");
    }
    if(a >= b){
        printf("a es mayor o igual que b\n");
    }
    if(a <= b){
        printf("a es menor o igual que b\n");
    }

    //Operadores lógicos
    if(a > b && a < 10){
        printf("a es mayor que b y menor que 10\n");
    }
    if(a > b || a < 10){
        printf("a es mayor que b o menor que 10\n");
    }
    if(!(a > b)){
        printf("a no es mayor que b\n");
    }

    //Operadores de bits
    printf("a & b = %d\n", a&b);
    printf("a | b = %d\n", a|b);
    printf("a ^ b = %d\n", a^b);
    printf("~a = %d\n", ~a);
    printf("a << 1 = %d\n", a<<1);
    printf("a >> 1 = %d\n", a>>1);

    //Operadores de tamaño
    printf("sizeof(int) = %d\n", sizeof(int));
    printf("sizeof(float) = %d\n", sizeof(float));
    printf("sizeof(double) = %d\n", sizeof(double));
    printf("sizeof(char) = %d\n", sizeof(char));

    //Operadores de dirección
    printf("Dirección de a: %p\n", &a);

    //Operadores de indirección
    int *p = &a;
    printf("Valor de a: %d\n", a);
    printf("Valor de a a través de p: %d\n", *p);

    //Operadores de estructura
    struct Punto{
        int x;
        int y;
    };
    struct Punto punto;
    punto.x = 5;
    punto.y = 10;
    printf("Punto: (%d, %d)\n", punto.x, punto.y);

    //Operadores de unión
    union Numero{
        int entero;
        float flotante;
    };
    union Numero numero;
    numero.entero = 5;
    printf("Número entero: %d\n", numero.entero);
    numero.flotante = 5.5;

    //Operadores de enumeración
    enum Color{
        ROJO,
        VERDE,
        AZUL
    };
    enum Color color = ROJO;
    switch(color){
        case ROJO:
            printf("Color rojo\n");
            break;
        case VERDE:
            printf("Color verde\n");
            break;
        case AZUL:
            printf("Color azul\n");
            break;
    }

    //Operadores de puntero
    int *q = &a;
    printf("Valor de a: %d\n", a);
    printf("Valor de a a través de q: %d\n", *q);

    //Operadores de selección
    int z = a > b ? a : b;
    printf("El mayor entre a y b es %d\n", z);

    //Operadores de secuencia
    a = (b = 5, b+10);
    printf("a = %d\n", a);

    //Operadores de coma
    a = (b = 5, b+10);
    printf("a = %d\n", a);

    //Operadores de dirección de memoria
    printf("Dirección de a: %p\n", &a);
    
    //Operadores de indirección
    int *r = &a;
    printf("Valor de a: %d\n", a);
    printf("Valor de a a través de r: %d\n", *r);

    
    

    return 0;
}

//Compilación: gcc apuntes1.c -o apuntes1

//Ejecución: ./apuntes1

//Punteros a uniones
/*Un puntero a una unión apunta a la ubicación de memoria asignada a la unión.

Un puntero de unión se declara utilizando la palabra clave union y la etiqueta de unión junto con * y el nombre del puntero.

Por ejemplo, considera las siguientes declaraciones:*/

// Un puntero a una unión sirve para acceder a la unión. Una unión es una estructura de datos que puede almacenar diferentes tipos de datos en el mismo espacio de memoria. 
//Por lo tanto, un puntero a una unión puede apuntar a diferentes tipos de datos en la unión.

#include <stdio.h>
#include <string.h>

union val
{
    int int_num;
    float fl_num;
    char str[20];
};

int main()
{
    union val info;
    union val *ptr = NULL;
    ptr = &info;
    ptr->int_num = 10;
    printf("info.int_num is %d", info.int_num);

    return 0;
}

//Con parametros:
#include <stdio.h>
#include <string.h>

union id
{
    int id_num;
    char name[20];
};

void set_id(union id *item);
void show_id(union id item);

int main()
{
    union id item;

    set_id(&item);
    show_id(item);

    return 0;
}

void set_id(union id *item)
{
    item->id_num = 42;
}

void show_id(union id item)
{
    printf("ID is %d", item.id_num);
}

//Array de uniones
/*Un array de uniones es un conjunto de uniones que se almacenan en una secuencia contigua de memoria.
 
Un array de uniones se declara utilizando la palabra clave union y la etiqueta de unión junto con [] y el nombre del array.
*/
#include <stdio.h>

union val
{
    int int_num;
    float fl_num;
    char str[20];
};

int main()
{
    union val nums[10];
    int k;

    /* create an array of ints */
    for (k = 0; k < 10; k++)
    {
        nums[k].int_num = k;
    }

    /* display array values */
    for (k = 0; k < 10; k++)
    {
        printf("%d  ", nums[k].int_num);
    }

    return 0;
}

