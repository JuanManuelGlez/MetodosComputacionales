#include <iostream>
#include <iomanip>
#include <thread>
#include "../../utils.h"
using namespace std;
using namespace std::chrono;

const int MAX_SIZE = 1000000; 
const int MAX_THREADS = 8;

typedef struct{
    int start, end;
    double result; 
} Block;


void* task (void* param){
    Block *block = (Block*) param;
    double result = 0;
    
    //calculo de pi usando la serie de Gregory-Leibniz
    for(int i=block->start; i<block->end; i++){
        result +=(i % 2 ? -1.0 : 1.0) / (2.0 * i + 1.0);
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
    //aproximación de pi usando la serie de Gregory-Leibniz multihilos
    totalTime = 0;
    cout<<"starting..."<<endl;
    for (int j=0;j<10;j++){
        
        start = high_resolution_clock::now();
        for(int i=0; i<MAX_THREADS; i++){
            blocks[i].start = i * blockSize;
            blocks[i].end = (i != (MAX_THREADS - 1))? (i + 1) * blockSize : MAX_SIZE;
            pthread_create(&tids[i], NULL, task, (void*) &blocks[i]);
        }

        result = 0;
        for (int i=0; i<MAX_THREADS; i++){
            pthread_join(tids[i], NULL);
            result += blocks[i].result;
        }

        result*=4;

        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }
    totalTime /= 10;
    cout << "El tiempo total fue de " << totalTime << endl;
    cout<<"Pi es aproximadamente: "<<setprecision(15)<<result<<endl;
}