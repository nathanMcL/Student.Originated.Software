#include <stdio.h>
#include <string.h>

int main(void) {
   char password[50];
   int length, i;
   
   //Promt the user...
   printf("Please enter a password you want to change:\n");
   fflush(stdout); // This allows the promt to display

   // Read the inputted password
   scanf("%s", password);
      
   // Get the length of the inputted password
   length = strlen(password);
   
   // Iterate over each of the inputted characters, and replace as needed
   for (i = 0; i < length; ++i) {
      if (password[i] == 'i') {
         password[i] = '1';   
      } else if (password[i] == 'a') {
         password[i] = '@';   
      } else if (password[i] == 'm') {
         password[i] = 'M';   
      } else if (password[i] == 'B') {
         password[i] = '8';   
      } else if (password[i] == 's') {
         password[i] = '$';   
      } else if (password[i] == 'c') {
         password[i] = '*';
      }
   }
   
   // Use an "!" to end the password
   password[length] = '!'; 
   password[length + 1] = '\0';
   
   // Print new password
   printf("New Password:\n %s\n", password);
   

   return 0;
}