#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>
#include <sys/types.h>

#define MAX_INPUT_SIZE 1024
#define MAX_ARGS 64

char** split_input(char* input);
void execute_command(char** args);

// Function declarations
int main() {
    char input[MAX_INPUT_SIZE];
    char** args;
        
    // Read input from user
    while (1) {
        printf("shell> ");
        if (fgets(input, MAX_INPUT_SIZE, stdin) == NULL) {
        continue;
    }

    
    input[strcspn(input, "\n")] = 0;  // Remove the newline character from input if present
    args = split_input(input); // split the input into arguments
    execute_command(args); // Execute the command
    free(args);  // Free allocated memory for arguments
    }
    return 0;
}

char** split_input(char* input) {
    char** args = malloc(MAX_ARGS * sizeof(char*));
    char* token;
    int i = 0;

    token = strtok(input, " ");
    while (token != NULL && i < MAX_ARGS - 1) {
        args[i++] = token;
        token = strtok(NULL, " ");
    }
    args[i] = NULL; // Null-terminate the array of arguments
    return args; 
}

void execute_command(char** args) {
    if (args == NULL || args[0] == NULL){
        return;
    }
    // Special case for the `cd` command
    if (strcmp(args[0], "cd") == 0) {
        if (args[1] == NULL) {
            // No target directory specified
            fprintf(stderr, "cd: missing argument\n");
        } else if (args[2] != NULL) {
            // More than one argument provided
            fprintf(stderr, "cd: too many arguments\n");
        } else {
            // Change the directory
            if (chdir(args[1]) != 0) {
                perror("cd");
            }
        }
        return;
    }
     
    pid_t pid;
    int status;

    pid = fork();
    if (pid == -1) {
        // Error forking
        perror("fork");
    } else if (pid == 0) {
        // Child process
        if (execvp(args[0], args) == -1) {
            perror("execvp");
            exit(EXIT_FAILURE);
        }
    } else{
        // Parent process
        do {
            waitpid(pid, &status, WUNTRACED);
        } while (!WIFEXITED(status) && !WIFSIGNALED(status));
    }
}