def bubble_sort(array):

    swap_status = True
    time = 0 
    n = len(array)

    while swap_status and time < n:

        index = 0
        total_swap = 1

        while index < len(array) - 1:

            if array[index] > array[index + 1]:
                # print("Swap")
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
            else: 
                total_swap += 1

            index += 1
            # print(f"Mini swaq :", array)

        # print("total ",total_swap)
        # print("New Interation :", array)
        if total_swap == n:
            swap_status = False

        time += 1

    return array