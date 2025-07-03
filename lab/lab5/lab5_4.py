# How many TVs do you want? 1
# How many DVD players do you want? 0
# How many audio systems do you want? 1
# The total amount is 18000.00 baht.
# Please pay 18000.00 baht. Thank you very much.



#The store offers 8% discount to the customer who purchases at least 40000 bahts. 

ratio = 40_000
price = [12000,3000,6000]

price[0] = price[0] * int(input("How many TVs do you want? "))
price[1] = price[1] * int(input("How many DVD players do you want? "))
price[2] = price[2] * int(input("How many audio systems do you want? "))

total_price = sum(price)
print(f"The total amount is {total_price:.2f} baht.")
if total_price >= ratio:
    discount = total_price * 0.08  #8% discount
    print(f"Discount: {discount:.2f} baht.")
    total_price -= discount

print(f"Please pay {total_price:.2f} baht. Thank you very much.")