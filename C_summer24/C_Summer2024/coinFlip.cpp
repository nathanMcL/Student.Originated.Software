#include <stdio.h>
#include <stdlib.h>

// Coin flipping, use an array of strings 
const char*  CoinFlip() {
    const char* outcomes[] = { "Tails", "Heads" };
    return outcomes[rand() % 2];
    }

int main(void) {
    int numbFlips;
    
    // The user should enter how many times they want to flip the coin...
    printf("Enter the number of coin flips:\n");
    scanf("%d", &numbFlips);

    // Seed for random number generator
    srand(2);

    // Next, a function to do the coin flips...
    for (int i = 0; i < numbFlips; i++) {
        printf("%s\n", CoinFlip());
    }

    return 0;

}