import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

R = 3  #Major radius for torus
r = 1 #Minor radius

#Create a meshgrid for u and v (The scalars)
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, 2 * np.pi, 100)
u, v = np.meshgrid(u, v)

#Parametric equations
x = (R + r * np.cos(v)) * np.cos(u)
y = (R + r * np.cos(v)) * np.sin(u)
z = r * np.sin(v)

#Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y, z, cmap = 'viridis', edgecolor = 'none') #Color gradient

ax.set_title("Parametric Torus", {'fontsize': 13, 'fontweight': 'bold', 'family': 'Georgia'})
ax.set_box_aspect([1, 1, 0.2])  
ticks = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
ax.set_xticks(ticks) #Adjust the x and y-axis
ax.set_yticks(ticks)
ax.set_xticklabels(ticks, fontname = 'Georgia')
ax.set_yticklabels(ticks, fontname = 'Georgia')
ax.set_zticks([]) #Remove the zticks
plt.show()