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
stack = []

smth = {
    '}' : "{",
    "]" : "[",
    ")" : "("
}

for i in text:
    if i in "([{}])":
        if i in smth.keys() and stack:
            if smth[i] == stack[-1]:
                stack.pop()
            else:
                break
                print('invalid parentheses')
        else: 
            stack.append(i)
            # print(f"Add : {stack}")

if len(stack) == 0: print('valid parentheses') 
else: print("invalid parentheses")