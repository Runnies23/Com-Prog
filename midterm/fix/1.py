depth = 0 

print(f"Submarine start at {depth} m")
while True:
    target = input("Target : ")
    if target.lower() == "quit":
        print("Simulated End")
        break
    target = int(target)
    if target == depth:
        print(f"Already at {depth}")
        continue

    if target > 500 or target < 0 :
        print("Invalid range input")
        continue
    
    while target != depth:
        if target > depth:
            if abs(depth - target) > 50:
                depth += 50
                print(f"Accessing to Depth {depth} m")
                continue
            else: 
                depth = target
                print(f"Accessing to Depth {depth} m")
                break

        elif target < depth:
            if abs(depth - target) > 50:
                depth -= 50
                print(f"Decessing to Depth {depth} m")
                continue
            else:
                depth = target
                print(f"Decessing to Depth {depth} m")
                break

    if target == depth:
        print(f"React the target {depth} m")

    