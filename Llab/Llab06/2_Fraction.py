class Fraction():
    def __init__(self, numerator:int, denominator:int):
        self.numerator = numerator
        self.denominator = denominator

    def gcd(self):
        greatest = 1
        for i in range(1,self.numerator+1):
            if self.numerator % i == 0 and self.denominator % i == 0:
                greatest = max(greatest, i)

        self.numerator = int(self.numerator / greatest)
        self.denominator = int(self.denominator / greatest)

    def evaluate(self):
        return self.numerator / self.denominator

    def add(self, n:int):
        nums = self.numerator + (n * self.denominator)
        return Fraction(nums, self.denominator)

    def __add__(self, other_frac):
        numerator = self.numerator * other_frac.denominator + other_frac.numerator * self.denominator
        denominator = self.denominator * other_frac.denominator
        return Fraction(numerator, denominator)

    def multiply(self, n:int):
        if n == 0:
            return Fraction(0,1)
        nums = self.numerator * n
        return Fraction(nums, self.denominator)

    def __mul__(self, other_frac):
        numerator = self.numerator * other_frac.numerator
        denominator = self.denominator * other_frac.denominator
        return Fraction(numerator, denominator)

    def __str__(self):
        self.gcd()
        return f"{self.numerator} / {self.denominator}"

print(Fraction(22,14))
# 11 / 7
print((Fraction(1,2) + Fraction(3,4)).multiply(0))
# 0 / 1
print((Fraction(22,14) * Fraction(2, 4)).add(1))
# 25 / 14
print(Fraction(22, 7).multiply(7).multiply(7))
# 154 / 1