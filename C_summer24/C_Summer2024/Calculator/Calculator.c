#include <stdio.h>
#include <string.h>

#include "Calculator.h"

// TODO: Define functions
Calculator InitCalculator() {
    Calculator c;
    c.calculatorValue = 0.0;
    return c;
}

// InitCalculator(), Addition(), Subtraction(), Multiplication(), Division(), Clear(), GetValue()
// Add the parameter to the calculator value
Calculator Addition(double val, Calculator c) {
    c.calculatorValue += val;
    return c;
}

// Subtract the parameter from the calculator value
Calculator Subtraction(double val, Calculator c) {
    c.calculatorValue -= val;
    return c;
}

// Multiply the calculator value by the parameter
Calculator Multiplication(double val, Calculator c) {
    c.calculatorValue *= val;
    return c;
}

// Divide the calculator value by the parameter
Calculator Division(double val, Calculator c) {
    c.calculatorValue /= val;
    return c;
}

// Clear the calculator value by setting it to 0.0
Calculator Clear(Calculator c) {
    c.calculatorValue = 0.0;
    return c;
}

// Return the current value of the calculator
double GetValue(Calculator c) {
    return c.calculatorValue;
}
