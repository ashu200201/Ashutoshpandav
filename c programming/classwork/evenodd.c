#include<stdio.h>

/*
    /  -> Quotient
    %  -> Remainder
*/
    void main()
    {
    	int a;
    	printf("enter a:");
    	scanf("%d",&a);
    	
    	if(a%2==0)
    	{
    		printf("\n%d is even.",a);
		}
		else
		{
			printf("\n%d is odd.",a);
		}
	}
	