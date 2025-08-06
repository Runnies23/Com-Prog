target = 10
array = [8,4,6,7,9,1,2,10,3,5]

from linear_search import Linear_search
from binary_search import Binary_search, Binary_search_recursive
from jump_search import Jump_search


print(array, target)
array.sort()
print(Linear_search(array=array,target=target))
print(Binary_search(array=array,target=target))
print(Binary_search_recursive(array=array,target=target))
print(Jump_search(array=array,target=target,jump_step=2))