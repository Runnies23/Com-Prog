order_lst = ["None", "Latte","Americano","Macha","Capucino","Chocolate"]
order_price = [0, 40,45,50,55,60]

def print_order():
    print(f"""0. Final
1. Latte
2. Americano
3. Macha
4. Capucino 
5. Chocolate""")

def order_coffee():
    order_dict = dict()
    total_price = 0 

    while True:
        coffe_type = int(input("Enter Coffe Type : "))
        # print(coffe_type)
        
        if coffe_type == 0:
            break

        amount = int(input(f"Amount of {order_lst[coffe_type]} : "))
        total_price += order_price[coffe_type] * amount

        if order_lst[coffe_type] not in order_dict:
            order_dict[order_lst[coffe_type]] = amount
        else:
             order_dict[order_lst[coffe_type]] += amount

    return order_dict, total_price 

def change(total_price, pay):
    change_dict = {
        1000 :0 ,
        500 :0 ,
        100 :0 ,
        50 :0 ,
        20 :0 ,
        10 :0 ,
        5 :0 ,
        1 : 0
    }

    change = pay - total_price
    print(f"Change is : {change}")
    for key, value in change_dict.items():
        temp = change // key
        change %= key

        if temp != 0:
            print(f"Change {key} : {temp}")

def print_recipe(orders_dict, custome_name, total_price):
    print("")

    order = ""
    for name, amount in orders_dict.items():
        idx = order_lst.index(name)
        price = order_price[idx]

        order += f"{name} {amount * price}, "
    
    order += f"{total_price} baht"

    print("=================")

    print(f"Customer name : {custome_name}")
    print(order)

    print("=================")

def end_day(sale_dict):
    print("=================")
    if len(sale_dict) == 0:
        print("Today sale : 0 baht")

    else: 
        total_price = 0 
        for key, value in sale_dict.items():
            print(f"{key} {value} baht")
            total_price += value
        print(f"Today sale : {total_price} baht")
    print("=================")


sale_dict = dict()
while True:
    # print_recipe()

    customer_name = input("Enter Customers Name : ")
    if customer_name.lower() == "end day":
        end_day(sale_dict)
        break

    order_dict, total_price = order_coffee()
    print(f"Price is : {total_price}")
    customer_pay = int(input("Enter Pay : "))

    change(total_price, customer_pay)
    print_recipe(order_dict, customer_name, total_price)

    if customer_name not in sale_dict:
        sale_dict[customer_name] = total_price
    else: 
        sale_dict[customer_name] += total_price


# bath -> baht 