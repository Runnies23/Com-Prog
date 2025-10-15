
def matching(string, pattern):
    if not pattern:
        return not string

    
    print(string, pattern)


    if pattern[0] == "*" and bool(string):
        #case of empty and still doing 
        return matching(string[1:],pattern) or (matching(string, pattern[1:]) and bool(string))


    if bool(string) and (string[0] == pattern[0]) or (pattern[0] == "?"):
        return matching(string[1:],pattern[1:])

    return False

# text = "aa"
# pattern = "a"


# text = "aba"
# pattern = "ab?aaa"

text = "aac"
pattern = "*"

print(matching(text,pattern))