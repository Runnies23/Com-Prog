x = int(input("Enter x : "))
y = int(input("Enter y : "))

def check_prime(x):
    for i in range(2,int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


rst = []
for i in range(x,y + 1):
    if i <= 1 :
        continue
    if check_prime(i):
        rst.append(i)

if len(rst) == 0:
    print(f"No prime in between {x} and {y}")
elif len(rst) == 1:
    print(f"A prime numbers betweeb {x} and {y} is:")
    print(rst[0])
else: 
    print(f"Prime numbers between {x} and {y} are:")
    for j in rst:
        print(j)