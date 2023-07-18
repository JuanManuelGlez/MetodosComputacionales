// Autor: Juan Manuel González Ascencio
// Matricula: A00572003
// Comando para correr: g++ secuencial.cpp -o app
// Descripción: Este programa imprime la suma de los números primos menores a 5000000
// Tiempo : 4.00311 segundos
// 0.00106 segundos

#include <iostream>
#include <iomanip>
#include <thread>
#include <math.h>
using namespace std;
using namespace std::chrono;


//Función que determina si un número es primo o no
bool esPrimo(int n){
    if(n<2){
        return false;
    }
    int m= sqrt(n);
    for (int i=2; i<=m; i++){
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
        suma = 0;
        start = high_resolution_clock::now();
        //Suma de los numeros primos menores a 5000000
        for (int i =0; i<max;i++){
            if (esPrimo(i)){
                //cout << i << "+"<<suma<<endl;
                suma+=i;
            }
        }
        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }

    cout << "La suma de los números primos menores a " << max << " es: " << fixed<<setprecision(0)<<suma << endl;
    totalTime /=10;
    cout << "El tiempo total fue de " << totalTime << endl;

}