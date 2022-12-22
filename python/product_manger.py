menu ="""
                       menu
                       press 1 for product_manager
                       press 2 for customer
      """
#take one dictionary for product items
products={}

#flag for multiple inputs

status=True
while status:
    print(menu)
    choice=int(input("Enter your choice: "))
    if choice==1:
        spec={}
        product_name=input("Enter product name: ")
        product_qty=input("Enter product qty: ")
        product_price=("Enter product price: ")

        if product_name in products.keys():
            old_qty=products[product_name]['qty']

            spec['qty']=old_qty+product_qty
            spec['price']=product_price

            products[product_name]=spec
            print("----->already exist",products)
        else:
            spec['qty']=product_qty
            spec['price']=product_price
            
            products[product_name]=spec

            print(products)

    else:
        for k in products.keys():
            print(f"{k}=Rs.{products[k]['price']}")

    ch=input("do you want to add more products: ")
    if ch=='no':
        status=False