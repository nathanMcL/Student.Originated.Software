#include <stdio.h>
#include <string.h>
#include "Product.h"

// TODO: implement the related function definitions in Product.c as listed below:

// InitProduct
Product InitProduct(char *name, char *code, double price, int count) {
    Product product;
    strcpy(product.name, name);
    strcpy(product.code, code);
    product.price = price;
    product.count = count;
    return product;
}
// SetName
Product SetName(char *name, Product Product) {
    strcpy(Product.name, name);
    return Product;
}

// GetName
void GetName(char *productName, Product product) {
    strcpy(productName, product.name);
}

// SetCode
Product SetCode(char *code, Product product) {
    strcpy(product.code, code);
    return product;
}

// GetCode
void GetCode(char *code, Product product) {
    strcpy(code, product.code);
}

// SetPrice
Product SetPrice(double price, Product product) {
    product.price = price;
    return product;
}

// GetPrice
double GetPrice(Product product) {
    return product.price;
}

// SetCount
Product SetCount(int count, Product product) {
    product.count = count;
    return product;
}

// GetCount
int GetCount(Product product) {
    return product.count;
}

// AddInventory
Product AddInventory(int amt, Product product) {
    product.count += amt;
    return product;
}

// SellInventory
Product SellInventory(int amt, Product product) {
    product.count -= amt;
    return product;
}


