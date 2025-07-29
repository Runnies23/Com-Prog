# def commaCode(myList):
#     if len(myList) == 0:
#         return ''
#     elif len(myList) == 1:
#         return myList[0]
#     else:
#         myList[-1] = "and " + myList[-1]
#     return ", ".join(myList)

def commaCode(myList):
    if len(myList) == 0:
        return ''
    elif len(myList) == 1:
        return myList[0]
    else:
        myList[-1] = myList[-2] + " and " + myList[-1]

    rst = ""
    for i in myList[:-2]:
        rst = rst + i + ", "
    rst += myList[-1]
    return rst


s = input("Input: ").split()
r = commaCode(s)
print(r)