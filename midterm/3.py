
#two pointer
array = [-1,0,1,2,-1,-4]
# array = []

array.sort()

answer_lst = []
left = 0
while left < len(array):
    right = len(array) - 1
    mid = left + 1
    while right > 0 and left < mid < right: 
        leftv, midv, rightv = array[left], array[mid], array[right]
        sums = leftv + midv + rightv
        if sums == 0:
            tuple_val = tuple((leftv, midv , rightv))
            if tuple_val not in answer_lst:
                answer_lst.append(tuple_val)
        if sums < 0:
            mid += 1 
        else: 
            right -= 1
    left += 1

print(answer_lst)