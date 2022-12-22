"""
 function without parameters and function with return types

 syntax:
        def myfun():
            statement
"""

def checkEvenodd():
    num=int(input("Enter your number:"))
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"
print(checkEvenodd())





"""
 function with parameters and function with return types

 syntax:
        def funname(parameter):
            return statement
"""

def checkEvenodd(num):
    if num%2==0:
        return "Even Number"
    else:
        return "Odd Number"
num=int(input("Enter your number:"))
print(checkEvenodd(num))
