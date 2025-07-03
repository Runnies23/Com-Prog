def multiply(num):
    i = 1
    while i < 13:
        print(f"{num} x {i} = {num * int(i)}")
        i += 1
    return 

status = True
while status:
    nums = input("Specify N (or just ENTER to quit): ")
    if nums == "":
        status = False
    else:
        multiply(int(nums))
