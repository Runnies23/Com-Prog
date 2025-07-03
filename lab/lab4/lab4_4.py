# Please enter your weight (in kg): 75
# Please enter your height (in cm): 175
# Your BMI: 24.49


def BMI(weight, height):
    height /= 100 
    bmi = weight / (height  * height)
    return bmi

weight = float(input("Please enter your weight (in kg): "))
height = float(input("Please enter your height (in cm): "))
print(f"Your BMI: {BMI(weight,height):.2f}")