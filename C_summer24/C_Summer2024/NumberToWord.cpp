#include <stdio.h>

int main(void) {

    int num;

    printf("Enter a number between 0 and 9: \n");
    scanf("%d", &num);

    if (num < 0 || num > 9) {

        printf("Invalid input. Please enter a number between 0 and 9.\n");
        return 1;

    }

    printf("%d _", num);
    switch (num) {
        case 0: printf(" Zero\n"); break;
        case 1: printf(" One\n"); break;
        case 2: printf(" Two\n"); break;
        case 3: printf(" Three\n"); break;
        case 4: printf(" Four\n"); break;
        case 5: printf(" Five\n"); break;
        case 6: printf(" Six\n"); break;
        case 7: printf(" Seven\n"); break;
        case 8: printf(" Eight\n"); break;
        case 9: printf(" Nine\n"); break;

    }
    return 0;


}