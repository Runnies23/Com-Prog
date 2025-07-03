food = {
    'Salad'	: 70,
    'Soup'	: 55,
    'Steak'	: 340,
    'Wine'	: 890,
    'Orange Juice' : 30,
    'Pasta'	: 195,
    'Fried rice' : 145,
}

total_price = 0
for key,value in food.items():
    total_price += value

print(f"The discounted cost is {total_price-(total_price * 0.08):.2f}")