#include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    const int MAX_TITLE_CHARS = 44;  // Maximum length of movie titles
    const int LINE_LIMIT = 100;      // Maximum length of each line in the text file
    char line[LINE_LIMIT];
    char inputFileName[25];
    char titles[100][MAX_TITLE_CHARS + 1];
    char ratings[100][6];
    char showtimes[100][500];
    int movieCount = 0;
    
    // Initialize the arrays
    for (int i = 0; i < 100; ++i) {
        titles[i][0] = '\0';
        ratings[i][0] = '\0';
        showtimes[i][0] = '\0';
    }

    // Read the name of the CSV file from the user
    printf("Enter the name of the CSV file: ");
    scanf("%24s", inputFileName);

    // Open the input file
    FILE *file = fopen(inputFileName, "r");
    if (file == NULL) {
        printf("Error: File %s not found.\n", inputFileName);
        return 1;
    }

    // Read and process each line of the CSV file
    while (fgets(line, sizeof(line), file) != NULL) {
        char showtime[10];
        char title[MAX_TITLE_CHARS + 1];
        char rating[6];
        int titleLength;

        // Extract the showtime
        int i = 0;
        while (line[i] != ',' && line[i] != '\0') {
            showtime[i] = line[i];
            ++i;
        }
        showtime[i] = '\0';
        ++i; // skip the comma

        // Extract the title
        int j = 0;
        while (line[i] != ',' && line[i] != '\0') {
            if (j < MAX_TITLE_CHARS) {
                title[j] = line[i];
            }
            ++i;
            ++j;
        }
        title[MAX_TITLE_CHARS] = '\0';  // Ensure title is null-terminated
        ++i; // skip the comma

        // Extract the rating
        int k = 0;
        while (line[i] != '\n' && line[i] != '\0') {
            rating[k] = line[i];
            ++i;
            ++k;
        }
        rating[k] = '\0';

        // Check if the movie title already exists in the list
        int found = 0;
        for (int m = 0; m < movieCount; ++m) {
            if (strncmp(titles[m], title, MAX_TITLE_CHARS) == 0 && strcmp(ratings[m], rating) == 0) {
                // Append the showtime to the existing movie entry
                strcat(showtimes[m], " ");
                strcat(showtimes[m], showtime);
                found = 1;
                break;
            }
        }

        if (!found) {
            // Add a new movie entry
            strncpy(titles[movieCount], title, MAX_TITLE_CHARS);
            titles[movieCount][MAX_TITLE_CHARS] = '\0';  // Ensure null-termination
            strncpy(ratings[movieCount], rating, 5);
            ratings[movieCount][5] = '\0';  // Ensure null-termination
            strcpy(showtimes[movieCount], showtime);
            ++movieCount;
        }
    }

    fclose(file);

    // Output the formatted table
    for (int m = 0; m < movieCount; ++m) {
        printf("%-44s | %5s | %s\n", titles[m], ratings[m], showtimes[m]);
    }

    return 0;
}
