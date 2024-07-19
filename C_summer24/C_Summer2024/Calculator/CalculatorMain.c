#include <stdio.h>

#include "Calculator.h"

int main() {
	Calculator calc = InitCalculator();
	double num1;
	double num2;

	scanf("%lf", &num1);
	scanf("%lf", &num2);

	// 1. The initial value
	printf("%.1lf\n", GetValue(calc));

	// 2. The value after adding num1
	calc = Addition(num1, calc);
	printf("%.1lf\n", GetValue(calc));

	// 3. The value after multiplying by 3
	calc = Multiplication(3, calc);
	printf("%.1lf\n", GetValue(calc));

	// 4. The value after subtracting num2
	calc = Subtraction(num2, calc);
	printf("%.1lf\n", GetValue(calc));

	// 5. The value after dividing by 2
	calc = Division(2, calc);
	printf("%.1lf\n", GetValue(calc));

	// 6. The value after calling the Clear() method
	calc = Clear(calc);
	printf("%.1lf\n", GetValue(calc));

	return 0;
}
