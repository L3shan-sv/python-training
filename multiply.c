#include <stdio.h>
int multiply_numbers( int a , int b){
    int result = a*b;
    return result;
}

int main(){
    int a=5, b=4;
    int product;

    product =multiply_numbers(a,b);
    printf(" The product of %d and %d is: %d\n", a,b , product);
    return 0;


}