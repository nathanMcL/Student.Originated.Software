#include <stdio.h>
#include <math.h> 

// the M_PI was not defined in the math.h libary, so I had to define it myself
#define PI 3.14159265358979323846

// Function to calculate the volume of a sphere
double sphereVolume(double radius) {
    return (4.0 / 3.0) * PI * pow(radius, 3);
}

int main() {
    double radius;
    // Prompt to enter the radius of the sphere
    printf("Enter the radius of the sphere: ");
    scanf("%lf", &radius);
    
    // Calculate the volume of the sphere 
    double volume = sphereVolume(radius);
    printf("Volume of the sphere: %lf\n", volume);

    return 0;
}
