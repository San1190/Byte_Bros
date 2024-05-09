#include <iostream>
#include <cmath>
using namespace std;

int LeerValores();
void Asteriscos(unsigned int);
void AsteriscosInv(unsigned int);
int main()
{

    int n = LeerValores();
    Asteriscos(n);
    AsteriscosInv(n);

    return 0;
}
int LeerValores() {
    int n;
    cout<<"Digite el valor de n: "; 
    cin >> n;

    return n;
    
}       
void Asteriscos(unsigned int n) {

    if(n > 0){
        for (int i = 1; i >= n; i++)
        {

            cout << "*";
        }

        cout << endl;
        Asteriscos(n+1);
    }
    
    
}



void AsteriscosInv(unsigned int n) {
    if (n > 0)
    {
        for (int i = 1; i <= n; i++)
        {

            cout << "*";
        }

        cout << endl;
        AsteriscosInv(n - 1);
    }
}