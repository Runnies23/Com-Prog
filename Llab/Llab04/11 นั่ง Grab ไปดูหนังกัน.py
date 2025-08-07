# car_size = 4
# total = 0
# lst = []

# input_text = input()

# # if input_text == "1 2 4 3 3":
# #     print("4")


# for i in input_text.split():
#     i = int(i)
#     if car_size == i:
#         total += 1
#     else: 
#         lst.append(i)


# # two pointer
# left, right = 0, len(lst)-1
# lst.sort()
# while left <= right:
#     if lst[left] + lst[right] <= car_size:
#         left += 1 
#     right -= 1
#     total += 1

# print(total)

# =================================== method 2 ===================================

# from collections import Counter

# groups = list(map(int, input().split()))
# count = Counter(groups)

# cars = count[4]
# temp = min(count[3], count[1])
# cars += temp

# count[3] -= temp
# count[1] -= temp

# cars += count[3]

# if count[2]:
#     temp = count[2] // 2
#     cars += temp
#     count[2] = count[2] % 2

# if count[2]:
#     cars += 1
#     temp = min(2, count[1])
#     count[1] -= temp

# if count[1] > 0:
#     cars += (count[1] + 3) // 4

# print(count)
# print(cars)


# =================================== method 3 ===================================
car_size = 4
total = 0
lst = []

for i in input().split():
    i = int(i)
    if car_size == i:
        total += 1
    else: 
        lst.append(i)

lst.sort(reverse=True)
left, right = 0, len(lst)-1

print(lst)

while len(lst) > 0:
    temp = lst[0]
    lst.pop(0)
    right = len(lst) - 1

    while right >= 0:
        print(temp + lst[right])
        if temp + lst[right] <= car_size:
            temp += lst[right]
            right -= 1 
            lst.pop()
            #print(temp + lst[right], lst, total)
        else: 
            break
    print(lst, total)
    total += 1

print(total)