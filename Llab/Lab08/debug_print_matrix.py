class Fraction():
    def __init__(self, numerator:int, denominator:int=1):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self):
        greatest = 1
        for i in range(1,self.numerator+1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                greatest = max(greatest, i)

        self.numerator = int(self.numerator / greatest)
        self.denominator = int(self.denominator / greatest)
    
    def divided(self, n:int):
        self.denominator *= n

    def multiply(self, n:int):
        self.numerator *= n

    def get_val(self):
        return self.numerator

    def __str__(self):
        self.gcd()
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator} / {self.denominator}"
    
    def __format__(self, spec):
        return format(str(self), spec)
    
class Matrix:
    def __init__(self):
        pass

class Rows:
    def __init__(self):
        pass
    

m = [
           [1,      -3,       4  ,     3],
       [2,      -5,       6,       6],
      [-3,       3,       4,       6,]
    ]

matrix = []
for i in m:
    temp = []
    for j in i:
        temp.append(Fraction(j))
    matrix.append(temp)


def diff_list(first, last): #last == diff_array
    first_ = [i.get_val() for i in first]
    rst = []
    for i in range(len(first_)):
        rst.append(Fraction(first_[i] - last[i]))
    
    return rst

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:>8}'
    print(row)
  print()



#======================================================================


cols = len(matrix[0])
rows = len(matrix)

col = 0
row = 0

print(f"Augmented Matrix:")
printMat(matrix)

while row < rows:
    #คุม range
    divider = matrix[row][col].get_val()
    for i in matrix[row]:
        i.divided(divider)

    print(f"R{row+1} => R{row+1}/({divider})")

    print(matrix[0][0])
    printMat(matrix)
        
    temp_rows = row + 1
    
    while temp_rows < rows :
        multiplyer = matrix[temp_rows][col].get_val()


        # diff_array = [i.multiply(multiplyer) for i in matrix[row]]
        diff_array = []
        for i in matrix[row]:
            i.multiply(multiplyer)
            diff_array.append(i.get_val())

        # diff_array = matrix[row]

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


