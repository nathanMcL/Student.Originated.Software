#include <stdio.h>

int main() {
    int number;

    // Prompt the user to enter a number
    printf("Enter a number: ");

    // Read the number from stdin
    scanf("%d", &number);

    // Print the  entered number
    printf("You entered: %d\n", number);

    return 0;
}