n = int(input("Enter factorial : "))

if n < 1:
    rst = 1
else: 
    rst = n

print(f"> fac({n})")

text = [f" {n}"]
for i in range(n - 1, -1, -1):
    text.append(f"fac({i})")
    if i == 0:
        print("1")
    else: 
        print(" * ".join(text))
    text.remove(f"fac({i})")
    if i == 0:
        text.append(str(1))
        break
    text.append(str(i))
    rst *= i

# text.append(str(i))
print(" * ".join(text))

print(">",rst)
