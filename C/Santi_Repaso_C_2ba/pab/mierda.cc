#include <iostream>
#include <cmath>
using namespace std;
int Ordenar( int n1, int n2, int n3)
{
    int max, min, inter;

    if(n1 > n2 && n2 > n3)
    {
        max = n1;
        inter = n2;
        min = n3;
    }
    else if (n2 > n1 && n1 > n3)
        {
            max = n2;
            inter = n1;
            min = n3;
        }
    else if(n1 > n3 && n3 > n2)
        {

            
            if (n3 > n1 && n3 > n2)
            {
                max = n3;
            }
        }
    }

    if (n1 < n2 && n1 < n3)
    {
        min = n1;
    }
    else
    {
        if (n2  < n1 && n2 < n3)
        {
            min = n2;
        }
        else
        {
            if (n3 < n1 && n3 < n2)
            {
                min = n3;
            }
        }
    }
    if(n1 != max && n1 != min ) {
        inter = n1;
    }
    else if(n2 != max && n2 != min) {
        inter = n2;
    }
    else if (n3 != max && n3 != min)
    {
        inter = n3;
        
    }
    return min, inter, max;
}
    

    int main()
    {
        int n1, n2, n3;
        cout << "Colo num 1:";
        cin >> n1;
        cout << "Colo num 2:";
        cin >> n2;
        cout << "Colo num 3:";
        cin >> n3;

        n1 , n2 , n3 = Ordenar(n1, n2, n3);

        cout<< "El numero mas pequeño es:"<<n1 <<"\nEl intermedio es: "<<n2<< "\nY el grande es:"<<n3<<endl;
    }
