def diff_list(first, last):
    rst = []
    for i in range(len(first)):
        rst.append(first[i] - last[i])
    
    return rst

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:>8}'
    print(row)
  print()

  

map_idx_to_char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
matrix = [
           [1,      -3,       4  ,     3],
       [2,      -5,       6,       6],
      [-3,       3,       4,       6,]
    ]

matrix = [       [1,     -2,       3   ,    9],
      [-1,       3,       0,      -4],
       [2,      -5,       5,      17]]

matrix = [
         [ 1,       1,       1 ,  10000],
       [5,       8 ,      9,   77000],
       [2,       0,      -1,       0],

]


cols = len(matrix[0])
rows = len(matrix)

col = 0
row = 0

print(f"Augmented Matrix:")
printMat(matrix)

while row < rows:
    #คุม range
    divider = matrix[row][col]
    matrix[row] =  [i / (divider) for i in matrix[row]]
    print(f"R{row+1} => R{row+1}/({divider})")
    printMat(matrix)
        
    temp_rows = row + 1
    
    while temp_rows < rows :
        multiplyer = matrix[temp_rows][col]
    
        diff_array = [i * (multiplyer) for i in matrix[row]]
        print(f"R{row+1}'->({multiplyer})*R1 {diff_array}")
        print(f"R{temp_rows+1} ==> R{temp_rows+1}-R{row + 1}'")
        
        matrix[temp_rows] = diff_list(matrix[temp_rows],diff_array)
        
        printMat(matrix)
        
        temp_rows += 1
    
    row += 1
    col += 1
    
print(f"Result from Gaussian Elimination:")
printMat(matrix)

#solve back progation
store_data = [None] * (cols - 1)

row = rows - 1
times = 0
while row >= 0:
    total = matrix[row][cols-1]
    
    count = 0
    col = cols - 1
    while col >= 0:
        if count == times:
            # print("save data:", total)
            store_data[row] = total
            break
        else:
            # print("add : ",{store_data[col-1] * matrix[row][col-1]},"total:",total,end="\t")
            total -= store_data[col-1] * matrix[row][col-1]
            # print(total)
        count += 1
            
        col -= 1
    times += 1
    row -= 1

print("After Back-Substitution:")
for idx, i in enumerate(store_data): 
  print(f"{map_idx_to_char[idx]} = {i}")
