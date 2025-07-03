import random

rand_point = int(input("Enter number of random points: "))
random.seed (2)
total = 0
for i in range(rand_point):
    # x,y = random.uniform(-1, 1), random.uniform(-1, 1) 
    x = random.uniform(-1, 1) 
    y = random.uniform(-1, 1)
    distance = ((x**2) + (y)**2)**0.5
    if distance <= 1:
        total+=1

print(f"Estimated value of pi with {rand_point} points: {(total / rand_point) * 4:.7f}")