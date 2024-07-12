#include <stdio.h>

int main(void) {
    int start, end, i, j;

    printf("Enter the start number for the Multiplcation table: ");
    scanf("%d", &start);

    printf("Enter the end number for the multiplication table: ");
    scanf("%d", &end);

    // Validate the input to ensure the start is less than or equal to the end
    if (start > end) {
        printf("Invalid input. Start number should be less than or equal to end number.\n");
        return 1;

    }

    // Loop through numbers 1 to 5
    for (i = start; i <= end; i++) {
        for (j = 1; j <= end; j++) {
            printf("%d X %d = %d\n", i, j, i * j);
        }
    }

    return 0;
}
