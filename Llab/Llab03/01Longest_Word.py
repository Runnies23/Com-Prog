x = input("Enter your sentence: ").split()
dict_ = dict()

for i in x:
    if i.lower()[0] not in dict_:
        dict_[i.lower()[0]] = i
    else:
        if len(i) > len(dict_[i.lower()[0]]):
            dict_[i.lower()[0]] = i

for key, value in dict_.items():
    print(f"{key.upper()}: {value}")