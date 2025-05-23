import matplotlib.pyplot as plt
import numpy as np

#x values in radians
x_trig = np.linspace(-2 * np.pi, 2 * np.pi, 500) #For trig function run from -2pi to 2pi
x_ln = np.linspace(0.01, 2 * np.pi, 500)  #for ln(x) go from 0.01 to 2pi, 500 points in between 
x_e = np.linspace(-2 * np.pi, np.log(3), 500) #for e^x limit it below 3 to prevent horizantal line

#y values to connect points to create the graph
y_sin = np.sin(x_trig)
y_cos = np.cos(x_trig)
y_ln = np.log(x_ln)
y_e = np.clip(np.exp(x_e), None, 3) #Place an upper bound on e^x

#Create a plot for the graphs and title
fig, ax = plt.subplots(figsize = (10, 6))
ax.set_title("f(x) = sin(x), cos(x), ln(x), and e^(x)", fontsize = 14, fontweight = 'bold', fontname = 'Georgia')

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

#Set tick label font to Georgia
for label in ax.get_xticklabels():
    label.set_fontname('Georgia')
for label in ax.get_yticklabels():
    label.set_fontname('Georgia')

#Plot functions on the ax
ax.plot(x_trig, y_sin, color = 'red', linewidth = 3, alpha = 0.8, label = 'f(x) = sin(x)')           #y = sin(x), adjusted linewidth and opacity
ax.plot(x_trig, y_cos, color = 'gold', linewidth = 3, alpha = 0.8, label = 'f(x) = cos(x)')                 #y = cos(x)
ax.plot(x_ln, y_ln, color = 'limegreen', linewidth = 3, alpha = 0.8, label = 'f(x) = ln(x)')             #y = ln(x)
ax.plot(x_e, y_e, color = 'dodgerblue', linewidth = 3, alpha = 0.8, label = 'f(x) = e^x')                  #y = e^(x)

#Legend for functions
ax.legend(loc = 'upper left', fontsize = 10, frameon = False, prop = {'family': 'Georgia'})

plt.show()


