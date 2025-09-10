width = 4 
amount = 3
lenght = width * 2 - 1

for i in range(lenght):
    for j in range(amount):
        space = (abs(lenght - (i * 2 + 1))// 2)    
        print(" " * space,end="")  
        print("*" * ((width - space) * 2 -1) ,end="")
        print(" " * space,end="")  

        print(" ",end="")
        
    print()