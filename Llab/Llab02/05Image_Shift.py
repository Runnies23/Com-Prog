
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

#add image padding on vertical 
new_image = ["0" * image_detail_h_w[1] for _ in range(vertical)]
#add image padding on horizontal
for rows in text_image[:-vertical]:
    new_image.append(("0" * horizontal) + rows[:-horizontal])

print("After shift:")
#print the padding image text
for i in new_image:
    print(i)