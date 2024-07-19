#include <stdio.h>
#include <string.h>

#include "Product.h"

int main() {
   char name[20];
   char productName[20];
	char code[20];
	char productCode[20];
	strcpy(name, "Apple");
	strcpy(code, "SKU234");
	double price = 0.40;
	int num = 3;
	Product product  = InitProduct(name, code, price, num);

	// Test 1 - Are instance variables set/returned properly?
	GetName(productName, product);
	GetCode(productCode, product);
	printf("Name: %s\n", productName);
	printf("Code: %s\n", productCode);
	printf("Price: %.2lf\n", GetPrice(product));
	printf("Count: %d\n\n", GetCount(product));

	// Test 2 - Are instance variables set/returned properly after adding and selling?
	num = 10;
	product = AddInventory(num, product);
	num = 5;
	product = SellInventory(num, product);
	GetName(productName, product);
	GetCode(productCode, product);
	printf("Name: %s\n", productName);
	printf("Code: %s\n", productCode);
	printf("Price: %.2lf\n", GetPrice(product));
	printf("Count: %d\n\n", GetCount(product));

	// Test 3 - Do setters work properly?
	strcpy(name, "Golden Delicious");
	product = SetName(name, product);
	strcpy(code, "SKU555");
	product = SetCode(code, product);
	price = 0.55;
	product = SetPrice(price, product);
	num = 4;
	product = SetCount(num, product);
	GetName(productName, product);
	GetCode(productCode, product);
	printf("Name: %s\n", productName);
	printf("Code: %s\n", productCode);
	printf("Price: %.2lf\n", GetPrice(product));
	printf("Count: %d\n\n", GetCount(product));

	return 0;
}