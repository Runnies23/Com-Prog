# nums = 7
nums = int(input())

if nums % 2 != 0:
    for i in range(nums):
        space = (abs(nums - (2*i+1)) // 2 )
        text_ = ((nums // 2) - abs((nums - (2*i+1))//2) + 1) * 2 -1
        # print(text_)

        print(" " * space,end="")
        print("#" * text_,end="")
        print()
else:
    print("Odd nums")