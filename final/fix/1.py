"""
input 
Name Severity Time 
20character int:1-5 str(HH:MM)

sort by nums of severity -> time -> Name (first character)
"""

order_dict = {}
count = 1

rst = []
while True:
    input_txt = input(f"Order #{count} : ")
    if input_txt == "":
        break
    name, severity, time = input_txt.split(" ")
    severity = int(severity)
    order_dict[name] = [severity, time]

#sort by severity
sorted_severity = []
for i in reversed(range(1,6)):
    local = []
    for key,value in order_dict.items():
        if value[0] == i:
            local.append(value,key)
    
    sorted_severity.append(local)
    
for i in (sorted_severity):
    # not finish (kinda lazy )