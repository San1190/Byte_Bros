
 


#include <stdio.h>

int main(int argc, char **argv)
{
	int a = 1, b = 5, c = 2, d = 3, e = 6;
	
	//a = d*(b/2);
	a = (d + e)*b/2;
	
	printf("El número es: %d", a);
	
	return 0;
}

