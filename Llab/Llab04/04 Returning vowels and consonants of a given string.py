charactor = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
text = input("Enter a string: ").strip().replace(" ", "")

vowels = ['a','e','i','o','u']
vowels_rst = []
consonants_rst = []

for i in text:
    i = i.lower()
    if i not in charactor:
        continue
    if i in vowels and i not in vowels_rst:
        vowels_rst.append(i)
    if i not in vowels and i not in consonants_rst:
        consonants_rst.append(i)

print(f"Unique vowels:  {vowels_rst}")
print(f"Unique consonants:  {consonants_rst}")

