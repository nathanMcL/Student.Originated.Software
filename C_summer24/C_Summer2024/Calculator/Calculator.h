#ifndef CALCULATOR_H_
#define CALCULATOR_H_

// Define the Calculator_struct
typedef struct {
    double calculatorValue;
} Calculator;

// TODO: Declare functions
// InitCalculator(), Addition(), Subtraction(), Multiplication(), Division(), Clear(), GetValue()
Calculator InitCalculator();
Calculator Addition(double val, Calculator c);
Calculator Subtraction(double val, Calculator c);
Calculator Multiplication(double val, Calculator c);
Calculator Division(double val, Calculator c);
Calculator Clear(Calculator c);
double GetValue(Calculator c);


#endif
