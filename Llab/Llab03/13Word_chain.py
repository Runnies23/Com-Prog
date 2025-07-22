seq_text = input("Text: ").split(' ')

def count_2_text(txt1, txt2, lenght):
    count = 0
    for i in range(lenght):
        if txt1[i] == txt2[i]:
            count += 1
    # print("Count :", count)
    return count > lenght - 3

chain_count = 1
Max_lenght = 0
temp = 1
n = len(seq_text[0])

for index in range(0, len(seq_text)-1):
    current = seq_text[index]
    next_index = index + 1
    next_val = seq_text[index+1]

    # print(f"Current : {current}, Next : {next_val}")

    if count_2_text(current, next_val, n):
        # print("add Lenght")
        temp += 1
    else: 
        # print("new Chain")
        Max_lenght = max(Max_lenght, temp)
        chain_count += 1
        temp = 1

Max_lenght = max(Max_lenght, temp)
print(f"{chain_count} Chain(s). Maximum length is {Max_lenght} word(s).")