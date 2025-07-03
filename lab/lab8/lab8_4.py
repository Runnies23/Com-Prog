status = True 

list_of_nums = []
while status:
        
    input_val = input("Enter a number (to quit, just [Enter]): ")
    if input_val == "":
        status = False
    else:
        list_of_nums.append(float(input_val))

if len(list_of_nums) == 0:
    print("Nothing to do.")
else:
    print(f"Maximum is {max(list_of_nums):.2f}")
    print(f"Minimum is {min(list_of_nums):.2f}")
    print(f"Average is {(sum(list_of_nums)/len(list_of_nums)):.2f}")