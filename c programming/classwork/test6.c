#include<stdio.h>

void main()
{
	int a,b;
	printf("enter first value:");
	scanf("%d",&a);
	printf("enter second value");
	scanf("%d",&b);
	printf("\nAddition : %d",(a+b));
	printf("\nSubtraction : %d",(a-b));
	printf("\nMultiplication : %d",(a*b));
	printf("\nDivsion : %.2f",((float)a/b));
}