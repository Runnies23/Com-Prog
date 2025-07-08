# Distribute a Number

def count_digits(number):
    return len(str(number))

def get_last_digit(n):
    return n % 10

def get_distribution(number):
    result_str = []
    for i in range(count_digits(number)):
        last = get_last_digit(number)
        number //= 10 
        result_str.append(f"{last}x10^{i}")
    return ' + '.join(result_str)


nums = int(input("Input number: "))
print(f"{nums} = {get_distribution(nums)}")