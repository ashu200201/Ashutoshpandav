#include<stdio.h>

void main()
{
	int rollno,s1,s2,s3,tot;
	char name[20];
	float per;
	printf("\nEnter your Name:");
	scanf("%s",&name);
	//gets(name);
	printf("\nEnter your Roll NO:");
	scanf("%d",&rollno);
	printf("\nEnter your Physics Marks:");
	scanf("%d",&s1);
	printf("\nEnter your Chemistry Marks:");
	scanf("%d",&s2);
	printf("\nEnter your Maths Marks:");
	scanf("%d",&s3);
	tot=s1+s2+s3;
	per=(float)tot/3;
	
	printf("\nRoll No:%d",rollno);
	printf("\nName:%s",name);
	printf("\nTotal:%d",tot);
	printf("\nPercentage:%.2f",per);
	
	if(per>75)
	{
		printf("\nDistinction");
		
	}
	else if(per>=60)
	{
		printf("\nFirst class");
	}
	else if(per>=50)
	{
		printf("\nsecond class");
	}
	else if(per>=40)
	{
		printf("\npass class");
	}
	else
	{
		printf("\n fail!");
	}
}	