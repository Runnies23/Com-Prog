import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2,2,100)
y = (x**3)- (2*x) + 1
# y = np.sin(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()


import numpy as np
import matplotlib.pyplot as plt

temperature = np.array([28,32,25,35,30])
humidity = np.array([50,65,34,90,75])
rainfall = np.array([10,25,0,50,16])

plt.scatter(temperature,humidity,c= rainfall)
plt.xlabel("Temperature (C)")
plt.ylabel("Humidity (%)")
plt.grid(True)
bar = plt.colorbar()  # add a color bar
bar.ax.set_title("Rainfall (mm)")  # add title to the color bar
plt.set_cmap("jet")  # set color mapping scheme to "jet"
plt.show()
