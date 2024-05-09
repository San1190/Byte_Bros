#include <iostream>
#include <cmath>
using namespace std;
unsigned int fact(unsigned int);
unsigned int valorAbs(int);
unsigned int potencia(int , int );


int main(){

    long int n, x;
    double sol = 0.0;
    cout << "Introduce la x: ";
    cin >> x;
    cout << "Introduce la n: ";
    cin >> n;

    for(int i = 0; i <= n; i++) {


        
        sol += (long double)potencia(x, n) / fact(valorAbs(i));
        cout << "Lawqwqw solucion es: " << sol << endl;
    }

    cout << "La solucion es: "<<sol<<endl;
}

unsigned int fact(unsigned int n)
{

    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }

   

    return fact;
}

unsigned int valorAbs(int n)
{

    if (n < 0)
    {
        

        n = abs(n);
    }

    return n;
}
unsigned int potencia(int n, int x) {

    double fact = x;
    double sol = 1;

    sol += fact;

    for (int i = 2; i <= n; i++)
    {
        fact = (double)fact * x;
        sol += fact;
    }

    return sol;
}