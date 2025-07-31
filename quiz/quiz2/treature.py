#treature 

text = 'qwewqe-35df4-05'

total = 0
status = ""
temp = 0
for char in text:
    print(char)
    if char.isdigit():
        temp = (temp * 10) + int(char)
    else: 
        if temp != 0:
            if status == "+" and temp < 0:
                temp = abs(temp)
            if status == "-" and temp > 0:
                temp = -1 * temp
            print("add", temp, status)
            total += temp
            temp = 0
        
    if char in "+-":
        status = char
        print("get -=", status)
    if status == "+" or status == "-":
        if not char.isdigit() and char not in "+-":
            print("loss status")
            status = ""
    
if temp != 0:
    if status == "+" and temp < 0:
        temp = -1 * temp
    if status == "-" and temp > 0:
        temp = abs(temp)
    total += temp

print(total)