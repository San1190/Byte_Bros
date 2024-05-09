#include <iostream>
#include <cmath>
using namespace std;

int main() {

    int n ,i;
    double x;

    double miserie = 1;
    cout<<"Escribe la x: ";
    cin >> x;

    cout<<"Escribe el numero de terminos: ";
    cin >> n;

    miserie += x;
    i = 2;

    if(n == 1) {
        miserie = 1;

    }
    while(i <= n) {
        x = x * x / i++;

        miserie += x;




    }


    cout<<"La solucion seria: " << miserie<<endl;



}