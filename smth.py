def getMultilinesInput():
    text = ""
    while True:
        line = input()
        if not line:
            break
        text += line + ' '
    return text

print("Parse a long paragraph (or text) below, following an ENTER as needed:")
ss = getMultilinesInput()

cleaned_text = ''
for ch in ss:
    if ch.isalpha():
        cleaned_text += ch.lower()
    else:
        cleaned_text += ' '

words = cleaned_text.split()
k = int(input("Top K rank: "))

num = {}
for word in words:
    if word in num:
        num[word] += 1
    else:
        num[word] = 1

sorted_items = sorted(num.items(), key=lambda x: x[1], reverse=True)

rank = 0
i = 0
while rank < k and i < len(sorted_items):
    current_count = sorted_items[i][1]
    same_count_words = []

    while i < len(sorted_items) and sorted_items[i][1] == current_count:
        same_count_words.append(sorted_items[i][0])
        i += 1

    same_count_words.sort()

    if len(same_count_words) == 1:
        print(f"{same_count_words[0]}: {current_count}")
    else:
        output_parts = []
        for word in same_count_words:
            output_parts.append(f"{word}: {current_count}")
        print(", ".join(output_parts))

    rank += 1