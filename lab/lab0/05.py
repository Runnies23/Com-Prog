def f(nums):
    if nums == 0:
        return 0 
    if nums % 2 == 0:
        return f(nums // 2)
    else:
        return 1 + f(nums // 2)
    
print(f(100))