#include <stdio.h>

int main(void) {
    double miles; // Declare a variable to store miles
    double hoursFly; // Declare a variable to store hours flying
    double hoursDrive; // Declare a variable to store hours driving

    // Prompt the user for distance in miles
    printf("Enter a distance in miles: ");
    scanf("%lf", &miles);

    // Calculate the corresponding hours flying and driving distance
    hoursFly = miles / 500.0;
    hoursDrive = miles / 60.0;

    // Print the hours flying and driving distance
    printf("%.2lf miles would take:\n", miles);
    printf("%.2lf hours to fly\n", hoursFly);
    printf("%.2lf hours to drive\n\n", hoursDrive);

    return 0;

}