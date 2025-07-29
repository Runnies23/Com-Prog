rows = int(input("Enter Rook's row position: "))
column = int(input("Enter Rook's column position: "))
n = 8
rows_fill = [" "] * 8
rows_fill[column] = "x"

rows_specific = ["x"] * 8
rows_specific[column] = "R"

def split():
    print("-----------------")

for i in range(n):
    split()
    print("|",end="")
    if i == rows:
        print("|".join(rows_specific),end="")
    else: 
        print("|".join(rows_fill),end="")
    print("|")
    

split()