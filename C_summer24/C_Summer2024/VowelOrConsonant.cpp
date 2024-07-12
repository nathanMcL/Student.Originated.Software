#include<stdio.h>


int main(void) {
    char ch;

    // create a infine loop so I don't have to execute the run command each time I test the script.
    // However after testing the program closes after it returns it's answer.
    while (1) {

        printf("Enter a character (or '0' to exit):\n ");
        printf("i.e: AbcDEfGhIJ...Z\n");

        // Reads in a character
        scanf("%c", &ch);

        // Exit condition
        if (ch == '0') {
            break;
        }

        // Using: logical OR (||). Check if the entered character was a vowel or consonant
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' ||
            ch == 'A' || ch == 'E' || ch == 'I' || ch == 'O' || ch == 'U') {
            printf("%c is a vowel.\n", ch);
            // Else if the char's range is between a - z
        } else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z')) {
            printf("%c is a consonant.\n", ch);

        } else {
            printf("%c is not a letter.\n", ch);
        }
    }
    return 0;

}