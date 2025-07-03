nums = int(input("Enter number of levels: "))
bush = int(input("Enter bush size: "))
 
def Tree(nums):
    for i in range(nums):
        print(" " * (nums-i-1),end='')
        print("*" * ((i * 2) + 1))
    return 

for _ in range(nums):
    Tree(bush)