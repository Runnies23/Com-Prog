people, zombies = [int(i) for i in input().split()]

#====== brute force ======
store_time = [0] * people
time_people = []

for _ in range(people):
    time_people.append(int(input()))

time = 0 
while zombies > 0:
    time += 1
    store_time = [i + 1 for i in store_time]
    for index, i in enumerate(time_people):
        if store_time[index] == i:
            store_time[index] = 0
            zombies -= 1
            if zombies == 0:
                continue

print(time)

# ====== Min Heap ======
# Library 
        