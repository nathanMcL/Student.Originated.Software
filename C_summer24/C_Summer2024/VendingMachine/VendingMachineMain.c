#include <stdio.h>
#include "VendingMachine.h"

int main() {
    VendingMachine vm;
    int purchase1, restock, purchase2;

    vm = InitVendingMachine();

    // Read in the purchase1, restock, and purchase2 values
    scanf("%d %d %d", &purchase1, &restock, &purchase2);

    vm = Purchase(purchase1, vm);
    vm = Restock(restock, vm);
    vm = Purchase(purchase2, vm);

    // Report the final inventory
    Report(vm);
   

   return 0;
}