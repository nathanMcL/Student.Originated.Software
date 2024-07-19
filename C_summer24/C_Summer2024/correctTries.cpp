#include <stdio.h>

// First, Create function that only accepts user input values
// between 1 & 10, continously, until the user enters the correct value 

int getValidInput() {
    int input;
    int attempts = 0;

    // Loop until a valid input is entered
    while(1) {
        printf("Enter a number between 1 and 10: ");
        scanf("%d", &input);
        attempts++;

        // Check if the input is valid
        if (input >= 1 && input <= 10) {
            break; // Exit the loop if the input is valid
        } else {
            printf("Invalid input. Keep trying!\n");
        }
    }

    // // Print out the valid input values, AND the number of tries it took
    printf("Valid input: %d\n", input);
    printf("Number of tries: %d\n", attempts);

    return input;
}

int main() {

    // Call the function
    getValidInput();
    return 0;

}

