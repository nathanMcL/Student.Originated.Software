#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <pthread.h>
#include <semaphore.h>
#include <fcntl.h>
#include <sys/stat.h>
#include "common_threads.h"

sem_t *s;

void *child(void *arg) {
    printf("child\n");
    // Use semaphore
    sem_post(s);
    sleep(1);
    printf("child delayed\n");
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p;
    printf("parent: begin\n");
    // init semaphore
    s = sem_open("/sem", O_CREAT, S_IRWXU, 0);
    if (s == SEM_FAILED) {
        printf("failed to create semaphore");
        exit(0);
    }

    Pthread_create(&p, NULL, child, NULL);
    // Use semaphore
    sem_wait(s);
    pthread_join(p, NULL);
    printf("parent: end\n");

    sem_close(s);
    return 0;
}
