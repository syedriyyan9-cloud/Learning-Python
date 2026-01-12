# Date: 2 jan 2026
# Name: riyyan

# 15-1. Cubes: A number raised to the third power is a cube. Plot the first five
# cubic numbers, and then plot the first 5000 cubic numbers.

# 15-2. Colored Cubes: Apply a colormap to your cubes plot.

import matplotlib.pyplot as plt

x_values = [x for x in range(5001)]
y_values = [x**3 for x in x_values]
fig, ax = plt.subplots()
ax.scatter(x_values,y_values, c=y_values, cmap=plt.cm.Greens)
# ax.plot(x_values, y_values)
plt.show()
