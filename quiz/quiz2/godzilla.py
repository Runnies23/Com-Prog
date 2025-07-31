n = 5

matrix = [
    [3,3,3,3,3],
    [3,2,2,2,3],
    [3,2,1,2,3],
    [3,2,2,2,3],
    [3,3,3,3,3]
]

seq = "E"

def north(): #up to down 
    for i in range(n):
        for j in range(n):
            if matrix[j][i] > 0 :
                matrix[j][i] -= 1
                break

def west(): #left to right
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0 :
                matrix[i][j] -= 1
                break

def south(): #down to up
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if matrix[j][i] > 0 :
                matrix[j][i] -= 1
                break


def east(): #right to left
    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            if matrix[i][j] > 0 :
                matrix[i][j] -= 1
                break

for direction in seq:
    match direction.upper():
        case "N":
            north()
        case "S":
            south()
        case "W":
            west()
        case "E":
            east()
        case _ :
            pass

for i in matrix:
    for j in i:
        print(j,end=" ")
    print()