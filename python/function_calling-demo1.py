"""
 there are 4 types of function categories
 1) function without parameters and function return type
    def funname():
        block
 2) function with parameter and function with return type
     def funname(parameters):
            block of code
"""
"""
def addition(num1,num2):
    ans=num1+num2
    print(ans)

addition(12,23)

n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
addition(n1,n2)
"""
def add():
    ans=num1+num2
    print(ans)
def sub():
    ans=num1-num2
    print(ans)
def mul():
    ans=num1*num2
    print(ans)
def div():
    ans=num1/num2
    print(ans)
status=True
while True:
    num1=int(input("Enter number 1: "))
    num2=int(input("Enter number 2: "))
    choice=int(input("Enter your choice: "))
    if choice == 1:
        add()
    elif  choice == 2:
        sub()
    elif  choice == 3:
        mul()
    elif  choice == 4:
        div()
    else:
            print("invalid")
    s=input("Do you want to continue yes or no: y/n : ")
    if s== "no"or "n":
      status=False
