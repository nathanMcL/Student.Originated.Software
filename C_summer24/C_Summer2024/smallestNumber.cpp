#include <stdio.h>

int main(void) {
   int num1, num2, num3;
   int smallest;
   
   // Scans for values entered by a user
   scanf("%d %d %d", &num1, &num2, &num3);
   
   // Checks if the first value is the smallest
   if (num1 <= num2 && num1 <= num3) {
      smallest = num1;
      // Checks if the second value is the smallest
   } else if (num2 <= num1 && num2 <= num3) {
      smallest = num2;
      // Checks if the third value is the smallest
   } else {
      smallest = num3;
   }
   
   // Print the smallest value
   printf("%d\n", smallest);
   

   return 0;
}
