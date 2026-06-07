#include <stdio.h>

 int main(){
    int age;
    printf("Please key in the age");
    scanf("%d", &age);
    if ( age >= 18){
        printf(" Youa are good my boy keep going\n");
    }
    else if  ( age >=15){
        printf(" we being serios my boy\n ");
    }
    else {
        printf(" Deathrowwww!!!!!!!!!\n");
    }
    return 0;


 }