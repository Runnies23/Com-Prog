a = int(input())
b = int(input())
c = int(input())

lst = [a,b,c]
max_val = max(lst)
min_val = min(lst)
normal_val = [i for i in lst if i != max_val and i != min_val][0]

print(min(lst), normal_val, max(lst))