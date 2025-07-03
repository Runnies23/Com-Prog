score = int(input("What's your math's score (0-100): "))
if score <= 100 and score > 0:
    if score >= 80:
        print("You got {A}.")
    elif score >= 70:
        print("You got {B}.")
    elif score >= 60:
        print("You got {C}.")
    elif score >= 50:
        print("You got {D}.")
    else:
        print("You got {F}.")
else:
    print (f"Score {score} out of range!")