#include <stdio.h>
#include <math.h>   

// First, calculate the perimeter of the rectangle
void calPerm(float height, float width, float *perimeter) {
    *perimeter = 2 * (height + width);
}

// In the main function we want to prompt the user to enter the height and width of the rectangle
// Scan in the floating numbers `%f` for the height and width.
// Then, we want to calculate the perimeter of the rectangle using the `calPerm` function
// Lastly, we want to print the perimeter of the rectangle 

int main(void) {
    float height, width, perimeter;

    printf("Enter the height of the rectangle: \n");
    scanf("%f", &height);

    printf("Enter the width of the rectangle: \n");
    scanf("%f", &width);

    calPerm(height, width, &perimeter);

    printf("The perimeter of the rectangle is: %.2f\n", perimeter);

    return 0;

}