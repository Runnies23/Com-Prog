from math import pi

x = float(input('Enter x: '))
y = float(input('Enter y: '))
d = float(input('Enter d: '))


print(f"The lawn has the area of {((x*y) - (((d / 2) ** 2 )* pi)):.2f} sq.m.")