def list_factors(n):
    rst = []
    for i in range(1, n+1):
        if n % i == 0:
            rst.append(str(i))
    return " ".join(rst)

def find_sum_and_num_factors(n):
    rst = list_factors(n)
    rst = [int(i) for i in rst.split(" ")]
    sums = sum(rst)
    return (sums, len(rst))

nums = int(input("Enter positive number: "))
print(f"Factors of {nums} are ")

rst = list_factors(nums)
print(rst)
summ, count = find_sum_and_num_factors(nums)

print(f"Sum of {rst} is {summ}")
print(f"Number of factors is {count}")
if count == 2:
    print(f"{nums} is prime number.")
else:
    print(f"{nums} is not prime number.")