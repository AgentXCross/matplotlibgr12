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
fig, ax = plt.subplots(figsize=(10, 6))
