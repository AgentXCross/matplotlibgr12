import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'Georgia' #Global font as georgia

#Define the domain for the function
x = np.linspace(-8, 8, 120)
y = np.linspace(-7, 7, 120)
x, y = np.meshgrid(x, y)

#Define the function in terms of z for f(x,y) = x^2 * y + sin(y)
z = (x**2) * y + np.sin(y)

fig = plt.figure(figsize = (10, 8))
ax = fig.add_subplot(111, projection = '3d')
surf = ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'none') #Color gradient

ax.set_title("F(x, y) = x²y + sin(y)", {'fontsize': 25, 'fontweight': 'bold', 'family': 'Georgia'}) #Create a fancy title and adjust axis titles
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("F(x, y)")

ax.set_box_aspect([1, 1, 1])  #Equal axis scaling
plt.colorbar(surf, ax = ax, shrink = 0.6, label = "z value")
plt.show()