#include <stdio.h>
#include "SimpleCar.h"


int main() {
    SimpleCar Car = {0};
    int forwardMiles, reverseMiles;
    
    // scan in the miles to drive forward and reverse
    scanf("%d %d", &forwardMiles, &reverseMiles);

    // Drive forward
    drive(&Car, forwardMiles);
    honk();
    report(&Car);

    // Drive in reverse
    drive(&Car, -reverseMiles);
    honk();
    report(&Car);

    return 0;

}