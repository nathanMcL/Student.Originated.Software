#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(void) {
    int NUM_CHARACTERS = 26;   // Maximum number of letters
    int MAX_SYNONYMS = 10;     // Maximum number of synonyms per starting letter
    int MAX_WORD_SIZE = 30;    // Maximum length of the input word
    int n, i;
    char word[MAX_WORD_SIZE];
    char letter;
    char* synonyms[NUM_CHARACTERS][MAX_SYNONYMS];   // Declare 2D array of string pointers for all synonyms
    char filename[MAX_WORD_SIZE + 4];
    FILE *file;

    // Initialize the 2D array
    for (n = 0; n < NUM_CHARACTERS; n++) {
        for (i = 0; i < MAX_SYNONYMS; i++) {
            synonyms[n][i] = NULL;
        }
    }

    // Read the word and letter from the user
    printf("Enter a word: ");
    scanf("%s", word);
    printf("Enter a letter: ");
    scanf(" %c", &letter);

    // Construct the filename
    snprintf(filename, sizeof(filename), "%s.txt", word);

    // Open the file
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error: File %s not found.\n", filename);
        return 1;
    }

    // Read synonyms from the file
    char line[100];
    int currentIndex = -1;
    while (fgets(line, sizeof(line), file) != NULL) {
        // Remove newline character
        line[strcspn(line, "\n")] = '\0';

        if (strcmp(line, "*") == 0) {
            currentIndex = -1;
        } else {
            if (currentIndex == -1) {
                currentIndex = line[0] - 'a';
                i = 0;
            }
            synonyms[currentIndex][i] = malloc(strlen(line) + 1);
            strcpy(synonyms[currentIndex][i], line);
            i++;
        }
    }

    fclose(file);

    // Output the synonyms that begin with the specified letter
    int index = letter - 'a';
    int found = 0;

    for (i = 0; i < MAX_SYNONYMS && synonyms[index][i] != NULL; i++) {
        printf("%s\n", synonyms[index][i]);
        found = 1;
    }

    if (!found) {
        printf("No synonyms for %s begin with %c.\n", word, letter);
    }

    // Free allocated memory
    for (n = 0; n < NUM_CHARACTERS; n++) {
        for (i = 0; i < MAX_SYNONYMS && synonyms[n][i] != NULL; i++) {
            free(synonyms[n][i]);
        }
    }

    return 0;
}
