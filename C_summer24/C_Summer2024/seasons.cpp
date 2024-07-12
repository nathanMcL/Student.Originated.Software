#include <stdio.h>
#include <string.h>


int isValidDate(char month[], int day) {
    // Day: range between: 1 < `x` or > 31
    if (day < 1 || day > 31) return 0;
    //Months with 30 days
    if ((strcmp(month, "April") == 0 || strcmp(month, "June") == 0 || strcmp(month, "September") == 0 || strcmp(month, "November") == 0) && day > 30) return 0; 
    // February only has up to 29 days
    if (strcmp(month, "February") == 0 && day > 29) return 0;
    return (strcmp(month, "January") == 0 || strcmp(month, "February") == 0 || strcmp(month, "March") == 0 || strcmp(month, "April") == 0 || strcmp(month, "May") == 0 || strcmp(month, "June") == 0 || strcmp(month, "July") == 0 || strcmp(month, "August") == 0 || strcmp(month, "September") == 0 || strcmp(month, "October") == 0 || strcmp(month, "November") == 0 || strcmp(month, "December") == 0);
}

const char* getSeason(char month[], int day) {
    if ((strcmp(month, "March") == 0 && day >= 20) || strcmp(month, "April") == 0 || strcmp(month, "May") == 0 || (strcmp(month, "June") == 0 && day <= 20)) {
        return "Spring";
    } else if ((strcmp(month, "June") == 0 && day >= 21) || strcmp(month, "July") == 0 || strcmp(month, "August") == 0 || (strcmp(month, "September") == 0 && day <= 21)) {
        return "Summer";
    } else if ((strcmp(month, "September") == 0 && day >= 22) || strcmp(month, "October") == 0 || strcmp(month, "November") == 0 || (strcmp(month, "December") == 0 && day <= 20)) {
        return "Autumn";
    } else {
        return "Winter";
    }
}

int main(void) {
    char inputMonth[50];
    int inputDay;
    // Scan for user input
    scanf("%s", inputMonth);
    scanf("%d", &inputDay);

    if (!isValidDate(inputMonth, inputDay)) {
        printf("Invalid\n");
    } else {
        printf("%s\n", getSeason(inputMonth, inputDay));
    }

    return 0;
}