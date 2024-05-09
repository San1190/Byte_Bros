#include <iostream>
#include <cmath>
using namespace std;
unsigned int fact(unsigned int);
unsigned int valorAbs(int);

int main()
{

    int n , k;

    cout << "Introduce un número n:";
    cin >> n;

    cout << "Introduce un numero k:";
    cin>> k;

    int factn,factk, factkn;

    factn = fact(valorAbs(n));
    factk = fact(valorAbs(k));
    factkn = fact(valorAbs(n - k));

    

    cout << "El numero es: " << factn / (factk * factkn);
    // cout << "El numero es: " << fact(n);
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