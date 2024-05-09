#include <stdio.h>

int main()
{
	
	int x,y,z,t;
	int max, min;
	
	printf("Introduzca número 1: ");
	scanf("%d",&x);
	
	printf("Introduzca número 2: ");
	scanf("%d",&y);
	
	printf("Introduzca número 3: ");
	scanf("%d",&z);
	
	printf("Introduzca número 4: ");
	scanf("%d",&t);
	
	 if(x >= y && x >= z && x >= t){
            max=x;
        }else{
            if(y > x && y > z && y > t){
                max=y;
            }else{
                if(z > x && z > y && z > t){
                    max=z;
                }else
                    max=t;
            }
        }
        if(x < y && x < z && x < t){
            min=x;
        }else{
            if(y < x && y < z && y < t){
                min=y;
            }else{
                if(z < x && z < y && z < t){
                    min=z;
                }else
                    min =t;
                    
	printf("El número máximo es %d y el mínimo %d", max,min);
	
	return 0
	
	
	
	
	
}
