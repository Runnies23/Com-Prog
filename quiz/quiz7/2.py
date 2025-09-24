#recursive function Krub P Nong

def find(lst, target):
    for i in lst:
        if isinstance(i, list):
            if find(i, target):
                return True
        elif i == target:
            return True

    return False


# mylst = eval(input("Enter List: "))
# target = int(input("Enter Target: "))

mylst = [1,[2,3,[4,5,[6]]]]
target = 20

print(find(mylst, target))

# type(i) == list