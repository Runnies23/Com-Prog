#Weight Status 

def cal_BMI(weight, height):
    if height > 100:
        height /= 100
    return weight / (height * height)

weight = float(input("What is your weight (kg)? "))
height = float(input("What is your height (cm)? "))

BMI_Val = cal_BMI(weight,height)

status = None
if BMI_Val >= 30 and BMI_Val > 0 :
    status = 'obese'
elif BMI_Val >= 25:
    status = 'overweight'
elif BMI_Val >= 18.5:
    status = 'normal'
else:
    status = 'underweight'

print(f"Your BMI is {BMI_Val:.2f}")
print(f"Weight status: {status}")