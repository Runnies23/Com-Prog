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

    def __str__(self):
        self.gcd()
        if self.denominator == 1:
            return f"{self.numerator}"
        return f"{self.numerator} / {self.denominator}"
    
    def __format__(self, spec):
        return format(str(self), spec)
    

x = Fraction(5)

x.multiply(2)
x.divided(11)

print(x)