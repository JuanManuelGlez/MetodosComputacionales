#include <iostream>
#include <iomanip>
#include <thread>
using namespace std;

const int MAXIMUM = 5;

void* task (void* param){
    cout << "tid = " << pthread_self() << "is starting... " << endl;
    for (int i=1; i <= MAXIMUM; i++){
        cout << "tid = "<< pthread_self()<< "is going to terminates "<< endl;
    }
    pthread_exit(0);
}

int main(int argc, char* argv[]){
    pthread_t tid;

    cout << "this is the main thread"<<endl;
    pthread_create(&tid, NULL, task, NULL);

    cout<< "The main thread is going to terminate"<< endl;
}