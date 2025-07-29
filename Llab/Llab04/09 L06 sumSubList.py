base_list = [int(i) for i in input().split()]
n = len(base_list)

while True: 
    left, right = [int(i) for i in input().split()]

    if right < 0:
        right = n - abs(right)
    if left < 0:
        left = n - abs(left)

    # print(left, right)

    if (left >= n or left < 0) and (right >= n or right < 0):
        print("x and y Bad Input")
        continue

    if (left >= n or left < 0):
        print("x Bad Input")
        continue

    if (right >= n or right < 0):
        print("y Bad Input")
        continue

    if left > right:
        break

    sample = base_list[left: right + 1]
    # print(left, right)
    # print(sample)
    print(sum(sample))
