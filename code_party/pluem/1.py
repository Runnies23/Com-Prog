data = open("./file/wave1/firstfive.txt").read().splitlines()
data = [int(i) for i in data if int(i) % 5 == 0]

sum = 0
for i in data:
    res = int(i) / 2
    if res / 2 in data:
        print(i)