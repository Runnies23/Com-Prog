#Is it a Leap Year?

def cal_leap_year(year):
    if year < 1751:  #
        if year % 4 == 0:
            return True
    else: 
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            return True
    return False

years = int(input("Enter year in AD: "))

if years > 0:
    if cal_leap_year(years):
        print(f"The year {years:d} (AD) is a leap year")
    else: 
        print(f"The year {years:d} (AD) is not a leap year")
else: 
    print("Invalid input: input year must be a positive integer")
    