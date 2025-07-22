m,n = [int(i) for i in input("Grid Size: ").split(" ")]
nums = int(input('Number of mine(s): '))
mine = [tuple([int(i) for i in input(f"Mine#{i+1}: ").split(" ")]) for i in range(nums)]


matrix = []
for i in range(n):
    temp = []
    for j in range(m):
        tuple_val = (j,i)
        if tuple_val in mine:
            temp.append("X")
        else:
            temp.append((j,i))
    matrix.append(temp)

def check(i,j):
    global matrix, m, n
    count = 0
    for index in range(-1,2):
        for index_2 in range(-1,2):
            idx_1 = i + index 
            idx_2 = j + index_2
            # print(idx_1, idx_2)
            if idx_1 < 0 or idx_2 < 0 or idx_1 >= m or idx_2 >= n:
                continue
            if matrix[idx_2][idx_1] == "X":
                count += 1
    return count

matrix_result = []
for i in range(n):
    temp = []
    for j in range(m):
        if matrix[i][j] == "X":
            temp.append("X")
        else:
            # print(i,j,check(i,j))
            temp.append(check(j,i))



    matrix_result.append(temp)

for i in matrix_result:
    for j in i:
        print(j,end=" ")
    print()