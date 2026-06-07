#include <stdio.h>
int main (){
    int value1, value2;
    printf ("please enter the first integer");
    scanf("%d", &value1);
    printf(" please enter the second interger");
    scanf("%d", &value2);
    
    int sum = value1+value2;
    printf("The sum is: %d\n",sum );

    return 0;
    



}