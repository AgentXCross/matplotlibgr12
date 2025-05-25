import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize = (8, 6)) #Size of window

gdp_per_worker = [ #data set #1 for y-variable
    139054.84, 149734.53, 109288.54, 125959.58, 105513.48,
    108618.67, 161430.35, 130445.52, 151336.56, 155698.46,
    115580.11, 123660.61, 125564.36, 105291.61, 139067.20,
    125413.54, 120424.05, 117436.89, 108130.82, 115679.85,
    97305.39, 110828.50, 136466.34, 154533.14, 118758.52,
    128518.24, 92437.59, 113386.30, 100355.61, 125838.93,
    97301.50, 87770.63, 132602.75, 122842.78, 128198.93,
    140244.60, 120544.10, 174374.81, 123896.53, 126044.22,
    103241.15, 125437.60, 108254.73, 122930.41, 84554.68,
    126529.48, 96173.01, 121054.01, 134651.50, 111100.76,
    114426.02, 119158.00, 134314.49, 124530.50, 103321.59,
    133649.44, 175084.70, 119117.41, 117060.37, 119515.27
]

workforce_in_stem = [ #data set #2 for x-variable
    10.40, 9.90, 9.50, 10.70, 8.50, 7.40, 12.70, 14.60, 12.90, 10.80,
    9.50, 10.60, 10.20, 9.20, 11.90, 10.10, 9.10, 11.50, 9.60, 9.20,
    6.70, 10.60, 15.20, 16.10, 11.60, 12.70, 7.60, 10.60, 10.70, 8.40,
    7.80, 7.60, 11.00, 8.50, 14.40, 13.50, 11.20, 11.80, 11.50, 10.40,
    8.90, 10.60, 8.80, 12.40, 7.30, 12.10, 8.40, 11.10, 7.50, 9.90,
    10.50, 9.70, 10.50, 10.60, 12.10, 14.00, 14.90, 9.20, 10.70, 7.80
]

#Line of Best Fit
slope, intercept = np.polyfit(workforce_in_stem, gdp_per_worker, 1) #x-var, y-var, degree 1 to return the slope and intercept of LOBF
x_fit = sorted(workforce_in_stem) #Sorted list of x-var
y_fit = [slope * val + intercept for val in x_fit] #Gets the corresponding y-value for every x on the line of best fit. MatPlotLib will connect all of them

#Scatter Plot
y_ticks = [75000, 90000, 105000, 120000, 135000, 150000, 165000, 180000]
x_ticks = [6, 8, 10, 12, 14, 16, 18] #List for x-axis and y-axis ticks on scatterplot

plt.scatter(workforce_in_stem, gdp_per_worker, color = 'darkturquoise', label = 'Data Points') #Create scatter plot with workforce as x and gdp as y
plt.xlabel("% Workforce in STEM",
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': 'Georgia'}) 
plt.ylabel("GDP per Worker ($USD)",
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': 'Georgia'})
plt.title("GDP per Worker VS % STEM Workforce in U.S. States and Canadian Provinces",
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': 'Georgia'})

plt.xticks(x_ticks, fontname = 'Georgia', fontsize = 10) #Set ticks
plt.yticks(y_ticks, fontname = 'Georgia', fontsize = 10)

#Plot the line of best fit
plt.plot(x_fit, y_fit, color = 'crimson', linewidth = 2, label = 'Line of Best Fit')

#Create a legend for the 2 plots (Line of best fit and scatter plot)
plt.legend(prop = {'family': 'Georgia', 'size': 10})
plt.grid(True)
plt.show()