#ifndef VENDING_MACHINE_H
#define VENDING_MACHINE_H

typedef struct VendingMachine_struct {
   int bottles;
} VendingMachine;

VendingMachine InitVendingMachine();
VendingMachine Purchase(int amount, VendingMachine vm);
VendingMachine Restock(int amount, VendingMachine vm);
int GetInventory(VendingMachine vm);
void Report(VendingMachine vm);

#endif