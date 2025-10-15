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


    def __add__(self, another_Fraction):
        if isinstance(another_Fraction,Fraction):
            numerator = self.numerator * another_Fraction.denominator + another_Fraction.numerator * self.denominator
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
    def __init__(self, matrix:list):
        # print(type(matrix[0][0]))
        if isinstance(matrix[0][0], Fraction):
            self.matrix = matrix
        else: 
            new_matrix = []
            for i in range(len(matrix)):
                rows = []
                for j in range(len(matrix[0])):
                    rows.append(Fraction(int(matrix[i][j])))
                new_matrix.append(rows)

            self.matrix = new_matrix

    def __str__(self):
        print_string = ""
        longest_lenght = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                string = f"{self.matrix[i][j]}"
                longest_lenght = max(longest_lenght, len(string))

        longest_lenght += 1
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                string = f"{self.matrix[i][j]}"
                print_string += (longest_lenght - len(string)) * " "
                print_string += f"{self.matrix[i][j]}"
            print_string += "\n"
        
        return print_string

    # def clone(self):
    #     return Rows([frac.clone() for frac in self.seq], "copy")
    
    def __add__(self, other_matrix):
        new_matrix = []
        if isinstance(other_matrix, Matrix):
            for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    rows.append(self.matrix[i][j] + other_matrix[i][j])
                new_matrix.append(rows)

        return Matrix(new_matrix)

    def __sub__(self, other_matrix):
        new_matrix = []
        if isinstance(other_matrix, Matrix):
            for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    rows.append(self.matrix[i][j] - other_matrix[i][j])
                new_matrix.append(rows)

        return Matrix(new_matrix)

    def __mul__(self, multiplyer):
        new_matrix = []
        if isinstance(multiplyer, Matrix):
            for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    temp = Fraction(0)
                    for k in range(len(self.matrix[0])):
                        result = self.matrix[i][k] * multiplyer[k][j]
                        temp = temp + result
                    rows.append(temp)
                new_matrix.append(rows)
        else:
            for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    rows.append(self.matrix[i][j] * multiplyer)
                new_matrix.append(rows)

        return Matrix(new_matrix)

    def __rmul__(self, other_matrix):
        return self.__mul__(other_matrix)

    def __pow__(self, power):
        old_matrix = []
        for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    rows.append(self.matrix[j][i].clone())
                old_matrix.append(rows)

        for _ in range(power - 1):
            temp = []
            for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    temp_val = Fraction(0)
                    for k in range(len(self.matrix[0])):
                        result = old_matrix[i][k] * self.matrix[k][j]
                        temp_val = temp_val + result
                    rows.append(temp_val)
                temp.append(rows)
            old_matrix = temp
    
        return Matrix(old_matrix)
    
    def T(self):
        new_matrix = []
        for i in range(len(self.matrix)):
                rows = []
                for j in range(len(self.matrix)):
                    rows.append(self.matrix[j][i])
                new_matrix.append(rows)

        return Matrix(new_matrix)
    
    def Transpose(self):
        return self.T()
    
    def Inverse(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])

        #create a main matrix with 0101010
        aug = []
        for i in range(rows):
            temp_rows = []
            for j in range(cols):
                temp_rows.append(self.matrix[i][j].clone())
            for j in range(cols):
                if i == j:
                    temp_rows.append(Fraction(1))
                else:
                    temp_rows.append(Fraction(0))
            aug.append(temp_rows)

        #print debug
        # for i in range(rows):
        #     for j in range(cols * 2):
        #         print(aug[i][j], " ",end="")
        #     print("")

        for row in range(rows):
            pivot = aug[row][row].clone()

            if pivot.get_val() == 0:
                for next_row in range(row,rows):
                    if aug[next_row][rows] != 0:
                        #swap 
                        temp_lst = aug[row]
                        aug[row] = aug[next_row]
                        aug[next_row] = temp_lst

                        pivot = aug[row][row].clone()

            pivot.swap()
            aug[row] = [aug[row][i] * pivot for i in range(cols * 2)]


        #turn into down triangle 
            for idx in range(row + 1, rows):
                # print(f"factor idx : {row} {idx}")
                factor = aug[idx][row]
                
                temp = []
                for i in range(cols * 2):
                    temp.append((factor * aug[row][i]) - aug[idx][i])

                aug[idx] = temp


        #print debug
        # for i in range(rows):
        #     for j in range(cols * 2):
        #         print(aug[i][j], " ",end="")
        #     print("")
        # print("")

        #reverse compute back 
        for row in reversed(range(rows)):
            for idx in range(row):
                # print(idx, row, "/",row)
                factor = aug[idx][row]
                
                temp = []
                for i in range(cols * 2):
                    temp.append(aug[idx][i] - (factor * aug[row][i]))

                aug[idx] = temp

        #print debug
        # for i in range(rows):
        #     for j in range(cols * 2):
        #         print(aug[i][j], " ",end="")
        #     print("")
        # print("")

        matrix = []
        for i in range(rows):
            matrix.append(aug[i][cols:])

        return Matrix(matrix)
        

    def __len__(self):
        return len(self.matrix)
    
    def __getitem__(self, index):
        return self.matrix[index]
    
    def __format__(self, spec):
        return format(str(self), spec)
    

    # def __str__(self):
    #     return f"{self.numerator}/{self.denominator}"
    



m = [
    # [1,2,3],
    # [4,5,6],
    # [7,8,9]

    [2,3,1],
    [3,3,1],
    [2,4,1]
]

matrix = Matrix(m)

print(matrix)

print(matrix * 2)
print(2 * matrix)
print(matrix * matrix)


print(matrix + matrix)
print(matrix - matrix)

print(matrix.T())
print(matrix.Transpose())

print(matrix ** 2)
print(matrix)

print(matrix.Inverse())
print(matrix)
