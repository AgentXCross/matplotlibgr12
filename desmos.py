import matplotlib.pyplot as plt
import numpy as np

#x values in radians
x_trig = np.linspace(-2 * np.pi, 2 * np.pi, 500) #For trig function run from -2pi to 2pi
x_ln = np.linspace(0.01, 2 * np.pi, 500)  #for ln(x) go from 0.01 to 2pi, 500 points in between 

#y values to connect points to create the graph
y_sin = np.sin(x_trig)
y_cos = np.cos(x_trig)
y_ln = np.log(x_ln)

#Create a plot for the graphs
fig, ax = plt.subplots(figsize = (10, 6))

#enter axes at (0,0), MatPlotLib Usually creates a box, we are removing the top and right side of box and moving the left and bottom to (0,0) to create 2 axes
ax.spines['left'].set_position('zero')   #y-axis at x=0
ax.spines['bottom'].set_position('zero') #x-axis at y=0
ax.spines['right'].set_color('none')     #hide right border, used to be apart of the box
ax.spines['top'].set_color('none')       #hide top border

#Set line thickness
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

#Add ticks for the x and y axis
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

#Plot functions on the ax
ax.plot(x_trig, y_sin, color = 'royalblue', linewidth = 3, alpha = 0.8)         #y = sin(x), adjusted linewidth and opacity
ax.plot(x_trig, y_cos, color = 'fuchsia', linewidth = 3, alpha = 0.8)           #y = cos(x)
ax.plot(x_ln, y_ln, color = 'palevioletred', linewidth = 3, alpha = 0.8)        #y = ln(x)

plt.show()


