map_to_char = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"] #-> Z

def map_base(nums, base):
    txt = ""
    while nums > 0:
        char = nums % base
        txt =  str(map_to_char[char %len(map_to_char) ]) + txt
        nums //= base
    return txt


nums = int(input())
while True:
    convert_nums = int(input())
    if convert_nums == 0:
        break

    rst = map_base(nums, convert_nums)
    print(rst)
    