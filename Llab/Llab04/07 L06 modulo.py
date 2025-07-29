N = int(input("N: "))
M = int(input("M: "))

rst = []

for i in range(N):
    nums = int(input(f"Input number {i+1}: "))
    modulo = nums % M
    if modulo not in rst:
        rst.append(modulo)
        
print(len(rst))
