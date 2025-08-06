"""
Jump Search is a searching algorithm for sorted arrays
check fewer elements (than linear search) by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
"""


def Jump_search(array,target,jump_step:int=2):
    index = 0
    while True:
        if index >= len(array):
            if array[-1] == target:
                return True
            else:
                return False

        if array[index] == target:
            return True
        elif array[index] < target:
            index += jump_step
        elif array[index] > target:
            index -= jump_step
            jump_step -= 1