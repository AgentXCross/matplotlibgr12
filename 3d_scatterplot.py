import matplotlib.pyplot as plt

gdp_per_worker = [ #data set variable 1
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

workforce_in_stem = [ #data set variable 2
    10.40, 9.90, 9.50, 10.70, 8.50, 7.40, 12.70, 14.60, 12.90, 10.80,
    9.50, 10.60, 10.20, 9.20, 11.90, 10.10, 9.10, 11.50, 9.60, 9.20,
    6.70, 10.60, 15.20, 16.10, 11.60, 12.70, 7.60, 10.60, 10.70, 8.40,
    7.80, 7.60, 11.00, 8.50, 14.40, 13.50, 11.20, 11.80, 11.50, 10.40,
    8.90, 10.60, 8.80, 12.40, 7.30, 12.10, 8.40, 11.10, 7.50, 9.90,
    10.50, 9.70, 10.50, 10.60, 12.10, 14.00, 14.90, 9.20, 10.70, 7.80
]

urbanization_rate = [ #data set variable 3
    74.30, 64.90, 57.70, 89.30, 55.50, 76.90, 94.20, 86.00, 86.30, 82.60,
    91.50, 74.10, 86.10, 69.20, 86.90, 71.20, 63.20, 72.30, 58.70, 71.50,
    62.60, 38.60, 85.60, 91.30, 73.50, 71.90, 46.30, 69.50, 53.40, 43.10,
    52.40, 49.00, 73.00, 94.10, 58.30, 93.80, 74.50, 87.40, 66.70, 61.00,
    82.80, 76.30, 64.60, 80.50, 47.00, 76.50, 72.40, 91.10, 51.50, 67.90,
    57.20, 66.20, 83.70, 89.80, 35.10, 75.60, 83.40, 44.60, 67.10, 62.00
]

#Create a figure with three-dimensional axes
fig = plt.figure(figsize = (12, 8))
ax = fig.add_subplot(111, projection = '3d')

#3D Scatter Plot tick values
y_ticks = [75000, 90000, 105000, 120000, 135000, 150000, 165000, 180000]
x_ticks = [6, 8, 10, 12, 14, 16, 18]
z_ticks = [35, 44, 53, 62, 71, 80, 89, 98]

ax.scatter(
    workforce_in_stem,   #X axis
    gdp_per_worker,      #Y axis
    urbanization_rate,   #Z axis
    color = 'deeppink', #Dot color
    s = 40,              #Dot size
    edgecolor = 'crimson'  
)

#Set axis labels
ax.set_xlabel('% Workforce in STEM', fontsize = 10, fontname = 'Georgia')
ax.set_ylabel('GDP per Worker ($USD)', fontsize = 10, fontname = 'Georgia')
ax.set_zlabel('Urbanization Rate (%)', fontsize = 10, fontname = 'Georgia')
ax.set_title('GDP Per Worker VS % STEM Workforce VS % Urbanization of U.S. States and CAN Provinces',
    fontsize = 12, fontname = 'Georgia', fontweight = 'bold')

#Set ticks and adjust font
ax.set_xticks(x_ticks)
ax.set_xticklabels([str(x) for x in x_ticks], fontname = 'Georgia', fontsize = 10)

ax.set_yticks(y_ticks)
ax.set_yticklabels([str(y) for y in y_ticks], fontname = 'Georgia', fontsize = 10)  

ax.set_zticks(z_ticks)
ax.set_zticklabels([str(z) for z in z_ticks], fontname = 'Georgia', fontsize = 10)

plt.tight_layout() #Adjusts spacing
plt.show()