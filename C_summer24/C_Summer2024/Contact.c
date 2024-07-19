// Contacts

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct ContactNode_struct {
   /* Define ContactNode struct here. */
   char contactName[50];
   char contactPhoneNum[50];
   struct ContactNode_struct* nextNodePtr;   
} ContactNode;

/* TODO: Define the functions. */
// void InitializeContactNode(ContactNode* thisNode, char* initialName, char* initialPhoneNumber)- 
// Initialize thisNode with initialName and initialPhoneNumber. 
void InitializeContactNode(ContactNode* thisNode, char* initialName, char* initialPhoneNumber) {
    strcpy(thisNode->contactName, initialName);
    strcpy(thisNode->contactPhoneNum, initialPhoneNumber);
    thisNode->nextNodePtr = NULL;
}

//char* GetName(ContactNode* thisNode) - Return contactName of thisNode
char* GetName(ContactNode* thisNode) {
    return thisNode->contactName;
}

// char* GetPhoneNumber(ContactNode* thisNode) - Return contactPhoneNumber of thisNode
char* GetPhoneNumber(ContactNode* thisNode) {
    return thisNode->contactPhoneNum;
}

// void InsertAfter(ContactNode* thisNode, ContactNode* newContactNode) - Insert newContactNode after thisNode
void InsertAfter(ContactNode* thisNode, ContactNode* newContactNode) {
    newContactNode->nextNodePtr = thisNode->nextNodePtr;
    thisNode->nextNodePtr = newContactNode;
}

// ContactNode* GetNext(ContactNode* thisNode) - Return the next node of thisNode
ContactNode* GetNext(ContactNode* thisNode) {
    return thisNode->nextNodePtr;
}

// void PrintContactNode(ContactNode* thisNode) - Output contactName and contactPhoneNumber of the thisNode
void PrintContactNode(ContactNode* thisNode) {
    printf("Name: %s\n", thisNode->contactName);
    printf("Phone number: %s\n", thisNode->contactPhoneNum);
}

int main(void) {
   /* TODO: Define main() to read the name and phone number for three contacts and output each contact.
    Create three ContactNodes and use the nodes to build a linked list. */

    // Define three ContactNode pointers
    char name1[50], phoneNumber1[15];
    char name2[50], phoneNumber2[15];
    char name3[50], phoneNumber3[15];

    // Read the name and phone number for three contacts
    
    // Person One:
    printf("Enter name for Person 1: ");
    fgets(name1, 50, stdin);
    name1[strcspn(name1, "\n")] = '\0';
    printf("Enter phone number for Person 1: ");
    fgets(phoneNumber1, 15, stdin);
    phoneNumber1[strcspn(phoneNumber1, "\n")] = '\0';

    // Person Two:
    printf("Enter name for Person 2: ");
    fgets(name2, 50, stdin);
    name2[strcspn(name2, "\n")] = '\0';
    printf("Enter phone number for Person 2: ");
    fgets(phoneNumber2, 15, stdin);
    phoneNumber2[strcspn(phoneNumber2, "\n")] = '\0';

    // Person Three:
    printf("Enter name for Person 3: ");
    fgets(name3, 50, stdin);
    name3[strcspn(name3, "\n")] = '\0';
    printf("Enter phone number for Person 3: ");
    fgets(phoneNumber3, 15, stdin);
    phoneNumber3[strcspn(phoneNumber3, "\n")] = '\0';

    // Output the linked list in main(). Use a loop to print each node with PrintContactNode().

    // Create three ContactNode pointers
    ContactNode* contact1 = (ContactNode*)malloc(sizeof(ContactNode));
    InitializeContactNode(contact1, name1, phoneNumber1);

    ContactNode* contact2 = (ContactNode*)malloc(sizeof(ContactNode));
    InitializeContactNode(contact2, name2, phoneNumber2);

    ContactNode* contact3 = (ContactNode*)malloc(sizeof(ContactNode));
    InitializeContactNode(contact3, name3, phoneNumber3);


    // Link the contact nodes
    InsertAfter(contact1, contact2);
    InsertAfter(contact2, contact3);

    // Use a loop to print each node with PrintContactNode()
    printf("\nCONTACT LIST\n");
    ContactNode* current = contact1;
    while (current != NULL) {
        PrintContactNode(current);
        current = GetNext(current);
        if (current != NULL) {
            printf("\n");
        }
    }

    // Free allocated memory
    free(contact1);
    free(contact2);
    free(contact3);





   
   return 0;
}