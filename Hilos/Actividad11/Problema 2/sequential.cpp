#include <iostream>
#include <iomanip>
#include <thread>
#include "../../utils.h"
using namespace std;
using namespace std::chrono;

const int MAX_SIZE = 5000000; 

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
    double result;

    high_resolution_clock::time_point start, end;
	double totalTime;



    //aproximación de pi usando la serie de Gregory-Leibniz
    totalTime = 0;
    cout<<"starting..."<<endl;
    for (int j=0;j<10;j++){
        start = high_resolution_clock::now();
        for(int i=0; i<MAX_SIZE; i++){
            result += 4.0 * (i % 2 ? -1 : 1) / (2 * i + 1);
        }
        

        end = high_resolution_clock::now();
        totalTime += duration_cast<duration<double>>(end - start).count();
    }
    totalTime /= 10;
    cout << "El tiempo total fue de " << totalTime << endl;
    cout<<"Pi es aproximadamente: "<<setprecision(15)<<result/10<<endl;
}