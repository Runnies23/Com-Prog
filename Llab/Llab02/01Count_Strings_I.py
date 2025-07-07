#Count Strings I


"""
Count Strings I
Count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.

Requirements
You MUST define a function countStr(m) that return the resulting number of strings that satisfy the above requirement, when m is a list of strings.

Example
Enter a set of strings: abc xyz aba 1221
2
Enter a set of strings: aa bab cca 1ds1
3
Example (shell mode)
>>> countStr(['abc','xyz','aba','1221'])
2
"""

def countStr(strs):
    lst = [i for i in strs if i[0] == i[-1]]
    return len(lst)

text = input().split()
print(countStr(text))