#Trapezoid


# Specify your trapezoid's properties.
# Enter length of side a: 38
# Enter length of side b: 22.4
# Height: 8.2
# The area of the trapezoid is 247.64

def trapezoid_area(A,B, height):

    area = ((A + B) / 2 ) * height

    return area


print("Specify your trapezoid's properties.")
lenght_A = float(input("Enter length of side a: "))
lenght_B = float(input("Enter length of side b: "))
lenght_height = float(input("Height: "))

print(f"The area of the trapezoid is {trapezoid_area(lenght_A,lenght_B, lenght_height):.2f}")