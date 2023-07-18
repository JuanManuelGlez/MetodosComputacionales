// Autor: Juan Manuel González Ascencio
// Matricula: A00572003
// Comando para correr: g++ -pthread -o app paralela.cpp
// Descripción: Este programa imprime la suma de los números primos menores a 5000000 utilizando hilos 
// Tiempo: 1.22826 segundos

#include <iostream>
#include <iomanip>
#include <thread>
#include <math.h>
#include "utils.h"
using namespace std;
using namespace std::chrono;

const int MAX_SIZE = 5000000;
const int MAX_THREADS = 8;

//?
typedef struct{
    int start, end;
    double result; 
} Block;


bool esPrimo(int i){
    int n = i;  
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


void* suma(void* param){
    Block *block = (Block*) param;
    double result = 0;
    for (int i=block->start;i<block->end;i++){
    
        if(esPrimo(i)){
            result+=i;
        }
    }
    block->result = result;
    return 0;
}



int main (int argc, char* argv[]){
    double result;
    high_resolution_clock::time_point start, end;
    double totalTime;

    int blockSize;
    Block blocks[MAX_THREADS];
	pthread_t tids[MAX_THREADS];
    blockSize = MAX_SIZE / MAX_THREADS;
    cout<<"starting..."<<endl;
    for (int j=0; j<10;j++){
        start = high_resolution_clock::now();

        for (int i=0; i<MAX_THREADS; i++){
            blocks[i].start = i*blockSize;
            blocks[i].end = (i != (MAX_THREADS - 1))? (i + 1) * blockSize : MAX_SIZE;
            pthread_create(&tids[i], NULL, suma, (void*) &blocks[i]);
        }

        result = 0;
        for (int i=0; i<MAX_THREADS; i++){
            pthread_join(tids[i], NULL);
            result += blocks[i].result;
        }

        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }

    totalTime /=10;
    cout<<"El tiempo total fue de "<<totalTime<<endl;
    cout << "La suma de los números primos menores a " << MAX_SIZE << " es: " << fixed << setprecision(0)<<result << endl;

}