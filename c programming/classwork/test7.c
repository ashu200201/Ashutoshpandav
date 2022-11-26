#include<stdio.h>

void main()
{
	int age;
	char name[50];
	float salary;
	
	printf("\n\xB2\xB2\xB2\xB2 Calculator \xB2\xB2\xB2\xB2");
	
	printf("\nEnter your name:");
	//scanf("%s",&name);/*(for only string)*/
	//scanf("%c",&name); /*for single charater*/
	gets(name);/*character with space*/
	printf("\nEnter your age:");
	scanf("%d",&age);
	printf("\nEnter your salary:");
	scanf("%f",&salary);
	
	printf("\nName is:%s",name);
	printf("\nAge is:%d",age);
	printf("\nSalary is:%.2f",salary);
	
}