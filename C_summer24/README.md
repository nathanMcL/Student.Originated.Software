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
> new file
> test.cpp
- To run the new C file in VS code...
> cd C_Summer2024/
> gcc -o test test.cpp
> ./test

