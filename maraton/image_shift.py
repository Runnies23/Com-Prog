horizontal = 3
vertical = 2

text ="""
tttttttttttttt
tt----tt----tt
tt----tt----tt
tt----tt----tt
tttttttttttttt
tttttttttttttt
tttttt--tttttt
tttttttttttttt
tttttttttttttt
""".strip().split("\n")

# print(text)
lst = []

image_height = len(text)
image_width = len(text[0])

if horizontal > 0:
    for i in text:
        
        lst.append(("0" * horizontal) + i[:-horizontal])
else:
    for i in text:
        lst.append(i[-horizontal:] + ("0" * abs(horizontal)))
    

rst = []
if vertical > 0:
    for i in range(image_height):
        if i < vertical:
            rst.append("0" * image_width)
        else:
            rst.append(lst[i-vertical])
else: 
    # print(lst)
    rst = lst[:vertical]
    for i in range(abs(vertical)):
        rst.append("0" * image_width)
    

for i in rst:
    print(i)