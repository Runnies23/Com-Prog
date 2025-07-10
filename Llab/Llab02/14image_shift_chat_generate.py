
horizontal = int(input("Enter horizontal shift size: "))
vertical = int(input("Enter vertical shift size: "))
padding_text = "0"

# Get image input
print("Enter image:")
text_image = []
while True:
    line = input()
    if line == "-1":
        break
    text_image.append(line)

# Get original dimensions
height = len(text_image)
width = len(text_image[0]) if height > 0 else 0

# Shift vertically
if vertical >= 0:
    new_image = [padding_text * width for _ in range(vertical)] + text_image[:height - vertical]
else:
    new_image = text_image[-vertical:] + [padding_text * width for _ in range(-vertical)]

# Shift horizontally
shifted_image = []
for row in new_image:
    if horizontal >= 0:
        new_row = (padding_text * horizontal) + row[:width - horizontal]
    else:
        new_row = row[-horizontal:] + (padding_text * (-horizontal))
    shifted_image.append(new_row)

# Print result
print("After shift:")
for row in shifted_image:
    print(row)
