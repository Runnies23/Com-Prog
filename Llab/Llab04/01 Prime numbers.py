def isPrime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

def printAllPrimes(limit):  
    for i in range(2,limit+1):
        if isPrime(i):
            print(i ,end=" ")

number = int(input("Input n: "))
printAllPrimes(number)