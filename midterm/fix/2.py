# input_lst = [[2,6],[5,8],[10,15]]
input_lst = input("Input : ")
input_lst = eval(input_lst)
input_lst.sort()

print(input_lst)


rst = []

for i in input_lst:
    start, end = i 
    if start > end:
        continue

    if len(rst) == 0:
        rst.append(i)

    recent_start, recent_end = rst[-1]

    if start <= recent_end and end >= recent_end:
        rst.remove([recent_start,recent_end])
        rst.append([start, recent_end])
        continue

    else:
        rst.append(i)


print(f"Output :",rst)
