

def selection_sort(array):
    """
    Selection Sort 
    - repeatedly selecting the smallest (or largest) element from the unsorted portion and swapping it with the first unsorted element.
    """

    for i in range(0,len(array)):
        smallest = array[i]
        smallest_position = i
        for j in range(i,len(array)):
            if smallest > array[j]:
                smallest = array[j]
                smallest_position = j

        temp = array[i]
        array[i] = smallest
        array[smallest_position] = temp
        del temp

    return array