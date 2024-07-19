#include <stdio.h>

// Recursive function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0) {
        return 1; //Base case
    } else {
        return n * factorial(n - 1);
    }
}

int main() {
    int number;

    printf("Enter a positive number: ");
    scanf("%d", &number);

    if (number < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        printf("Factorial of %d is %d\n", number, factorial(number));
    }

    return 0;
}