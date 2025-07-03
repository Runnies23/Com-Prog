def rectangle_area_and_perimeter(length,width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def read_rectangle():
    length = float(input("Enter rectangle length: "))
    width = float(input("Enter rectangle width: "))
    return length,width

side1,side2 = read_rectangle()
area, peri = rectangle_area_and_perimeter(side1,side2)
print(f"The area of the rectangle is {area:.2f}")
print(f"The perimeter of the rectangle is {peri:.2f}")