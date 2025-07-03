
text = input("Enter a message: ")
for index, char in enumerate(text):
    print(" " * index,end="")
    print(char)