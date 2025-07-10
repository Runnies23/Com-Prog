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

# seen = set()
seen = []

for ch in first_str:
    if ch in second_str and ch not in seen:
        seen.append(ch)

def add_and_drop(text, set_val):
    result = ''
    for ch in text:
        if ch not in set_val:
            result += ch
    return result

first_str = add_and_drop(first_str,seen)
second_str = add_and_drop(second_str,seen)


print(first_str+second_str)