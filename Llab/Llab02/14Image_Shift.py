# missing case shift minus like -1, -2 

horizontal = int(input("Enter horizontal shift size: "))
vertical = int(input("Enter vertical shift size: "))
padding_text = "0"

#get image input 
print("Enter image: ")
text_image = []
status = True
while status:
    input_text = input()
    if input_text == '-1':
        status = False
        continue
    text_image.append(input_text)

#detail about size image that is width and height
image_detail_h_w = [len(text_image), len(text_image[0])]

if vertical >= 0:
    new_image = [padding_text * image_detail_h_w[1] for _ in range(vertical)] + text_image[:image_detail_h_w[0] - vertical]
else:
    new_image = text_image[-vertical:] + [padding_text * image_detail_h_w[1] for _ in range(abs(vertical))]

result_image = []
if horizontal >= 0:
    for rows in new_image:
        result_image.append((padding_text * horizontal) + rows[:image_detail_h_w[1] -horizontal])
else: 
    for rows in new_image:
        result_image.append(rows[-horizontal:] + (padding_text * abs(horizontal)))

print("After shift:")
#print the padding image text
for i in result_image:
    print(i)
