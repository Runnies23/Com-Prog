def readMat(fn='gauss01.txt'):
  m = []
  with open(fn) as fp:
    for line in fp:
      m.append(line.strip().split(' '))
  return m

def printMat(m):
  for i in range(len(m)):
    row = ''
    for j in range(len(m[0])):
      row += f'{m[i][j]:>8}'
    print(row)
  print()

filename = './case/gauss10.txt'


# filename = input("Enter filename: ")
m = readMat(filename)

"""
case 7, 8, 10 is missing (the response is correct) but why error ? 
"""

class Fraction():
    def __init__(self, numerator:int, denominator:int=1):
        self.numerator = numerator
        self.denominator = denominator
        self.status = False

    def gcd(self):
        """
        after test case 10++ slow with old GCD algorithm (find because of keyboard interupt and the process in this function)

        from for loop from (a,b) => O(min(a,b)) (OOP2 Llab08 code)
        to
        euclidean to optimize the runtime
        """
        def euclidean_gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        num = self.numerator
        den = self.denominator

        if den < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

        a, b = abs(self.numerator), abs(self.denominator)
        
        g = euclidean_gcd(a, b)
        self.numerator //= g
        self.denominator //= g
    
    def divided(self, n:int):
        self.denominator *= n

    def __mul__(self, other_frac):
        numerator = self.numerator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, another_Fraction):
        if isinstance(another_Fraction,Fraction):
            numerator = self.numerator * another_Fraction.denominator - another_Fraction.numerator * self.denominator
            denominator = self.denominator * another_Fraction.denominator
            return Fraction(numerator, denominator)
        
    def swap(self):
        temp = self.numerator
        self.numerator = self.denominator
        self.denominator = temp 

    def multiply(self, n:int):
        self.numerator *= n

    def get_val(self):
        if self.denominator == 1:
            return self.numerator
        else: 
            return self.numerator / self.denominator

    def __str__(self):
        self.gcd()
        if self.denominator == 1:
            return f"{self.numerator}"
        if self.numerator == 0:
            return f"0"
        return f"{self.numerator}/{self.denominator}"
    
    def __format__(self, spec):
        return format(str(self), spec)
    
    def clone(self):
        return Fraction(self.numerator, self.denominator)
    
class Matrix:
    def __init__(self):
        pass

class Rows: #Seq of the Fraction
    def __init__(self, lst_of_frac:list, name=None):
        self.seq = lst_of_frac
        self.name = name

    def multiply(self, multiplyer:Fraction):
        rst = []
        for i in self.seq:
            # i.multiply(multiplyer)
            rst.append(i * multiplyer)
        self.seq = Rows(rst)

    def divided(self, divider:Fraction):
        divider.swap()
        rst = []
        for i in self.seq:
            # i.divided(divider)
            rst.append(i * divider)
        self.seq = Rows(rst)
        
    def __sub__(self, another_seq):
        # raise isinstance(another_seq, Rows)
    
        rst = []

        for idx in range(len(self.seq)):
            rst.append(self.seq[idx] - another_seq[idx])

        self.seq = rst

        return rst
    
    def clone(self):
        # return Rows(self.seq[:], "copy")
        return Rows([frac.clone() for frac in self.seq], "copy")
    
    def __len__(self):
        return len(self.seq)
    
    def __getitem__(self, index):
        return self.seq[index]
    
    def get_seq_lst(self):
        string = []
        """
        expect : 
        [2, -6, 8, 6]
        and 
               1      -3       4       3
        """

        for item in self.seq:
            string.append(str(item))

        return f"[{", ".join(string)}]"
    
map_idx_to_char = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
# m = [
#            [1,      -3,       4  ,     3],
#        [2,      -5,       6,       6],
#       [-3,       3,       4,       6,]
#     ]

# matrix = [       [1,     -2,       3   ,    9],
#       [-1,       3,       0,      -4],
#        [2,      -5,       5,      17]]

# matrix = [
#          [ 1,       1,       1 ,  10000],
#        [5,       8 ,      9,   77000],
#        [2,       0,      -1,       0],

# ]



matrix = []
for i in m:
    temp = []
    for j in i:
        temp.append(Fraction(int(j)))

    matrix.append(Rows(temp))

cols = len(matrix[0])
rows = len(matrix)

col = 0
row = 0

# print(f"cols : {cols}, rows : {rows}")

print(f"Augmented Matrix:")
printMat(matrix)

while row < rows:
    #คุม range
    divider = matrix[row][col].clone()

    print(f"R{row+1} => R{row+1}/({divider})")
    matrix[row].divided(divider)  
    printMat(matrix)
        
    temp_rows = row + 1
    
    while temp_rows < rows :
        multiplyer = matrix[temp_rows][col].clone()
    
        diff_array = matrix[row].clone()
        # print(matrix[0].get_seq_lst())
        diff_array.multiply(multiplyer)
        # print(matrix[0].get_seq_lst())

        print(f"R{row+1}'->({multiplyer})*R{row+1} {diff_array.get_seq_lst()}")
        print(f"R{temp_rows+1} ==> R{temp_rows+1}-R{row + 1}'")
        matrix[temp_rows] =  Rows(matrix[temp_rows] - diff_array) #diff_list(matrix[temp_rows],diff_array)
        del diff_array
        printMat(matrix)
        # matrix[temp_rows] = matrix[temp_rows] - diff_array #diff_list(matrix[temp_rows],diff_array)
        # printMat(matrix)

    #     break
    # break
        
        
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
    total = matrix[row][cols-1].clone()
    
    count = 0
    col = cols - 1
    while col >= 0:
        if count == times:
            # print("save data:", total)
            store_data[row] = total
            break
        else:
            # print("add : ",{store_data[col-1] * matrix[row][col-1]},"total:",total,end="\t")
            # print(store_data[col-1].get_val(), type(store_data[col-1].get_val()))
            # print(matrix[row][col-1].get_val(), type(matrix[row][col-1].get_val()))
            # print(store_data[col-1].get_val(), matrix[row][col-1])

            total -= store_data[col-1] * matrix[row][col-1]
            # print(total)
        count += 1
            
        col -= 1
    times += 1
    row -= 1

print("After Back-Substitution:")
for idx, i in enumerate(store_data): 
  print(f"{map_idx_to_char[idx]} = {i}")
print()