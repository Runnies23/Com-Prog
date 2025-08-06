lst = ['a', 0, 0, 'b', 'b', 'b', 'c', 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

rst = []
current = []

temp = [lst[0]]
current = temp[0]

for i in lst[1:]:
    if i == current:
        temp.append(i)
    else:
        if len(temp) > 0:
            rst.append(temp)
            current = i
            temp = [i]

rst.append(temp)
print(rst)