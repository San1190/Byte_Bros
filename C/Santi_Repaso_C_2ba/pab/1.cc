#include <iostream>
#include <cmath>
using namespace std;

int main()
{  
    const int RADIO = 4;
    float x, y, ecuacion;

    

    cout << "Introduce un valor de x: ";
    cin >> x;

    cout << "Introduce un valor de y: ";
    cin >> y;

    ecuacion = pow((x - 3), 2)  + pow((y - 2),2)  - pow(RADIO, 2);
    

    if(ecuacion > 0) {

        cout <<"El punto está en el exterior de la circunferencia";
    } else if(ecuacion < 0) {

        cout<<"El punto está en el interior de la circunferencia";

    } else {

        cout <<"El punto se encuentra en el trazo de la circunferencia";

    }

    return 0;
}


