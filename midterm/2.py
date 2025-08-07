a = input("Enter a: ")
b = input("Enter b: ")

try:
    a = eval(a)
    type_a = type(a)
except: 
    type_a = str
try:
    b = eval(b)
    type_b = type(b)
except: 
    type_b = str

def check_even_odd(n):
    return "Even" if n % 2 == 0 else "Odd"

def format_float_int(n):
    if type(n) == int:
        return int(n)
    if str(n)[-2:] == ".0":
        return int(n)
    return f"{n:.2f}"

def print_type(n):
    if n == int:
        return "Integer"
    if n == float:
        return "Float"
    if n == str:
        return "String"


print(f"a is {print_type(type_a)}")
print(f"b is {print_type(type_b)}")

if type_a == int: 
    print(f"a is {check_even_odd(a)}")
if type_b == int: 
    print(f"b is {check_even_odd(b)}")


if type_a == str or type_b == str:
    if type_a == float or type_b == float:
        pass
    if type_a == str and type_b == str:
        print(f"a+b is ({a+b})")
    else:
        print(f"a*b is ({a * b})")
else:
    print(f"""a+b is {format_float_int(a+b)}
a-b is {format_float_int(a-b)}
a*b is {format_float_int(a*b)}
a/b is {format_float_int(a/b)}
""")


# print type 
# print odd even if int 
# int int float + - * /
# str str + 
# int str * 
# float * str (nothing)
