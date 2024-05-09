#include <stdio.h>

int main()
{
    int terminos;
    double x;
    double serie(double, int);
    printf("Este programa calcula \"e\" elevado a \"x\" por desarrollo en serie\ncon el numero de terminos que quieras\n");
    printf("Teclea x: ");
    scanf("%lf", &x);
    printf("Teclea el numero de terminos: ");
    scanf("%d", &terminos);
    printf("El resultado de e elevado a %g con %d terminos es %1.16lf\n", x, terminos, serie(x, terminos));

    return 0;
}
double serie(double z, int numero)
{
    double miserie = 1, frac;
    int i;
    frac = z;
    miserie += frac;
    i = 2;
    if (numero == 1)
    {
        miserie = 1;
        return miserie;
    }
    while (i <= numero)
    {
        frac = frac * z / i++;
        miserie += frac;
    }
    return miserie;
}