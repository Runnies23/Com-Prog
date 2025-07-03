status = True
data = []

while status:
    input_value = input("Enter score (or ENTER to finish): ")
    if input_value == "":
        status = False
    else:
        data.append(int(input_value))

for index,item in enumerate(data):
    print(f"Student #{index+1} score: {item}")

print(f"""Average score is {(sum(data)/len(data)):.2f}
Minimum score is {min(data)}
Maximum score is {max(data)}
""")