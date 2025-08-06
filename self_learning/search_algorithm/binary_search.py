def Binary_search(array, target):
    array.sort()

    left, right = 0, len(array)-1
    while left <= right:
        middle = (left+right) // 2
        # print(array[left:right])   #=== Debug
        # print(middle)              #=== Debug
        if array[middle] == target:
            return True
        elif array[middle] > target:
            right = middle - 1
        else: 
            left = middle + 1

    return False


def Binary_search_recursive(left:int=0, right:int=None, array:list=None, target:int=None):
    if right == None:
        right = len(array)-1
    # print(array[left:right], target, left, right)
    
    if left > right:
        return False

    middle = (left + right)//2
    if array[middle] == target:
        return True
    elif array[middle] > target:
        rst = Binary_search_recursive(left, middle - 1, array,target)
    else:
        rst = Binary_search_recursive(middle + 1, right,array,target)

    return rst
    