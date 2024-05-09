#include <iostream>
using namespace std;

int main() {
	int a = 1;
	
	int num;
	
	cout<<"Introduzca un numero natural: ";
	cin>>num;
	
	for(int i = 1; i <=num ; i+= 1) {
		
		for(int j = 1; j <= i + (a-1); j++){
		
			
			cout <<"*";
			a += 2;
			
		//	i += 1;
		}
		cout<<endl;
		
		
		

		
		
	}
	
	
	
	
	

	
	
	return 0;
}
