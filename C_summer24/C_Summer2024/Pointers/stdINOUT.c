#include <stdio.h>

int main() {
    char input[100];
    
    // Prompt the user
    printf("Enter a string: ");
    
    // Read a string from stdin
    fgets(input, sizeof(input), stdin);
    
    // Print the entered string to stdout
    printf("You entered: %s", input);
    
    return 0;
}
