n,m = list(map(int, input("City Size: ").split(" ")))
# City = """2 3 5 6 2
# 1 3 4 7 1
# 6 5 4 1 3
# 2 3 7 9 6"""

City = [input() for _ in range(n)]
City = [list(map(int, i.split())) for i in City]
# print(City)

#West top to down 
count_west = 0
count_East = 0
count_north = 0
count_south = 0
for i in range(n):
    recent_west = 0
    for j in range(m):
        if City[i][j] > recent_west:
            count_west += 1 
            recent_west = City[i][j]

    recent_East = 0
    for j in range(m-1,-1,-1):
        if City[i][j] > recent_East:
            count_East += 1 
            recent_East = City[i][j]


for j in range(m):
    recent_north = 0
    for i in range(n):
        if City[i][j] > recent_north:
            count_north += 1 
            recent_north = City[i][j]

    recent_south = 0
    for i in range(n-1,-1,-1):
        if City[i][j] > recent_south:
            count_south += 1 
            recent_south = City[i][j]

rst = []

most = max([count_west,count_East,count_north,count_south])
#N S E W
if count_north == most:
    rst.append("N")    

if count_south == most:
    rst.append("S")    

if count_East == most:
    rst.append("E")    

if count_west == most:
    rst.append("W")    

print(' '.join(rst))
