nums = int(input())
car = [0,0,0]
seq = []

for _ in range(nums):
    seq.append(int(input()))


# print(car,seq)

while len(seq) > 0:
    if car[0] == 0:
        car[0] = seq[0]
        print("A")
        seq.pop(0)
        # print(car,seq)

    if len(seq) == 0:
        break

    if car[1] == 0:
        car[1] = seq[0]
        print("B")
        seq.pop(0)
        # print(car,seq)

    if len(seq) == 0:
        break

    if car[2] == 0:
        car[2] = seq[0]
        print("C")
        seq.pop(0)
        # print(car,seq)
    
    temp = car.copy()
    car = []
    for i in temp:
        if i != 0:
            car.append(i - 1)
        else: 
            car.append(i - 1)
