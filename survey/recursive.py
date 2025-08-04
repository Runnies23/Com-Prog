# def recursive(n):
#     if n == 1:#base case  
#         return 1
#     return n * recursive(n-1) #recursive case 

# print(recursive(15))

def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1 
    return fibo(n-1) + fibo(n-2)

print(fibo(20))