#include<stdio.h>

    void main()
    {
    	int age;
    	printf("enter age:");
    	scanf("%d",&age);
    	if(age>=18)
    	{
    		printf("\nyou are eligible for voting.");
		}
		else
		{
			printf("\nyou are not eligible for voting.");
		}
	}