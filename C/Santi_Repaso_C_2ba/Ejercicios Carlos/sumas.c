


#include <stdio.h>

int main(int argc, char **argv)
{
	int a = 3, b = 7;
	
	//b+=b*2;
	//a = b =2;
	a=b-=2-a*b+b+b+-a*a/b;
	printf("%d,%d",a,b);
	
	return 0;
}

