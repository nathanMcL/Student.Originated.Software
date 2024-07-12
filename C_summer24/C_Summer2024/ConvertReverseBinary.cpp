#include <stdio.h>

int main(void) {
    int x;

    // Read from input
    scanf("%d",&x);

    // If the input is a positive number...
    if (x <= 0) {
        printf("Please enter a positive integer.\n");
        return 1; // If a negative number is entered, exit with an error code
    }

    while (x > 0) {
        printf("%d", x % 2);
        x = x / 2;
    }
    printf("\n");

    return 0;

}