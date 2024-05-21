#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <semaphore.h>
#include "common_threads.h"
#include <fcntl.h>
#include <sys/stat.h>

sem_t *s1, *s2, *s3, *s4;

sem_t *Open_semaphore(const char *name, int val) {
  sem_t *sem = sem_open(name, O_CREAT, S_IRWXU, val);
  if (sem == SEM_FAILED) {
    printf("failed to create a semaphore.\n");
    exit(0);
  }
  return sem;
}

void Post_semaphore(sem_t *sem) {
  if (sem_post(sem) < 0) {
    perror("sem_post");
    exit(1);
  }
}

void Wait_semaphore(sem_t *sem) {
  if (sem_wait(sem) < 0) {
    perror("sem_wait");
    exit(1);
  }
}

void *child_1(void *arg) {
    printf("child 1: before\n");
    sleep(1);
    printf("child 1 delayed before child 2\n");
    Post_semaphore(s1); 
    Wait_semaphore(s2);

    printf("child 1: after\n");
    sleep(2);
    printf("child 1 delayed after child 2\n");
    Post_semaphore(s3);
    return NULL;
}

void *child_2(void *arg) {
    Wait_semaphore(s1);
    printf("child 2: before\n");
    Post_semaphore(s2);

    printf("child 2: after\n");
    Post_semaphore(s4);
    return NULL;
}

int main(int argc, char *argv[]) {
    pthread_t p1, p2;
    printf("parent: begin\n");
    // init semaphores here
    s1 = Open_semaphore("/s1", 0);
    s2 = Open_semaphore("/s2", 0);
    s3 = Open_semaphore("/s3", 0);
    s4 = Open_semaphore("/s4", 0);
    
    Pthread_create(&p1, NULL, child_1, NULL);
    Pthread_create(&p2, NULL, child_2, NULL);
    Pthread_join(p1, NULL);
    Pthread_join(p2, NULL);
    Wait_semaphore(s3); // Ensure child_1 has printed "child 1 delayed after child 2"
    Wait_semaphore(s4); // Ensure child_2 has printed "child 2: after"
    printf("parent: end\n");

    sem_close(s1);
    sem_close(s2);
    sem_close(s3);
    sem_close(s4);
    sem_unlink("/s1");
    sem_unlink("/s2");
    sem_unlink("/s3");
    sem_unlink("/s4");
    return 0;
}
