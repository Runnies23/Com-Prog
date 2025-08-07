n = 5
rst = []


"""
1 2 3 4 5
5 4 3 2 1
6 7 8 9 0 
0 8 6 5 4
3 4 5 6 7
"""

for _ in range(n):
    rst.append(list(map(int, input().split(" "))))
print(rst)