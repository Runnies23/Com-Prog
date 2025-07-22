print("Parse a long paragraph (or text) below, following an ENTER as needed:")

count_dict = dict()
status = True
text = []
while status:
    raws = input()
    if raws == "":
        status = False
        break
    text.append(raws)

topk = int(input('Top K rank: '))

text = " ".join(text).lower()#.replace(',','')
text = text.split(' ')

for i in text:
    if i not in count_dict:
        count_dict[i] = 1
    else: 
        count_dict[i] += 1

for i in sorted(set(count_dict.values()))[::-1][:topk]: #o n^2
    text = []
    for key, value in count_dict.items():
        if value == i:
            text.append(f"{key}: {value}")
    print(", ".join(text))