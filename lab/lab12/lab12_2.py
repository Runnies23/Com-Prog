file_name = input('Enter file name: ')
data = list(map(float, [i for i in open(file_name).read().splitlines() if i != ""]))

mean = sum(data) / len(data)
print(f"""Size of the data set is {len(data)}
Minimum is {min(data):.2f}
Maximum is {max(data):.2f}
Mean is {mean:.2f}""")

std = [abs(i - mean)**2 for i in data]
# std /= (len(data)-1)
print(f"Standard deviation is {((sum(std)/(len(data)-1))**0.5):.2f}")