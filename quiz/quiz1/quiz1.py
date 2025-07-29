

map_to_char = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
out_of_range = [0,1, -1, 17]

def base(nums:int=-2025, base_num:int=2):
    first_num = abs(nums)
    result = ""
    while True: 
        if first_num != 0:
            rsl = int(first_num % base_num)
            if rsl >= 10:
                rsl = map_to_char[rsl]
            result = str(rsl) + result
            first_num = int(first_num / base_num)
        else:
            break
    if nums <= 0:
        result = "-"+ result
    return result


Nums = int(input("N: "))
while True:
    base_convert = int(input("Base to convert: "))
    if base_convert <= 0 or base_convert in out_of_range or base_convert > 16:
        break
    print(base(Nums, base_convert))