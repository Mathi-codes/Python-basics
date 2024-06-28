#include<stdio.h>
int fact(int n){
    int fact=1;
    for (int i=1;i<n+1;i++){
        fact*=i;
    }
    return fact;
}
int main(){
    printf("Enter the number : ");
    int num,sum=0;
    scanf("%d",&num);
    while (num>0){
        int last=num%10;
        sum+=fact(last);
        num/=10;
    }
    printf("%d",sum);
}