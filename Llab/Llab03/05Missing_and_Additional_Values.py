lst1 = eval(input("Input list1: "))
lst2 = eval(input("Input list2: "))

result_1 = []
result_2 = []
for i in lst1:
    if i not in lst2:
        result_1.append(i)
for i in lst2:
    if i not in lst1:
        result_2.append(i)

print("Missing values in list1 =",result_2)
print("Additional values in list1 =",result_1)
print("Missing values in list2 =",result_1)
print("Additional values in list2 =",result_2)


