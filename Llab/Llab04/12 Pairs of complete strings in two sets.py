charactor = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")
string_1 = eval(input("String set1: "))
string_2 = eval(input("String set2: "))

rst = []


for i in string_1:
    for j in string_2:
        count = []
        text = i + j
        for char in text:
            if char in charactor and char not in count:
                count.append(char)
        if len(count) == 26:
            rst.append(text)
            
print(f"Output: {len(rst)}")
print("The total complete pairs that are forming are:")

for i in rst:
    print(f" {i}")
        
        
        
