

n, m = [int(i) for i in input("City Size: ").split(' ')]
matrix = list()
for i in range(n):
    matrix.append([int(i) for i in input().split(' ')])

W_count = 0
E_count = 0
N_count = 0
S_count = 0

for i in range(n):
    #compute W 
    current_tower = matrix[i][0]
    W_count += 1
    for j in range(1, m):
        if current_tower < matrix[i][j]:
            current_tower = matrix[i][j]
            W_count += 1

    #compute E 
    current_tower = matrix[i][m-1]
    E_count += 1
    for j in range(m-2, -1,-1):
        if current_tower < matrix[i][j]:
            current_tower = matrix[i][j]
            E_count += 1

for i in range(m):
    #compute N
    current_tower = matrix[0][i]
    N_count += 1
    for j in range(1, n):
        if current_tower < matrix[j][i]:
            current_tower = matrix[j][i]
            N_count += 1

    #compute S

    current_tower = matrix[n-1][i]
    S_count += 1
    for j in range(n-2, -1,-1):
        if current_tower < matrix[j][i]:
            current_tower = matrix[j][i]
            S_count += 1

result_lst = [N_count, S_count, E_count, W_count]
max_result = max(result_lst)

for index, item in enumerate(result_lst):
    if item == max_result:
        print(["N","S","E","W"][index],end=' ')