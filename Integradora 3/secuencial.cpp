// Autor: Juan Manuel González Ascencio
// Matricula: A00572003
// Comando para correr: g++ secuencial.cpp -o app
// Descripción: Este programa imprime la suma de los números primos menores a 5000000


#include <iostream>
#include <iomanip>
#include <thread>
#include <math.h>
using namespace std;
using namespace std::chrono;



bool esPrimo(int n){
    if(n<2){
        return false;
    }
    for (int i=2; i<=sqrt(n); i++){
        if(n%i==0){
            return false;
            
        }
    }
    
    return true;
    
}

int main (int argc, char* argv[]){

    high_resolution_clock::time_point start, end;
	double totalTime;


    int max = 5000000;
    double suma = 0;

    totalTime = 0;
    cout<<"starting..."<<endl;
    for(int j=0; j<10;j++){
        start = high_resolution_clock::now();
        for (int i =0; i<max;i++){
            if (esPrimo(i)){
                //cout << i << "+"<<suma<<endl;
                suma=suma+i;
            }
        }
        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }

    cout << "La suma de los números primos menores a " << max << " es: " << suma/10 << endl;
    totalTime /=10;
    cout << "El tiempo total fue de " << totalTime << endl;

}