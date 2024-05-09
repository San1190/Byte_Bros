#include <iostream>
#include <cmath>
using namespace std;
unsigned int Fact(unsigned int);
bool Combinatorio(int, int, unsigned int &r);
void LeerValores(int &m, int &n);

int main()
{
    int m,n;
    unsigned int r;
    LeerValores(m,n);

    //r = Fact(m) / (Fact(n) * Fact(m - n));
    //cout << r;

    if(Combinatorio(m,n,r)){
        cout<<"El numero combinatorio " <<m <<" sobre ";
        cout <<n<<" es "<<r<<endl;
    } else {

        cout<<"No es posible calcular el numero combinatorio \n";
    }
    
   


    return 0;
}
void LeerValores(int &m, int &n) {
    cout<<"Indroduce el valor de m :" ; cin>>m;
    cout<<"Introduxwe n: "; cin >>n;

}

unsigned int Fact(unsigned int n)
{

    int fact = 1;

    for (int i = 1; i <= n; i++)
    {
        fact *= i;
    }

    return fact;
}


bool Combinatorio(int m, int n, unsigned int &r) {

    if( n>= 0 && m >= 0) {
        if(m > n){
            r = Fact(m) / (Fact(n) * Fact(m - n));
            //cout << r;
            return true;
        }
    }
    return false;

    
}