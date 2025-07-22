# # # val = "1, 3, 5, 7, 9, 11, 13, 15, 17, 19"
# # # target = 7
# # # val = "2, 4, 6, 8, 10, 12, 14, 16, 18, 20"
# # # target = 16

# val = input("ข้อมูล: ")
# target = int(input("ค่าที่ต้องการหา: "))

# val = [int(i) for i in val.split(", ")]

# n = len(val)

# total = 0
# l = 0
# r = n - 1
# while l <= r:
#     total += 1
#     print(val[l:r])
#     mid = (l + r) // 2
#     item = val[mid]
#     if item == target:
#         print(f"จำนวนครั้งที่ค้นหา: {total}")
#         break
#     if item > target:
#         r = mid - 1
#     else: 
#         l = mid + 1



# Labels ===================================
# def bs(k:int, m:list, c=0):
#     mid = len(m) // 2
#     c +=1 
#     print(f"Debug : bs({k},{m},{c})")
#     if m[mid] == k: return c #base case

#     if k > m[mid] : return bs(k, m[mid+1:],c)
#     return bs(k,m[:mid],c)

# count = bs(7, [1, 3, 5, 7, 9, 11, 13, 15, 17, 19])
# print(count)

# k, m = 16, [2,4,6,8,19,12,14,16,18,20]
# count = bs(k,m)
# print(count)
# Labels ===================================


def recursive_binary(target, array, left:int = 0, right=None, count:int=0):
    if right is None: 
        right = len(array) - 1

    middle = (left+right)//2
    middle_val = array[middle]
    if middle_val == target:
        return count + 1
    if middle_val > target:
        return recursive_binary(target, array, left, middle-1, count + 1)
    else: 
        return recursive_binary(target, array, middle + 1, right, count + 1)

val = input("ข้อมูล: ")
target = int(input("ค่าที่ต้องการหา: "))

val = [int(i) for i in val.split(", ")]

print(f"จำนวนครั้งที่ค้นหา: {recursive_binary(target=target, array=val)}")