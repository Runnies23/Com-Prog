labels = """a b c d e f g h i j k l m n o p q r s t u v w x y z""".split(" ")
labels2id = {labels : index for index, labels in enumerate(labels)}
id2labels = {index : labels for index, labels in enumerate(labels)}

result = ""
text = input("Enter text: ")
step = int(input("Enter step: "))

for char in text:
    if char.lower() in labels:
        char_add = id2labels[(labels2id[char.lower()] + step) % 26]
        if char.isupper():
            char_add = char_add.upper()

        result += char_add
        # print(result)
    else: 
        result += char

print(result)