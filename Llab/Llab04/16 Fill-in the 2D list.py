nums = int(input("Enter the number of rows or columns : "))


temp = 0
for i in range(nums):
    for j in range(nums):
        print(f"{j + 1+temp:^3}",end="")
    temp += 1
    print()
