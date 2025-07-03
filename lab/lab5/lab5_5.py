"""
Quadratic Equation Solver

this function solve the Quandratic Equation
return 3 data format 
- if D == 0 
- if D < 0
- if D > 0
"""

from math import sqrt

def Quadratic_Equation_Solver():
    input_list = [None] * 3 
    for i in range(3):
        index_list = ['1st','2nd','3rd']
        input_list[i] = float(input(f"{index_list[i]} coefficient: "))
        if input_list[0] == 0:
            print("1st coefficient can't be zero. Program exits.")
            return {"message" : "1st_zero"}
        
    D = (input_list[1] ** 2) - (4 * input_list[0] * input_list[2])

    if float(D) == 0.0:
        return {
                "message" : "DEqualZero",
                "value" : - (input_list[1] / (2 * input_list[0]))
                }
    if D > 0:
        return {
                "message" : "DMorethanZero",
                "value" : [(- input_list[1] + sqrt(D)) / (2 * input_list[0]), (- input_list[1] - sqrt(D)) / (2 * input_list[0])]                
                }
    if D < 0:
        first_val = (-input_list[1]) / (2 * input_list[0])
        second_val = sqrt(-D) / (2 * input_list[0])

        if second_val < 0:
            second_val = abs(second_val)
            return {
                "message" : "DLessthanZero",
                "value" : [
                    f"{first_val:.3f}+{second_val:.3f}i",
                    f"{first_val:.3f}-{second_val:.3f}i"
                ]
            }
        return {
            "message" : "DLessthanZero",
            "value" : [
                f"{first_val:.3f}+{second_val:.3f}i",
                f"{first_val:.3f}-{second_val:.3f}i"
            ]
        }

response = Quadratic_Equation_Solver()
if response['message'] == "1st_zero":
    pass
if response['message'] == "DEqualZero":
    print(f"Only one real root: {response['value']:.3f}")
if response['message'] == "DMorethanZero":
    print(f"Two real roots: {response['value'][0]:.3f} and {response['value'][1]:.3f}")
if response['message'] == "DLessthanZero":
    print(f"Two complex roots: {response['value'][0]} and {response['value'][1]}")
else:
    pass