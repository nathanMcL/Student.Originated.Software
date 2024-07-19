#ifndef PRODUCT_H_
#define PRODUCT_H_

// TODO: Create Product struct here.
// Product InitProduct(char *name, char *code, double price, int count)
typedef struct {
    char name[20];
    char code[20];
    double price;
    int count;
} Product;

// TODO: Declare related functions here.

//Product SetName(char *name, Product product) - set the product name to parameter name
Product InitProduct(char *name, char *code, double price, int count);
// void GetName(char *productName, Product product) - return the product name in productName
Product SetName(char *name, Product product);
void GetName(char *productName, Product product);
// Product SetCode(char *code, Product product) - set the product code (i.e. SKU234) to parameter code
Product SetCode(char *code, Product product);
// void GetCode(char *productCode, Product product) - return the product code in productCode
void GetCode(char *productCode, Product product);
// Product SetPrice(double price, Product product) - set the price to parameter product
Product SetPrice(double price, Product product);
// double GetPrice(Product product) - return the price
double GetPrice(Product product);
// Product SetCount(int count, Product product) - set the number of items in inventory to parameter num
Product SetCount(int count, Product product);
// int GetCount(Product product) - return the count
int GetCount(Product product);
// Product AddInventory(int amt, Product product) - increase inventory by parameter amt
Product AddInventory(int amt, Product product);
// Product SellInventory(int amt, Product product) - decrease inventory by parameter amt
Product SellInventory(int amt, Product product);

#endif