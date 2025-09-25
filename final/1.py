#regx 
# pattern - string
# lowercase 
# . 
# * 

def regx(text: str, pattern: str) -> bool:
    if not pattern:
        return not text

    first_match = bool(text) and pattern[0] in {text[0], "."}

    if len(pattern) >= 2 and pattern[1] == "*":
        return (
            regx(text, pattern[2:])
            or first_match
            and regx(text[1:], pattern)
        )
    else:
        return first_match and regx(text[1:], pattern[1:])
    
mystr = input("Enter string : ")
pattern = input("Enter Pattern : ")

# mystr = "aab"
# pattern = "c*a*."

print(regx(mystr, pattern))