#include <stdio.h>

// This is a basic view at the Swap Method...

void swap(int *a, int *b) {
    int temp;  // Temporary variable to hold one of the values
    temp = *a;
    *a = *b;
    *b = temp;
}

// Swap using arithmetic operations
void swap_arithmetic(int *a, int *b) {
    *a = *a + *b;
    *b = *a - *b;
    *a = *a - *b;
}

// Swap using bitwise XOR
void swap_xor(int *a, int *b) {
    *a = *a ^ *b;
    *b = *a ^ *b;
    *a = *a ^ *b;
}

int main() {
    int x = 5;
    int y = 10;

    printf("Before the swap (temp): x = %d, y = %d\n", x, y);
    swap(&x, &y);
    printf("After the swap (temp): x = %d, y = %d\n", x, y);

    // Reset values
    x = 5;
    y = 10;

    printf("Before the swap (arithmetic): x = %d, y = %d\n", x, y);
    swap_arithmetic(&x, &y);
    printf("After the swap (arithmetic): x = %d, y = %d\n", x, y);

    // Reset values
    x = 5;
    y = 10;

    printf("Before swap (xor): x = %d, y = %d\n", x, y);
    swap_xor(&x, &y);
    printf("After swap (xor): x = %d, y = %d\n", x, y);

    return 0;
}