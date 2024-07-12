#include <stdio.h>

int main(void) {
    int num;
    long long factorial = 1; 

    printf("Enter a number between 1 and 10: ");
    scanf("%d", &num);

    // Ensure the number is between 1 and 10
    if (num < 1 || num > 10) {
        printf("Invalid input. Please enter a number between 1 and 10.\n");
        return 1;
    }

    // Calculate the factorial
    for (int i = 1; i <= num; i++) {
        factorial *= i;
    }

    printf("Factorial of %d is %lld\n", num, factorial);

    return 0;
}
