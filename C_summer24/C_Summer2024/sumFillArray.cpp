#include <stdio.h>
#include <stdlib.h>

// First, I want to calculate the sum of array elements
int sumArray(int array[], int length) {
    int sum = 0;
    for (int i = 0; i < length; i++) {
        sum += array[i];
    }
    return sum;
}

// Function to fill the array with user input
void fillArray(int array[], int length) {
    printf("Enter the elements of the array:\n");
    for (int i = 0; i < length; i++) {
        scanf("%d", &array[i]);
    }
}

int main(void) {
    int length;
    
    // Prompt the user to enter the number of elements
    printf("Enter the number of elements in the array: ");
    scanf("%d", &length);
    
    int* array = (int*)malloc(length * sizeof(int)); // Dynamically allocate memory for the array using malloc

    // Check if the memory was allocated
    if (array == NULL) {
        fprintf(stderr, "Memory allocation failed\n"); // `fprintf` is used to print to the standard error
        return 1; 
    }

    // Call the function to fill the array
    fillArray(array, length);

    // Call the function to calculate the sum of the array elements
    int sum = sumArray(array, length);

    // Print the sum of the array elements
    printf("The sum of the array elements is: %d\n", sum);

    // Free the allocated memory
    free(array);

    return 0;
}
