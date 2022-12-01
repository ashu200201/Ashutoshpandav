#include<stdio.h>

    void main()
    {
    	int a,b;
    	printf("Enter a:");
    	scanf("%d",&a);
    	printf("Enter b:");
    	scanf("%d",&b);
    	if(a>b)
    	{
    		printf("\na is maximum.");
		}
		else if(a<b)
		{
			printf("\nb is maximum.");
		}
		else
		{
			printf("\nBoth are equal.");
		} 	
	}