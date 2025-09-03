width = 4 
amount = 3
lenght = width * 2 - 1

for i in range(lenght):
    for j in range(amount):
        if j % 2 == 0:
            space = (abs(lenght - (i * 2 + 1))// 2)    
            print(" " * space,end="")  
            print("*" * ((width - space) * 2 -1) ,end="")
            print(" " * space,end="")  
        else: 
            space = (abs(lenght - (i * 2 + 1))// 2) + 1   
            print("*" * space,end="")  
            print(" " * ((width - space) * 2 -1) ,end="")
            if i == 0 or i == lenght - 1:
                print("*" * (space - 1),end="")  
            else: 
                print("*" * space , end="")
        
    print()