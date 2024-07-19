#include <stdio.h>
#include <stdlib.h>

typedef struct Time_struct {
    int hours;
    int minutes;
    int seconds;
} Time;

// Allocate and return a Time as per parameters
Time* CreateTime(int hours, int minutes, int seconds) {
    Time* newTime = (Time*)malloc(sizeof(Time));
    if (newTime == NULL) {
        printf("Memory allocation failed\n");
        exit(1);  // Exit if memory allocation fails
    }
    newTime->hours = hours;
    newTime->minutes = minutes;
    newTime->seconds = seconds;
    return newTime;
}

// Read integers hours, minutes, seconds; create and return a Time using the input values
Time* ReadTime() {
    int hours, minutes, seconds;
    scanf("%d %d %d", &hours, &minutes, &seconds);
    return CreateTime(hours, minutes, seconds);
}

Time* TimeDifference(Time* end, Time* start) {
    Time* diff = CreateTime(0, 0, 0);

    // Begin with uncorrected arithmetic
    diff->hours = end->hours - start->hours;
    diff->minutes = end->minutes - start->minutes;
    diff->seconds = end->seconds - start->seconds;

    // Adjust for negative seconds
    if (diff->seconds < 0) {
        diff->seconds += 60;
        diff->minutes -= 1;
    }

    // Adjust for negative minutes
    if (diff->minutes < 0) {
        diff->minutes += 60;
        diff->hours -= 1;
    }

    return diff;
}

void PrintTime(Time* t) {
    printf("%02d:%02d:%02d", t->hours, t->minutes, t->seconds);
}

int main(void) {
    Time* start = NULL;
    Time* end = NULL;
    Time* difference = NULL;

    printf("Enter start time (hh mm ss): ");
    start = ReadTime();
    printf("Enter end time (hh mm ss): ");
    end = ReadTime();
    difference = TimeDifference(end, start);

    printf("Start:\t");
    PrintTime(start);
    printf("\nEnd:\t");
    PrintTime(end);
    printf("\nDifference: ");
    PrintTime(difference);
    printf("\n");

    // Always free dynamically allocated memory when no longer needed
    free(start);
    free(end);
    free(difference);

    return 0;
}
