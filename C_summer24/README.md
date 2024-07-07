## C Programming Introduction Summer 2024


## 06/25/2024 MacN C 👨🏻‍💻
zybooks<br>

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

![Screenshot (10)](https://github.com/nathanMcL/Student.Originated.Software/assets/129904249/9674fb07-eaf5-4a24-be4c-c3d87bd78c9d)

## 06/28/2024 C++
- To create a new C file in VS code...
> new file<br>
> test.cpp<br>
- To run the new C file in VS code...
> cd C_Summer2024/<br>
> gcc -o test test.cpp<br>
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
