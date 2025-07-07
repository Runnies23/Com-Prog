#Concatenated string with uncommon characters

"""
Concatenated string with uncommon characters
Two strings are given and you have to modify the 1st string such that all the common characters of the 2nd string have to be removed and the uncommon characters of the 2nd string have to be concatenated with the uncommon characters of the 1st string.

ตัวอย่างการทำงาน 1
Input string: aacdb
Input string: gafd
cbgf
ตัวอย่างการทำงาน 2
Input string: abcs
Input string: cxzca
bsxz
หมายเหตุ: ไม่อนุญาติให้ใช้โครงสร้างข้อมูลไพท่อนเซต และคำสั่ง import ถ้าตรวจพบ จะถูกหักคะแนน -70%
"""

first_str = input("Input string: ")
second_str = input("Input string: ")


seen = set()

def add_and_drop(str, text):
    seen.add(str)

    return text.replace(str,'')

first_str = add_and_drop(first_str[0],first_str)
first_str = add_and_drop(first_str[1],first_str)
# first_str = add_and_drop(first_str[2],first_str)
for char in second_str:
    if char in seen:
        second_str = second_str.replace(char,'')

result_text = []
result_text.append(first_str)
result_text.append(second_str)


print("".join(result_text))