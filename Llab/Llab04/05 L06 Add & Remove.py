init_list = [int(i) for i in input().split()]

while True:
    ope, val = input().split()
    val = int(val)
    if ope == "E":
        break
    match ope:
        case "A":
            init_list.append(val)
            #print(init_list)
        case "S":
            print(init_list[val])
        case "R":
            init_list.pop(val)
            
for i in init_list:
    print(i,end=" ")
