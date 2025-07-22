# x = "()[]{}"
# x = input("input: ")

# while "{}" in x or "[]" in x or "()" in x:
#     x = x.replace("{}",'').replace("[]",'').replace("()","")

# print(x)
# if "{" not in x and "[" not in x and "(" not in x and "}" not in x and ")" not in x and "]" not in x:
#     print("valid parentheses")
# else:
#     print("invalid parentheses")

text = input("input: ")
paren_map = {
    ")" : "(",
    "}" : "{",
    "]" : "["
}

stack = []

#replace the word in the Stringh forat
status = False

new_text = ""
for i in text:
    if status:
        if i in """"'""":
            status = False
    else: 
        if i not in """"'""":
            new_text += (i)
        else: 
            if i in """"'""":
                status = True


for i in new_text:
    if i in paren_map.keys():
        x = stack.pop(-1)
        if x != paren_map[i]:
            print('invalid parentheses')
            break
    elif i in paren_map.values():
        stack.append(i)

else:
    if stack:
        print('invalid parentheses')
    else:
        print("valid parentheses")



# while ("{" in x or "[]" in x or "()"  in x or " " in x): pass