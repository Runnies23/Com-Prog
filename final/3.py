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

    def __add__(self, another_Fraction):
        if isinstance(another_Fraction,Fraction):
            numerator = self.numerator * another_Fraction.denominator + another_Fraction.numerator * self.denominator
            denominator = self.denominator * another_Fraction.denominator
            return Fraction(numerator, denominator)

    def __sub__(self, another_Fraction):
        if isinstance(another_Fraction,Fraction):
            numerator = self.numerator * another_Fraction.denominator - another_Fraction.numerator * self.denominator
            denominator = self.denominator * another_Fraction.denominator
            return Fraction(numerator, denominator)

    def __mul__(self, other_frac):
        numerator = self.numerator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        return Fraction(numerator, denominator)
        
    def swap(self):
        temp = self.numerator
        self.numerator = self.denominator
        self.denominator = temp 

    def multiply(self, n:int):
        self.numerator *= n

    def multiply_int(self, n:int):
        self.numerator *= n
        return Fraction(self.numerator, self.denominator)


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
    def __init__(self, matrix):
        new_matrix = []
        if not isinstance(matrix[0][0], Fraction):
            print("Init new class with fraction")
            for i in range(len(matrix)):
                temp_lst = []
                for j in range(len(matrix[0])):
                    temp_lst.append(Fraction(matrix[i][j]))
                new_matrix.append(temp_lst)
            self.matrix = new_matrix
        else: 
            self.matrix = matrix

    def __str__(self):
        max_space = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                text = f"{self.matrix[i][j]}"
                max_space = max(max_space, len(text))

        return_txt = ""
        space = max_space + 1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):    
                text = f"{self.matrix[i][j]}"
                return_txt += f"{(space - len(text)) * " "}{text}"
            return_txt += "\n"
        
        return return_txt
    
    def __add__(self, another):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp_lst = []
            for j in range(len(self.matrix[0])):
                temp_lst.append(self.matrix[i][j] + another[i][j])
            new_matrix.append(temp_lst)

        return Matrix(new_matrix)
    
    def __sub__(self,another):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp_lst = []
            for j in range(len(self.matrix[0])):
                temp_lst.append(self.matrix[i][j] - another[i][j])
            new_matrix.append(temp_lst)

        return Matrix(new_matrix)

    def __mul__(self,another):
        if isinstance(another, int):
            new_matrix = []
            for i in range(len(self.matrix)):
                temp_lst = []
                for j in range(len(self.matrix[0])):
                    temp_frac = self.matrix[i][j].clone()
                    temp_lst.append(temp_frac.multiply_int(another))
                new_matrix.append(temp_lst)
            return Matrix(new_matrix)
        
        elif isinstance(another, Matrix):
            new_matrix = []
            for i in range(len(self.matrix)):
                temp_lst = []
                for j in range(len(self.matrix[0])):
                    temp = Fraction(0)
                    for k in range(len(self.matrix[0])):
                        temp += (self.matrix[i][k] * another[k][j])
                    temp_lst.append(temp)
                new_matrix.append(temp_lst)

            return Matrix(new_matrix)
            

    def __pow__(self,nums):
        old = self.clone()
    
        for _ in range(nums-1):

            new_matrix = []
            for i in range(len(self.matrix)):
                temp_lst = []
                for j in range(len(self.matrix[0])):
                    temp = Fraction(0)
                    for k in range(len(self.matrix[0])):
                        temp += (self.matrix[i][k] * old[k][j])
                        # print(temp)
                    temp_lst.append(temp)
                new_matrix.append(temp_lst)

        if nums == 1:
            return Matrix(self.matrix)

        return Matrix(new_matrix)
    
    def clone(self):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp_lst = []
            for j in range(len(self.matrix[0])):
                temp_lst.append(self.matrix[i][j].clone())
            new_matrix.append(temp_lst)

        return Matrix(new_matrix)

    def Trasponse(self):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp_lst = []
            for j in range(len(self.matrix[0])):
                temp_lst.append(self.matrix[j][i].clone())
            new_matrix.append(temp_lst)

        return Matrix(new_matrix)
    
    def T(self):
        new_matrix = []
        for i in range(len(self.matrix)):
            temp_lst = []
            for j in range(len(self.matrix[0])):
                temp_lst.append(self.matrix[j][i].clone())
            new_matrix.append(temp_lst)

        return Matrix(new_matrix)
    
    def Inverse(self):
        Identity_matrix = self.Identity()

        return 
    
    def Identity(self):
        new_array = []
        for i in range(len(matrix)):
            rows = []
            for j in range(len(matrix[0])):
                if i == j:
                    rows.append(Fraction(1))
                else:
                    rows.append(Fraction(0))
            new_array.append(rows)
        return Matrix(new_array)
                    

    
    def __rmul__(self, nums):
        return self.__mul__(nums)
    
    def __getitem__(self,idx):
        return self.matrix[idx]


m = [
    [1,2,-3],
    [3,4,5],
    [6,7,8]
]

matrix = Matrix(m)


print(matrix)

# print(Fraction(3) + Fraction(4))
# print(matrix + matrix)

print(matrix * matrix)
print(matrix * 3)

print(matrix)
print(matrix ** 2)

print(matrix)
print(matrix.T())


print(matrix)
print(matrix.Trasponse())


print(matrix)
print(matrix - matrix.T())

#inverse matrix

