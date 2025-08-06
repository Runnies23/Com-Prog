depth = int(input("Enter the depth of the well: "))
frog  = int(input("How high the frog can jump up? "))
down  = int(input("How far the frog slips down? "))

# depth, frog, down = 5, 3, 2

possible = True

if depth == 0 or depth == frog:
    print(f"The frog is free on day 1.")
    possible = False
elif frog <= down:
    possible = False
    print("The frog will never escape from the well.")


days = 1
while possible and depth >= 0:
    depth -= frog
    if depth <= 0:
        print(f"The frog is free on day {days}.")
        break
    print(f"On day {days} the frog leaps to the depth of {depth} meters.")
    depth += down
    print(f"At night he slips down to the depth of {depth} meters.")
    days += 1