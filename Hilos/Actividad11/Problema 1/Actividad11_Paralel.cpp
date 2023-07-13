#include <iostream>
#include <iomanip>
#include <thread>
#include "../../utils.h"
using namespace std;
using namespace std::chrono;

const int MAX_SIZE = 1000000000;
const int MAX_THREADS = 8;

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
    }
    return 0;
}


int main (int argc, char* argv[]){
    int *arr;
    double result;

    high_resolution_clock::time_point start, end;
	double totalTime = 0;
	// These variables are used by thread management.
	int blockSize;
	Block blocks[MAX_THREADS];
	pthread_t tids[MAX_THREADS];

    arr = new int[MAX_SIZE];
	fill_array(arr, MAX_SIZE);
    display_array("arr:", arr);

    //conteo de pares
    blockSize = MAX_SIZE / MAX_THREADS;
    cout<<"starting..."<<endl;
    for(int j=0;j<10;j++){
    start = high_resolution_clock::now();
    for (int i=0; i<MAX_THREADS; i++){
        blocks[i].start = i * blockSize;
        blocks[i].end = (i + 1) * blockSize;
        blocks[i].arr = arr;
        pthread_create(&tids[i], NULL, task, (void*) &blocks[i]);
    }

    for (int i=0; i<MAX_THREADS; i++){
        pthread_join(tids[i], NULL);
        result += blocks[i].result;
    }

    end = high_resolution_clock::now();
    totalTime += duration_cast<duration<double>>(end - start).count();

    }
    totalTime /= 10;
    cout<<"el tiempo promedio fue de "<<totalTime<<endl;
}