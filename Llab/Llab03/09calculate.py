class MyMath():
    def __init__(self):
        self.pi = self.pi_value()

    def is_even(self, n):
        if n % 2 == 0:
            return True
        else: return False

    def fac(self, n):
        if n == 1: #base case 
            return 1 
        return n * self.fac(n - 1) # recursive 
    
    
        
    def is_prime(self, n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def divide_by(self, n, m):
        if n % m == 0:
            return True
        else: return False

    def ten_to_bi(self, n):
        text = ""
        while n > 0:
            R = n % 2
            text = str(R) + text
            n //= 2
        return text

    def ten_to_oct(self, n):
        text = ""
        while n > 0:
            R = n % 8
            text = str(R) + text
            n //= 8
        return text

    def ten_to_sixteen(self, n):
        labels = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
        text = ""
        while n > 0:
            R = n % 16
            text = str(labels[R]) + text
            n //= 16
        return text

    def int_to_roman(self, n):
        rst = ""
        roman_nums = {
            1000 : "M",
            900 : "CM",
            500 : "D",
            400 : "CD",
            100 : "C",
            90 : "XC",
            50 : "L",
            40 : "XL",
            10 : "X",
            9 : "IX",
            5 : "V",
            4 : "IV",
            1 : "I"
        }
        for key, value in roman_nums.items():
            temp = n // key
            if temp > 0:
                rst += value * temp
            n %= key
        return rst
    
    def Nilakantha_pi(self, a:int=2, n:int=1):
        if n == 51:
            return 0
        
        return  (4 / (a * (a+1) * (a+2))) * ((-1) ** (n + 1)) + self.Nilakantha_pi(a+2, n=n+1)

    def pi_value(self):
        return 3 + self.Nilakantha_pi()

my_math = MyMath()
num = int(input("Please Enter Number : "))
k = int(input("Divide by? : "))

if my_math.is_even(num):
    print('This number is even number.')
else:
    print('This number is not even number.')

if num <= 20:
    print(f'factorial is {my_math.fac(num):,.0f}.')
else:
    print('factorial TOO LONG.')

if my_math.is_prime(num):
    print('This number is a prime number.')
else:
    print('This number is not a prime number.')

if(my_math.divide_by(num,k)):
    print(f'{num} is divisible by {k}.')
else:
    print(f'{num} is not divisible by {k}.')

print(f'{num} is {my_math.ten_to_bi(num)} in base 2.')
print(f'{num} is {my_math.ten_to_oct(num)} in base 8.')
print(f'{num} is {my_math.ten_to_sixteen(num)} in base 16.')
print(f'{num} is {my_math.int_to_roman(num)} in roman numeral system.')
print(f'PI is {my_math.pi:.20f}')