# 1 1 2 2 3 3 4 4 -> 6
# 1 2 4 3 3 -> 4 

lst = [1,4,2,3,3]
n = 4

# lst = [1,1,2,3,4,4,2,3]
# n = 6
total = 0

lst.sort()
lst.reverse()

while len(lst) > 0:
    # print(lst)
    sm = lst[0]
    lst.pop(0)
    idx = len(lst) - 1
    # print(sm)
    while idx >= 0:
        if sm + lst[idx] <= n:
            sm += lst[idx]
            lst.pop()
            idx -= 1
        else: 
            break
    total += 1

print(total)