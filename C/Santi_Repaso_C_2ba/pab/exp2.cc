#include <iostream>
#include <cmath>
using namespace std;
unsigned int fact(unsigned int);
unsigned int valorAbs(int);

int main(){

    int n;

    cout <<"Introduce un número:";
    cin>> n;

    cout <<"El numero es: " << fact(valorAbs(n));
    //cout << "El numero es: " << fact(n);
}

unsigned int fact(unsigned int n) {
    
    int fact = 1;


    for (int i = 1; i <= n; i++)
    {
        fact *= i;
        
    }


    return fact;
}

unsigned int valorAbs(int n) {

    if(n < 0) {

        n = abs(n);
    }

    return n;

}