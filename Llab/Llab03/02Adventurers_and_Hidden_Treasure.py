x = input("ป้อนรหัสลับ: ")
Sum = 0 
temp = ""

for char in x:
    if char.isdigit():
        temp += char
    else: 
        if temp != "":
            Sum += int(temp)
            temp = ""

if temp != "":
    Sum += int(temp)

print("ผลลัพธ์:",Sum)