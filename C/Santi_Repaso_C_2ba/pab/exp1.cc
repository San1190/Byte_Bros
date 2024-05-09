#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int num, i; 
    double fact , x,sol = 1;

    cout << "Introduce el valor de x:";
    cin >> x;


    cout << "Introduce un numero:";
    cin >> num;

    fact = x;
    sol += fact;
    if(num == 1) {
        sol = 1;
    }
    for(i = 2; i <= num; i++) {

        fact = (double)fact * x / i;
        sol += fact;
    }
    cout <<"El resultado es:" << sol <<endl;

}
