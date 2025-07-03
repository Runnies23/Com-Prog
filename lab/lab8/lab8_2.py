
status = True
data = []

while status:
    data.append(float(input("Enter a number (or 0 to exit): ")))
    if float(data[-1]) == 0.0:
        status = False

print(f"The sum of positive numbers is {sum([i for i in data if i > 0]):.2f}")
print(f"The sum of negative numbers is {sum([i for i in data if i < 0]):.2f}")