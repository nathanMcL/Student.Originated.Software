#include <stdio.h>
#include <string.h>
#include <ctype.h>

void CreateAcronym(char userPhrase[], char userAcronym[]) {
    int j = 0; // Index starts here for userAcronym
    char* token = strtok(userPhrase, " "); // String token the userPhrase 

    // While the token is not NULL...
    while (token != NULL) {
        // ...Check if the first character of the token is uppercase letter
        if (isupper(token[0])) {
            userAcronym[j++] = token[0]; // Add the uppercase letter to userAcronym
            userAcronym[j++] = '.'; // Next, we want a period to be added after each uppercase letter
        }
        token = strtok(NULL, " "); // Move to the next token
    }
    userAcronym[j] = '\0'; // Add the null terminator to userAcronym, to end the string
    
}

int main() {
    char userPhrase[51]; // Assign max length to userPhrase 
    char userAcronym[51]; // Assign max length to userAcronym

    fgets(userPhrase, sizeof(userPhrase), stdin);  // Read the input phrase using fgets
    userPhrase[strcspn(userPhrase, "\n")] = '\0';  // Remove the newline character from the input

    CreateAcronym(userPhrase, userAcronym);  // Create the acronym

    printf("%d\n", userAcronym);  // Output the results

    return 0;
}