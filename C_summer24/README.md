## C Programming Introduction Summer 2024


## 06/25/2024 MacN C 👨🏻‍💻

### Chpt 1 
- Whitespace
- Errors & Warnings

```
0000000  0    0  !
0     0  0   0   !
0     0  0  0    !
0     0  000     !
0     0  0  0    !
0     0  0   0   
0000000  0    0  !
```  

### Chpt 2

- Variables<br>
> - When examining a sequence of assignments in C, the key thing to keep in mind is that each assignment statement is processed sequentially, and each assignment overrides the previous value of the variable unless the variable is used in the expression that computes its new value.<br>
  
```
x = 7
y = 7
z = 0
x = 5
y = 5
```
- What is x, y, & z?<br>

```
 x = 5
 y = 5
 z = 0
```

### 06/27/2024 Motivation

I like this phrase, It helps me conceptulize what the compiler is doing when an error occurs.
- The error may actually exist in an earlier line, but the compiler didn't get confused until reaching line 5.<br>

### ...
![Screenshot (10)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/9674fb07-eaf5-4a24-be4c-c3d87bd78c9d)

## 06/28/2024 C++
- To create a new C file in VS code...
> new file<br>
> test.cpp<br>
- To run the new C file in VS code...
> cd C_Summer2024/<br>
> gcc -o test test.c<br>
> ./test<br>

## 06/30/2024 ifs & else

```
#include <stdio.h>

int main(void) {
   int num1, num2, num3;
   int smallest;
   
   // Scans for values entered by a user
   scanf("%d %d %d", &num1, &num2, &num3);
   
   // Checks if the first value is the smallest
   if (num1 <= num2 && num1 <= num3) {
      smallest = num1;
      // Checks if the second value is the smallest
   } else if (num2 <= num1 && num2 <= num3) {
      smallest = num2;
      // Checks if the third value is the smallest
   } else {
      smallest = num3;
   }
   
   // Print the smallest value
   printf("%d\n", smallest);
   

   return 0;
}

```

## 07/01/2024

- Implementing a range:

  ![Screenshot (13)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/489be698-6207-407d-8938-e2876674ace9)


- Logical AND, OR and NOT
![Screenshot (14)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/a285e9d3-d210-4a37-b4a7-125ba2dbe868)
  

Logical Operator	Description<br>
- a AND b	Logical AND = true when both of its operands are true.
- a OR b	Logical OR = true when at least one of its two operands are true.
- NOT a	Logical NOT = true when its one operand is false, and vice-versa.

### 07/01/2024 1330, if / else deconstructed
 `if () {} {} {} {} {}`
 
```
if () {
         
   } else if () {
         
   } else if () {
         
   } else {
         
   }
```

```
if () {
      printf("");  
   } else if (); {
      printf("");   
   } else if (); {
      printf("");   
   } else {
      printf("");   
   }
```

```
if (letSay >= 1 && letsSay <= 20000) {
      printf("between 1 and lets say 20000k\n");  
   } else if (letsSay >= 20000 && letsSay <=30000); {
      printf("Oh! That's more than lets say 20k, but less than 30k\n");   
   } else if (letsSay >= 30000 && letsSay <= 45000); {
      printf("Lets say  30k is less 45k\n");   
   } else {
      printf("Lets say Invalid something\n");   
   }
```

## 07/02/2024 

```
Logical operator	Description
a && b	Logical AND (&&) = true when both of its operands are true
a || b	Logical OR (||) = true when at least one of its two operands are true
!a	Logical NOT (!) = true when its one operand is false, and vice-versa.
```
## 07/03/2024 for loop deconstructed

```
for (initialExpression; conditionExpression; updateExpression) {
   // Loop body
}
```

- initialExpression...
  > The initialExpression is executed at the beggining of the loop, and is used as a loop control variable <br>
  > `int i = 0;` initialize the loop variable `i` to 0...

- conditionExpression...
  > The conditionExpression is evaluated before each iteration of the loop. If the condition is true, the `loop` body is executed, else false, the loop terminates.<br>
  > if `i < 10`, then the loop continues if `i` is less than 10...<br>
  > if `arr[i] != -1`, then the loop continues as long as the element at the index `i` of array `arr` is `not equal` to -1.<br>

- updateExpression...
  > The updateExpression is executed after each iteration of the loop body, and is used to update the initialExpression     variable.<br>
  > `i++` increases the initialExpresion value by 1...
  > `i += 2` increments the initialExpresion value by 2...
  > `i--` decreases the initialExpresion value by -1...

- An example of a `for` `loop`
```
for () {()}
for (int i = 0; i < 10; i++) {()}
for (int i = 0; i < 10; i++) { // i is initialized to 0, the loop runs while i is less than 10
  printf("%d ", i); // The loop body, it could be anything else besides a print statement.
}
printf("\n");
```
## 07/08/2024 Two-dimensional arrays...

```
// Initializing a 2D array
int numVals[2][3] = { {22, 44, 66}, {97, 98, 99} };

// Use multiple lines to make rows more visible
int numVals[2][3] = {
   {22, 44, 66}, // Row 0
   {97, 98, 99}  // Row 1
};
```
- `int numVals[2][3]`
  > - Declares a two-dimensional array called: `numVals` with 2 rows [2] and 3 columns [3] <br>
  > - `{22, 44, 66}`: Represents the values in the first row (row 0) <br>
  > - `{97, 98, 99}`: Represents the values in the second row (row 1) <br>

- Next you could `print` all the elements in the array...
```
for (int i = 0; i < 2; ++i) {  // Iterate over the rows
  for (int j = 0; k < 3; ++j) {} // Then, iterate over the columns
    std::cout << "numVals[" << i << "][" << j << "] = " << numVals[i][j] << std::end1;
    }
  }
  return 0;
}
```

### 07/11/2024 Pass by Value vs. Pass by Pointer

In C you can use pointers in two different ways...<br>

- `Pass by Value` uses the modulus `%` ASCII symbol...<br>
> When a variable is passed to a function by `value`, the original variable is not changed...<br>
> A copy of the variable's value is made and passed to the function. This means that the functions work with a copy, not the original variable...<br>
> Any changes made to the parameter inside the function do not affect the original variable in the calling function...<br>
> Pass by Value ensures that the original data remains unchanged and isolated from modifications within the function...<br>

```
// Pass by Value uses the `%` symbol
printf("\t\ta = %2d %p\n", a, &a);
```


- `Pass by Pointer` uses the  asterisk `*` ascii symbol...<br>
> In a `Pass by Pointer` the address of the variable is 'passed' to a function...<br>
> The function can then use the address to access and modify the actual variable.
  
```
// Pass by Pointer uses the `*` symbol
printf("\t\ta = %2d %p\n", *a, a);

```

### Key Differences

- `Pass by Value`: 
> - Requires additional memory to store the copy of the variable.
> - Safer as it prevents accidental modifications to the original value...
> - `Pass by Value`: `Increment(a);` – The function receives a copy of `a`.

- `Pass by Pointer`:
> - Directly uses the memory address.
> - Less safe as it allows direct modifications to the original variable, which can lead to unintended side effects.
> - `Pass by Pointer`: `Increment(&a);` - The function receives the address of `a`.


## 07/14/2024 Malloc()...

### What is `malloc()`
- `malloc()` / "Memory Allocation" is used to dynamically allocate a specific block of memory on the heap. 
> - `Dynamically allocate` means the process of allocating memory during the runtime of the program, as opposed to static memory allocation, which occurs at compile time. <br>
> - Use when you need to allocate memory without initialization. <br> 
 

```
void* malloc(size_n size);
```
- `size` is the number of bytes to allocate <br>
> - Returns a pointer to the beginning of the block of memory allocated, if the allocation fails, it returns `NULL`. <br>

```
pointerVariableName = (dataType*)malloc(numElements * sizeof(dataType))
```


```
Int main() {
	// Allocate memory for an array of 10 integers
	int* array = (int*)malloc(10 * sizeof(int));

	// Check if malloc succeeded. Check for NULL, which can indicate that the memory allocation failed
	if (array == NULL) {
		printf("Memory allocation failed\n");
		return 1;
	}

	// Use the allocated memory
	for (int i = 0; i < 10; i++) {
		array[i] = i + 1;
		printf("%d", array[i]);
	}
	printf("\n");

	// Free the allocated memory to prevent memory leeks.
	free(array);

	return 0;

}

```
## ... and the others...
- `calloc`: Allocates memory for an array of elements, initializes all bytes to zero, and returns a pointer to the allocated memory <br>
- `realloc`: Changes the size of the previously allocated memory block, preserving the content up to the minimum of the old and new sizes.

## 07/16/2024 Grouping Data: using `struct`

- A structure `struct` in C is used to group different types of related data.<br>
- For example, a `struct` tagged `time`, might have hours, minutes, and seconds, which is information regarding the `struct` `time` but they can have different data types. <br>
- `typedef` is a keyword that is used to create a new name for an existing type called `struct`.<br>  
  
- In the following code snippet a struct is created and variables are declared within the body `{ }`.<br>
 
```
typedef struct Time_struct {
    int hours;
    int minutes;
    int seconds;
} Time;
```

Next... <br>
- We create a function that defines the structure named `Time` and passes in the declared  `struct` `members`: `hours`, `minutes`, and `seconds`.<br>

- `Time* newTime = (Time*)malloc(sizeof(Time));` <- This line allocates memory dynamically for the `Time*` structure. <br>
- The sizeof(Time) ensures that enough memory is allocated to hold all the `members` of the structure.<br>
- `if (newTime == NULL)`, this checks if the previous `malloc` function was successful.<br>
- If in the terminal, and it returns a `Memory allocation failed`, that means the memory allocation failed `NULL`, and the program exits. <br>


```
Time* CreateTime(int hours, int minutes, int seconds) {
    Time* newTime = (Time*)malloc(sizeof(Time));
    if (newTime == NULL) {
        printf("Memory allocation failed\n");
        exit(1);  // Exit if memory allocation fails
    }
```

Initializing the `Members`:<br>

-  `newTime->hours = hours; ...minutes; ...seconds;` Those lines `initialize` the members of the `Time` structure using the values passed as arguments to the function `CreateTime`. <br> 
- The `->` operator is used to access the members of the structure through a pointer `*`.<br>
Lastly... <br>
- The `return newTime;` function returns a pointer`*` to the newly created `Time` `struct`.

```
    newTime->hours = hours;
    newTime->minutes = minutes;
    newTime->seconds = seconds;
    return newTime;
```

Complete code snippet: <br>

```
typedef struct Time_struct {
    int hours;
    int minutes;
    int seconds;
} Time;

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
```

## 07/17/2024 stdout, stdin file pointers...

- `stdout` is a predefined FILE* that is pre-associated with a system's `standard output` or `stdout`. <br>
>  The predefined `FILE*` is a pointer to a file structure that is automatically setup when the program starts.<br>

- `fprintf` function is used to write formatted output to a specified file stream, like the terminal.<br>

```
#include <stdio.h>

int main() {
    // Using fprintf to write a string to stdout
    fprintf(stdout, "Catastic!\n");

    // Using fprintf to write an integer to stdout
    fprintf(stdout, "%d\n", 7);

    return 0;
}
```
- The Output...
```
Catastic!
7
```
## 07/18/2024 `stdin` file pointer...

- `stdin` is a predefined file stream in C that stands for "Standard input".
> `stdin` is used to `receive input` data from the standard input device,<br>
> This could be the keyboard of a computer.<br>
> By default, when a C program reads input, it reads from the `stdin`.<br>

- `scanf` = Reads the formatted input from `stdin`.
- `fgets` = Reads a string from `stdin`.
- `getchar`= Reads a single character from `stdin`

### `stdin.c`...

```
{
    int number;

    // Prompt the user to enter a number
    printf("Enter a number: ");

    // Read the number from stdin
    scanf("%d", &number);

    // Print the  entered number
    printf("You entered: %d\n", number);

    return 0;
}
```
- Output: <br>
```
Enter a number: 7
You entered: 7
```

### `stdin` and `stdout`, `stdINOUT.c`

- The following code snippet shows how you can use both the `stdin`, and `stdout`.
- use `while (getchar() != '\n');` to clear the `Input Buffer` to remove any leftover newline characters from the previous inout.<br> 
```
{
    char input[100];
    
    // Prompt the user
    printf("Enter a string: ");
    
    // Read a string from stdin
    fgets(input, sizeof(input), stdin);
    
    // Print the entered string to stdout
    printf("You entered: %s", input);
    
    return 0;
}
``` 
- Output: <br>
```
Enter a string: Cats are awesome!
You entered: Cats are awesome!
```

## 07/19/2024 `Recursion`...

- What is `Recursion`?<br>
> Recursion is a technique in programming where you have a function call itself directly or indirectly to solve a problem.<br>
> Recursion allows for a complex problem, that can be divided into smaller, or similar sub-problems.<br>

- How is `Recursion` used in creating algorithms? <br>
`Recursion` is a method in designing algorithms that can be used to solve problems with the following approaches...<br>
> Divide-and-Conquer: Problems that can be broken down into smaller sub-problems of the same type. <br>
> Dynamic Programming: Problems that can be solved by solving overlapping sub-problems and storing their results.<br>
> Backtracking: Problems that involve exploring multiple possible solutions and discarding those that do not meet the criteria.<br>
> Fibonacci sequence, where each number is the sum of the two preceding numbers.<br>
> F(n)=F(n−1)+F(n−2)
> with base cases:
> 𝐹(0) = 0
> 𝐹(1) = 1

- classic example of recursion is calculating the factorial of a number. The factorial of a positive integer 
𝑛 n is the product of all positive integers less than or equal to 𝑛. The recursive definition of factorial is:

> 𝑛! = 𝑛×(𝑛 − 1)!
> with the base case being:
> 0! = 1

```
// Recursive function to calculate the factorial of a number
int factorial(int n) {
    if (n == 0) {
        return 1; //Base case
    } else {
        return n * factorial(n - 1);
    }
}
```
### Recursion benefits and drawbacks
- Benefits of Recursion
  > Simplicity: Recursive solutions can be simpler and more intuitive. <br>
  > Modularity: Recursive functions can be broken down into simpler sub-problems.<br>
  > Recursive Problems: Tree traversals, graph algorithms, and divided-and-conquer algorithms are naturally recursive.<br>

- Drawbacks of Recursion
> Performance: Recursive solutions can be less efficient due to repeated calculations and function call overhead.<br>
> Stack Overflow: Each recursive call adds a new layer to the call stack, which can lead to stack overflow in the recursion depthis too great.<br>
