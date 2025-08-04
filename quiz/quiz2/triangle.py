
# p = 12
p = int(input())

most = 0
for a in range(1,p // 2):
    c = ((p**2) + (2* (a ** 2)) - (2 * p * a)) / (2 * (p-a))
    print(c)
    if str(c).endswith(".0"):
        most = max(most, int(c))

print(most)