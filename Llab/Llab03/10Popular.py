nums = input("Input number of words: ")
name = [input() for _ in range(int(nums))]
frequency = dict()

for i in name:
    first_char = i[0].lower()
    if first_char not in frequency:
        frequency[first_char] = 1
    else:
        frequency[first_char] += 1

max_name = max(frequency.values())
for key, value in frequency.items():
    if value == max_name:
        word = key

print(f"The popular character is {word}.")
print(f"The character is used in {max_name} words.")
print("\n".join([i for i in name if i[0] == word]))