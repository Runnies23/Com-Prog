file = """
alice,2025-08-01 09:10,2025-08-01 11:45
Bob,2025-08-01 08:00,2025-08-01 08:30
Carol,2025-08-01 12:00,2025-08-01 17:00
david,2025-08-01 10:15,2025-08-01 13:00
ellen,2025-08-01 14:00,2025-08-01 18:45
Alice,2025-08-01 07:30,2025-08-01 07:31
Grace,2025-08-02 12:23,2025-08-02 12:30
Carol,2025-08-02 11:00,2025-08-02 20:10
""".strip().split("\n")

# file_name = input("Enter the session file: ")
# file = open(file_name).read().splitlines()
# file = [i for i in file if i != ""]

def process_str_to_date_time(s):
    """
    This function gets the string and returns the date and time as lists
    """
    date, time = s.split(" ")
    date = list(map(int, date.split("-")))
    time = list(map(int, time.split(":")))
    return date, time

def duration(start: str, end: str) -> int:
    """
    Calculate the duration in minutes between two datetime strings.
    """
    start_date, start_time = process_str_to_date_time(start)
    end_date, end_time = process_str_to_date_time(end)

    # This condition calculates the duration only if dates match or end is after start
    if start_date[2] <= end_date[2]:
        if (start_date[2] == end_date[2]) and (
            end_time[0] > start_time[0] or 
            (end_time[0] == start_time[0] and end_time[1] > start_time[1])
        ):
            hour = end_time[0] - start_time[0]
            mins = end_time[1] - start_time[1]
        elif start_date[2] < end_date[2]:
            days = end_date[2] - start_date[2]
            hour = (end_time[0] + (days * 24)) - start_time[0]
            mins = end_time[1] - start_time[1]
        else:
            hour = 0
            mins = 0

        total_mins = hour * 60 + mins
        return total_mins
    else:
        return 0

Employee_dict = dict()

for i in file:
    name, start, end = i.split(",")
    if name.lower() in Employee_dict:
        Employee_dict[name.lower()] += duration(start,end)
    else:
        Employee_dict[name.lower()] = duration(start,end)

set_of_dict = Employee_dict.values()
max_val = max(set_of_dict)
min_val = min(set_of_dict)

lst_max = []
lst_min = []

for key, value in Employee_dict.items():
    if value == max_val:
        lst_max.append(key)
    if value == min_val:
        lst_min.append(key)

print("Shortest session:")
for i in lst_min:
    print(f"- User: {i.capitalize()}, Duration {min_val} minutes")

print()
print("Longest session:")
for i in lst_max:
    print(f"- User: {i.capitalize()}, Duration {max_val} minutes")

while True:
    name_inspect = input("Type the username to observe session time: ")
    if name_inspect == "":
        print("Exiting...")
        break

    if name_inspect.lower() in Employee_dict:
        print(f"{name_inspect.capitalize()} was logged in for a total of {Employee_dict[name_inspect.lower()]} minutes.")
    else:
        print(f"No sessions found for '{name_inspect}'. Please try again.")
