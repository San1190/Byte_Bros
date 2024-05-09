#include <iostream>
#include <cmath>
using namespace std;
unsigned int Fact(unsigned int x)
{
    if (x == 0)
    {
        x == 1;
    }
    else
    {
        x = x * Fact(x - 1);
    }
    return x;
}
int main() {
        cout<< Fact(5);


}




 