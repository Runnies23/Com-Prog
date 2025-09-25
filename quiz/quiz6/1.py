#merge 2 sorted list 
# Python if compare the text it's will compare on the string as well (it mean code is not matter to write proirity on sort with text or charactor - write like a number)

a = [1,2,3,4,5,6]
b = [4,5,7,8,10]

a = ['A','a','b']
b = ['M',"n"]

#Method 1 selection sort (merge then sort) #struct 1 case left 


#Method 2 Merge sort (Just only merge - not divide) #My friend (Mark did it and pass)
idx_a = 0
idx_b = 0

rst_lst = []

while idx_a < len(a) and idx_b < len(b):
    value_a = a[idx_a]
    value_b = b[idx_b]

    if value_a <= value_b:
        rst_lst.append(value_a)
        idx_a += 1
    else: 
        rst_lst.append(value_b)
        idx_b += 1 

if idx_a < len(a):
    rst_lst.append(a[idx_a:])

elif idx_b < len(b):
    rst_lst = rst_lst + b[idx_b:]

print(a[idx_a:], b[idx_b:])
print(rst_lst)