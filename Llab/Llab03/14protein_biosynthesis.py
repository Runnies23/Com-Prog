text_input = input('DNA: ')

change_seq = {
    "A" : "U",
    "C" : "G",
    "G" : "C",
    "T" : "A"
}

new_seq = ""
for char in text_input:
    if char in change_seq:
        new_seq += change_seq[char]
    else: 
        new_seq += char
del text_input


# AUG 
# GCAGCAGGAUGUCGUACUCGUAGUAGUCGGGUAACAGUACG

stop_dna = ['UAA','UGA','UAG']
# print(new_seq)
start = 0
for i in range(len(new_seq) - 2):
    if new_seq[i] == "A" and new_seq[i+1] == "U" and new_seq[i+2] == "G":
        start = i + 3
        break
# print(start)
# print(new_seq[start:])

count = 1
for i in range(start, len(new_seq), 3):
    dna = new_seq[i:i+3]
    # print(dna)
    if dna not in stop_dna:
        count += 1
    else:
        break
print(f"{count} Amino acid(s)")