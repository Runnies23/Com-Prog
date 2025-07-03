status = True
data = []

while status:
    input_value = input("Enter score (or ENTER to finish): ")
    if input_value == "":
        status = False
    else:
        data.append(int(input_value))

data = sorted(data)[::-1]
for index, item in enumerate(data):
    print(f"Rank #{index+1}: {item}")