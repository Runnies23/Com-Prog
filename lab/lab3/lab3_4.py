from math import pi

def circle_area(radius):
    return pi * radius * radius

def circle_circumference(radius):
    return 2 * pi * radius

radius = float(input("Enter the radius of the circle: "))
print(f"The circumference of the circle is {circle_circumference(radius):.2f}")
print(f"The area of this circle is {circle_area(radius):.2f}")