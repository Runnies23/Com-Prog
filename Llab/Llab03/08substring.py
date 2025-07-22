text = input("Text: ")
string = input('Substring: ')

if string in text:
    text = text.replace(string,f"[{string}]")
    print(text)
else: 
    print("Not found")