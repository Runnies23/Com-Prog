import numpy as np
import matplotlib.pyplot as plt

file_name = input("Enter file name: ")
text = open(file_name).read().splitlines()

height = []
weight = []
BMI = []
for i in text:
    weight_temp, height_temp = list(map(float, i.split(",")))
    weight.append(weight_temp)
    height.append(height_temp)
    height_temp /= 100
    BMI.append(weight_temp / (height_temp * height_temp))

plt.scatter(weight,height,c=BMI)
plt.xlabel("Weight (kg)")
plt.ylabel("Height (cm)")
plt.grid(True)
bar = plt.colorbar()
bar.ax.set_title("BMI")
plt.set_cmap("jet")
plt.show()