#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define SIZE 10
// I don't want to have to write additional functions, I want to try and combine the fill and reverse functions into on function. 
// Fill an array with random values between 0 and 100, and then create a reversed version
void fillReverseArray(int array[], int reversedArray[], int size) {
    for (int i = 0; i < size; i++) {
        array[i] = rand() % 101;
        reversedArray[size - 1 - i] = array[i]; // Now, fill the array in reverse order
    }

}

// Print the array
void printArr(const int array[], int size) {
    for (int i = 0; i < size; i++) {
        printf("%d ", array[i]);
    }
    printf("\n");
}

int main(void) {
    // Declare the arrays
    int array[SIZE];
    int reversedArray[SIZE];

    // Fill the array with random numbers...   
    srand(time(0));

    // ... and create a reversed version
    fillReverseArray(array, reversedArray, SIZE);

    // Print the original array
    printf("Original array:\n");
    printArr(array, SIZE);

    // Print the reversed array
    printf("Reversed array:\n");
    printArr(reversedArray, SIZE);

    return 0;


}