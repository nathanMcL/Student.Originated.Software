#include <stdio.h>
#include <math.h>

int main(void) {
    float side1, side2, hypotenuse, area;

    printf("Enter the length of the first side: \n");
    // scan in the floating numbers `%f`
    scanf("%f", &side1);

    printf("Enter the length of the second side: \n");
    // scan in the floating numbers `%f`
    scanf("%f", &side2);

    // D^2 = X^2 + Y^2 sqrt
    hypotenuse = sqrt((side1 * side2) + (side2 * side2));

    // Find the area of the hypotenuse
    // Area = 0.5 * side1 * side2
    area = 0.5 * side1 * side2;

    // Print the length of the hypotenuse
    printf("The length of the hypotenuse is: %.2f\n", hypotenuse);

    // print the area of the triangle
    printf("The area of the triangle is: %.2f\n", area); 

    return 0;

}