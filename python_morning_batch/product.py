import module

choice=int(input("Enter your choice: "))
price=int(input("Enter your price: "))
qty=int(input("Enter your quantity: "))
if choice==1:
     print("laptop")
     module.multiplication(price,qty)
elif choice==2:
    print("mobile")
    module.multiplication(price,qty)
else:
    print("Empty")