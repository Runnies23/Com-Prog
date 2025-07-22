current_time = [int(i) for i in input("Input current time: ").split(":")]
nap_time =  int(input("Input nap time: "))
snooze_time = int(input("Input snooze time: "))

# current_time =[int(i) for i in "00:00".split(":")]
# nap_time =  3
# snooze_time = 2

def print_and_add(time):
    global current_time
    for _ in range(time):

        current_time[1] += 1

        if current_time[1] == 60:
            current_time[0] += 1
            current_time[1] = 0

        if current_time[0] == 24:
            current_time[0], current_time[1] = 0,0
        print(f"{current_time[0]:02d}:{current_time[1]:02d}")

print('Nap time starts.')
print_and_add(nap_time)

status = "Snooze"
while status != "Dismiss":
    status = input("Alarm rings. Dismiss or Snooze: ")
    if status == "Dismiss":
        continue
    print_and_add(snooze_time)

        

