#include <stdio.h>
int main(){
    int balance =500;
    int amount =0;
    printf("Please key in the desired amount to withdraw");
    scanf("%d", &cash);
    
    if (amount <= 0){
        print (" Incorrect amount keyed in please retry \n");
    }
    else if (amount>balance){
        printf(" Insufficient amount in the account\n");
    }
    
    int Remainder = amount-balance;
    printf(" amount remeining in the account is %d\n");
    return 0;

}