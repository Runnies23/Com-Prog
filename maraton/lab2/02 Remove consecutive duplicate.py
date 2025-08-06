lst = ['a', 0, 0, 'b', 'b', 'b', 'c', 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# lst = list(map(int, eval(input("InputList: "))))
count = []
rst = []
recent = ""

for i in lst:
    if i == recent:
        continue
    else:
        rst.append(i)
        recent = i

print(rst)