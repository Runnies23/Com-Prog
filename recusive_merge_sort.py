lst1 = [1,2,4]
lst2 = [1,3,4]


def merge_sort(lst1,lst2):

    print(lst1, lst2)
    if lst1 and not lst2:
        return lst1
    elif lst2 and not lst1:
        return lst2

    if lst1[0] <= lst2[0]:
        return [lst1[0]] + merge_sort(lst1[1:], lst2)
    else:
        return [lst2[0]] + merge_sort(lst1, lst2[1:])

print(merge_sort(lst1,lst2))