number = input("Enter lucky number : ")
amount = int(input("Enter amount of candidates : "))
ID = []

max_val, max_ID = -99,0

for j in range(amount):
    count = 0
    txt = (input(f"Enter ID card number {j+1}: "))
    for i in txt:
        if i == number:
            count += 1
    if max_val == count:
        ID.append(txt)
    if max_val < count:
        max_val = count
        max_ID = txt
        ID = [max_ID]

for i in ID:
    if int(max_ID) < int(i):
        max_ID = i
        
print(f"Winner: {max_ID}")

