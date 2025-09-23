
def digit(num):
    return num % 10 

def tens(num):
    return (num // 10)  % 10 

def hundreds(num):
    return (num // 100) % 10 

def thousands(num):
    return (num // 1000)  % 10 

def sum_digits(num):
    return sum([int(i) for i in str(num)])
    

n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))