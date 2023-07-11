#include <iostream>
#include <iomanip>
#include <thread>
#include <math.h>
using namespace std;

void* root (void* param){
    for (int i=1; i<=10; i++){
        cout<<"la raiz de "<<i<<" es "<<sqrt(i)<<endl;
    }
    pthread_exit(0);
}

void* square (void* param){
    for(int i=1; i<=10;i++){
        cout<<"El cuadrado de "<<i<<" es "<<pow(i,2)<<endl;
    }
    pthread_exit(0);
}

int main (int argc, char* argv[]){
    pthread_t raiz;
    pthread_t cuadrado;

    pthread_create (&raiz, NULL, root, NULL);
    pthread_create (&cuadrado, NULL, square, NULL);

    pthread_join(raiz, NULL);
    pthread_join(cuadrado, NULL);
    
    return 0;
}