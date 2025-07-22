file_path = input("File name: ")

most_score = -99
name_lst = []

data = open(file_path).read().split("\n")

for i in data:
    temp = i.split(" ")
    name, score = temp[0], [int(k) for k in temp[1:]]
    # print(score)
    max_score, min_score = max(score), min(score)
    # print(f"max : {max_score}, min : {min_score}")
    score.remove(max_score)
    score.remove(min_score)
    total = sum(score)
    if total > most_score:
        most_score = total
        name_lst = [name]
    elif total == most_score:
        name_lst.append(name)

print(most_score)
for i in name_lst:
    print(i)