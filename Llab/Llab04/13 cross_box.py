n = int(input())
# n = 13
print("." * n)

special = n // 2

for i in range(1,n-1):
    print(".",end="")
    print(" " * ((special-1) - abs(n - (i * 2 + 1))//2),end="")
    print(".",end="")
    if i == special:
        pass
    else:
        print(" " * ((abs((n) - (i * 2 + 1))//2) * 2 -1),end="")
        print(".",end="")
        
    print(" " * ((special-1) - abs(n - (i * 2 + 1))//2),end="")
    print(".")
    
print("." * n)