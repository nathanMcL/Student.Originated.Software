#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int GetMonthAsInt(char *monthString) {
    int monthInt;

    if (strcmp(monthString, "January") == 0) {
        monthInt = 1;
    } else if (strcmp(monthString, "February") == 0) {
        monthInt = 2;
    } else if (strcmp(monthString, "March") == 0) {
        monthInt = 3;
    } else if (strcmp(monthString, "April") == 0) {
        monthInt = 4;
    } else if (strcmp(monthString, "May") == 0) {
        monthInt = 5;
    } else if (strcmp(monthString, "June") == 0) {
        monthInt = 6;
    } else if (strcmp(monthString, "July") == 0) {
        monthInt = 7;
    } else if (strcmp(monthString, "August") == 0) {
        monthInt = 8;
    } else if (strcmp(monthString, "September") == 0) {
        monthInt = 9;
    } else if (strcmp(monthString, "October") == 0) {
        monthInt = 10;
    } else if (strcmp(monthString, "November") == 0) {
        monthInt = 11;
    } else if (strcmp(monthString, "December") == 0) {
        monthInt = 12;
    } else {
        monthInt = 0;
    }

    return monthInt;
}

int main(void) {
    char input[100];

    while (1) {
        // Read the input line
        fgets(input, sizeof(input), stdin);
        input[strcspn(input, "\n")] = '\0'; // Remove the newline character

        // Check for the end condition
        if (strcmp(input, "-1") == 0) {
            break;
        }

        // Parse the input date
        char monthStr[20], dayStr[10], yearStr[10];
        int month, day, year;

        // Check if the input matches the correct format
        if (sscanf(input, "%19s %9[^,], %9s", monthStr, dayStr, yearStr) == 3) {
            // Convert month to integer
            month = GetMonthAsInt(monthStr);
            if (month > 0) {
                // Convert day and year to integers
                day = atoi(dayStr);
                year = atoi(yearStr);

                // Print the formatted date
                printf("%d-%d-%d\n", month, day, year);
            }
        }
    }

    return 0;
}
