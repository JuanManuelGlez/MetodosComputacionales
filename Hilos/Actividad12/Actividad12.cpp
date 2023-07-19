// Autor: Juan Manuel González Ascencio
// Matricula: A00572003
// Comando para correr: g++ paralela.cpp -o app -lpthread

#include <iostream>
#include <pthread.h>
#include <unistd.h>
#include <cstdlib>
#include <ctime>

using namespace std;

const int MAX_ESTUDIANTES = 5; 
const int MAX_REBANADAS = 8;  
int reb_pizza = MAX_REBANADAS; 

pthread_t hilos[MAX_ESTUDIANTES]; 
int ids[MAX_ESTUDIANTES]; 
pthread_cond_t cond_pizza;  
pthread_mutex_t bloqueo_pizza;  

void estudiar(int tiempo) {
    sleep(tiempo);
}

void* estudiante(void *param) {
    int id = *((int*) param);
    int tiempo;
    srand(time(0) + id);
    while(true) {
        pthread_mutex_lock(&bloqueo_pizza);
        while (reb_pizza == 0) {
            pthread_cond_wait(&cond_pizza, &bloqueo_pizza); //Espera a que haya pizza
        }
        --reb_pizza;
        cout << "Estudiante " << id << " esta comiendo una rebanada de pizza.\n"; 

        if (reb_pizza == 0) {
            cout << "Estudiante " << id << " se comio la ultima rebanada de pizza.\n";
            cout << "¡NO HAY MAS PIZZAAAA!\n";
            cout << "Estudiante " << id << " esta llamando a la pizzeria.\n";
            reb_pizza = MAX_REBANADAS;
            pthread_cond_broadcast(&cond_pizza); // En caso de que no haya pizza se avisa a todos los hilos
        }
        pthread_mutex_unlock(&bloqueo_pizza); //Desbloquea el mutex

        tiempo = (rand() % 5) + 1;
        estudiar(tiempo);
    }
    pthread_exit(NULL);
}

int main(int argc, char* argv[]) {
    for (int i = 0; i < MAX_ESTUDIANTES; i++) {
        ids[i] = i + 1; 
    }


    pthread_mutex_init(&bloqueo_pizza, NULL); //Inicializa el mutex
    pthread_cond_init(&cond_pizza, NULL);

    for (int i = 0; i < MAX_ESTUDIANTES; i++) { //Crea los hilos
        pthread_create(&hilos[i], NULL, estudiante, (void*) &ids[i]);
    }

    for (int i = 0; i < MAX_ESTUDIANTES; i++) { //Se hace el join de los hilos
        pthread_join(hilos[i], NULL);
    }

    pthread_cond_destroy(&cond_pizza); //Destruye la variable condicional
    pthread_mutex_destroy(&bloqueo_pizza);

    return 0;
}