#include <iostream>
#include <iomanip>
#include <thread>
#include "../../utils.h"
using namespace std;
using namespace std::chrono;

const int MAX_SIZE = 1000000000;

typedef struct{
    int start, end;
    int *arr;
    double result; 
} Block;


void* task (void* param){
    Block *block = (Block*) param;
    double result = 0;
    for (int i = block->start; i < block->end; i++){
        result += block->arr[i];
    } return 0;
}


int main (int argc, char* argv[]){
    int *arr;
    double result;

    high_resolution_clock::time_point start, end;
	double totalTime;

    arr = new int[MAX_SIZE];
	fill_array(arr, MAX_SIZE);
    display_array("arr:", arr);

    //conteo de pares
    totalTime = 0;
    cout<<"starting..."<<endl;
    for (int j=0;j<10;j++){
        start = high_resolution_clock::now();
        for(int i=0; i<MAX_SIZE; i++){
         if(arr[i]%2==0){
                result++;
         }
        }

        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }
    totalTime /= 10;
    cout << "El tiempo total fue de" << totalTime << endl;
}