#include <stdio.h>
int main(){
    secret=Leshan;
    tries=0;

    if (password==secret){
        printf(" User Authenticated ");
    }
    if ( password=! secret and tries<3){
        printf(Password Failed please recheck);
    }
    else if (password =! and tries =3){
        printf(" Too many tries ");
    }
 return 0;
}