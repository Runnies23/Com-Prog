#first name last name with out repeat 

store = []

while True:
    text = input("Enter Name :")
    if text == "":
        break
    text = text.split()
    if len(text) != 2:
        print("Invalid")
    
    first_name, last_name = [i.lower() for i in text]
    idx = 1
    gmail = f"{first_name}.{last_name[:idx]}@ku.th"
    while gmail in store:
        if idx > len(last_name):
            break
        gmail = f"{first_name}.{last_name[:idx]}@ku.th"
        idx += 1    
    
    print(f"KU gmail : {gmail}")
    store.append(gmail)

    # print(gmail)