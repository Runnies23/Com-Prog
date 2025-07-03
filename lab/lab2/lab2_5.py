time = int(input("How many total seconds? "))

hour = time // 3600
time %= 3600
minute = time // 60
time %= 60


print(f"{hour} hour(s) {minute} minute(s) and {time} second(s) have passed.")