#include <stdio.h>

// (MD / MPG) * DPG = DrivingCost
double DrivingCost(double milesPerGallon, double dollarsPerGallon, double milesDriven) {
    return (milesDriven / milesPerGallon) * dollarsPerGallon;
}

int main(void) {
    double milesPerGallon, dollarsPerGallon;

    printf("Enter the car's miles per gallon:\n");
    scanf("%lf", &milesPerGallon);

    printf("Enter the price of gas\n");
    scanf("%lf", &dollarsPerGallon);

    printf("Cost for 10 miles: $%0.2lf\n",DrivingCost(milesPerGallon, dollarsPerGallon, 10.0));
    printf("Cost for 50 miles: $%0.2lf\n",DrivingCost(milesPerGallon, dollarsPerGallon, 50.0));
    printf("Cost for 400 miles: $%0.2lf\n",DrivingCost(milesPerGallon, dollarsPerGallon, 400.0));
   

   return 0;
}