#Score Grading


hw = float(input("Enter the homework percentage: "))
mid = float(input("Enter the midterm percentage: "))
final = float(input("Enter the final percentage: "))

total_score = (hw * 0.2) + (mid * 0.4) + (final * 0.4)

print(f"Total score: {total_score:.2f}")
if total_score <= 100 and total_score > 0:
    if total_score >= 80:
        print("You receive the grade A")
    elif total_score >= 75:
        print("You receive the grade B+")
    elif total_score >= 70:
        print("You receive the grade B")
    elif total_score >= 65:
        print("You receive the grade C+")
    elif total_score >= 60:
        print("You receive the grade C")
    elif total_score >= 55:
        print("You receive the grade D+")
    elif total_score >= 50:
        print("You receive the grade D")
    else:
        print("You receive the grade F")
else:
    print (f"total_score {total_score} out of range!")

