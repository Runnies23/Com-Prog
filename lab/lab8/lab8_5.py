depth = int(input("Enter the depth of the well: "))
high = int(input("How high the frog can jump up? "))
far = int(input("How far the frog slips down? "))

def function(depth,high,far):
    if high > far and depth > high:
        index = 1
        while depth > 0:
            depth -= high
            if depth <= 0:
                return True, index
            print(f"On day {index} the frog leaps to the depth of {depth} meters.")
            depth += far
            print(f"At night he slips down to the depth of {depth} meters.")
            index += 1
        
    else:
        print("The frog will never escape from the well.")
        return False, None
result = function(depth,high,far)
if result[0]:
    print(f"The frog is free on day {result[1]}.")