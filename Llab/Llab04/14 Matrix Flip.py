Direction = input("Direction to flip square (V/H): ").upper()
size = int(input("Input size of square: "))

matrix_a = []

for _ in range(size):
    matrix_a.append(input().split())


match Direction:
    case "V":
        rst = matrix_a[::-1]
    case "H":
        rst = []
        for i in matrix_a:
            rst.append(i[::-1])
print(f'After flip:')
for i in rst:
    print(" ".join(i))
