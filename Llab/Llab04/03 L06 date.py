date = int(input("d: "))
month = int(input("m: "))
year = int(input("y: "))

year_lst = [31,28,31,30,31,30,31,31,30,31,30,31]

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    allday = 366
    year_lst[1] = 29
else:
    allday = 365
    
summ = 0    
for index, value in enumerate(year_lst):
    if index == month-1:
        break
    summ += year_lst[index]
    #print(summ, index)
    
summ += date
print(summ)
