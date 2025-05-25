import matplotlib.pyplot as plt
import numpy as np

def histogram(font):
    raw_data = input("Enter your data separated by commas: ") #Ask user for data
    data = [float(num.strip()) for num in raw_data.split(",")]
    raw_bins = input("Enter all the bins separated by commas: ") #Ask user for bins 
    bin_edges = [round(float(num.strip()), 2) for num in raw_bins.split(",")] 
    hist_title = input("Enter your histogram title: ") #Ask for title
    x_axis_label = input("Enter the label for the x-axis: ") #X axis label
    y_axis_label = input("Enter the label for the y-axis: ") #Y axis label
    outline_color = input("Enter the edge color for the histogram: ") #Ask for edge color of bars
    fill_color = input("Enter the fill color for the histogram: ") #Ask for fill color
    plt.hist(data, bins = bin_edges, edgecolor = outline_color, color = fill_color) #Create the histogram
    plt.title(  #Title name and font
        hist_title,
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': font}
        )
    plt.xlabel(x_axis_label, fontsize = 12, fontweight = 'medium', family = font) #X and Y axis
    plt.ylabel(y_axis_label, fontsize = 12, fontweight = 'medium', family = font)
    plt.xticks(bin_edges, fontname = font, fontsize = 10) #Adjust tick font and size
    plt.yticks(fontname = font, fontsize = 10)
    plt.show()    

def scatter_plot(font):
    raw_y_data = input("Enter your y-variable data separated by commas in order: ") #Ask user for data
    raw_x_data = input("Enter your x-variable data separated by commas in order: ") 
    y_data = [round(float(num.strip()), 2) for num in raw_y_data.split(",")]
    x_data = [round(float(num.strip()), 2) for num in raw_x_data.split(",")]
    #Check if number of x and y data values match
    if len(x_data) != len(y_data):
        print("Error: The number of x and y values must match!")
        return
    scatter_title = input("Enter your scatterplot title: ") #Ask for title
    x_axis_label = input("Enter the label for the x-axis: ") #X axis label
    y_axis_label = input("Enter the label for the y-axis: ") #Y axis label
    fill_color = input("Enter the fill color for the data points: ") #Ask for fill color
    raw_x_ticks = input("Enter the x-ticks separated by commas: ") #Ticks
    raw_y_ticks = input("Enter the y-ticks separated by commas: ")
    x_ticks = [round(float(tick.strip()), 2) for tick in raw_x_ticks.split(",")]
    y_ticks = [round(float(tick.strip()), 2) for tick in raw_y_ticks.split(",")]
    line_color = input("Enter the line of best fit color: ") #LOBF color
    #Line of best fit calculations
    slope, intercept = np.polyfit(x_data, y_data, 1)
    x_fit = sorted(x_data)
    y_fit = [slope * val + intercept for val in x_fit]
    #Create scatter plot
    plt.scatter(x_data, y_data, color = fill_color, label = "Data Points")
    plt.xlabel(
        x_axis_label,
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': font}
    )
    plt.ylabel(
        y_axis_label,
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': font}
    )
    plt.title(
        scatter_title,
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': font}
    )
    plt.xticks(x_ticks, fontname = font, fontsize = 10) #Set ticks
    plt.yticks(y_ticks, fontname = font, fontsize = 10)
    plt.plot(x_fit, y_fit, color = line_color, linewidth = 2, label = "Line of Best Fit")
    plt.legend(prop = {'family': font, 'size': 10})
    plt.grid(True)
    plt.show()

def bar_chart(font):
    raw_x_data = input("Enter your categories in bar chart separated by commas: ")
    raw_y_data = input("Enter the corresponding values separated by commas: ")
    x_data = [value.strip() for value in raw_x_data.split(",")]
    y_data = [round(float(value.strip()), 2) for value in raw_y_data.split(",")]
    #Check if number of x and y data values match
    if len(x_data) != len(y_data):
        print("Error: The number of x and y values must match!")
        return
    bar_title = input("Enter your bar chart title: ") #Ask for title
    x_axis_label = input("Enter the label for the x-axis: ") #X axis label
    y_axis_label = input("Enter the label for the y-axis: ") #Y axis label
    fill_color = input("Enter the fill color for the bars: ")
    raw_y_ticks = input("Enter the y-ticks separated by commas: ")
    y_ticks = [round(float(tick.strip()), 2) for tick in raw_y_ticks.split(",")]
    plt.ylim(min(y_ticks), max(y_ticks))
    #Create the chart
    plt.bar(x_data, y_data, color = fill_color)
    plt.xlabel(
        x_axis_label,
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': font}
    )
    plt.ylabel(
        y_axis_label,
        fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': font}
    )
    plt.title(
        bar_title,
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': font}
    )
    plt.yticks(y_ticks, fontname = font, fontsize = 10)
    plt.show()

def pie_chart(font):
    raw_x_data = input("Enter your pie chart categories separated by commas: ")
    raw_y_data = input("Enter the corresponding values separated by commas: ")
    x_data = [val.strip() for val in raw_x_data.split(",")]
    y_data = [round(float(val.strip()), 2) for val in raw_y_data.split(",")]
    pie_title = input("Enter the title of your pie chart: ")
    raw_colors = input("Enter the colors in corresponding order separated by commas: ")
    colors = [color.strip() for color in raw_colors.split(",")]
    #Check if number of x and y data values and colors match
    if len(x_data) == len(y_data) == len(colors):
        plt.pie(y_data, labels = x_data, colors = colors, autopct = '%1.1f%%', textprops = {'fontsize': 12, 'fontfamily': font})
        plt.title(
            pie_title,
            fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': font}
        )
        plt.show()
    else:
        print("Error: The number of x, y values, and colors must match!")
        return
    
def box_and_whisker(font):
    raw_data = input("Enter your data separated by commas: ") #Ask user for data
    data = [float(num.strip()) for num in raw_data.split(",")]
    box_title = input("Enter the title of the box-and-whisker plot: ")
    x_title = input("Enter the x-axis title: ")
    raw_x_ticks = input("Enter the x-axis tick values: ")
    x_ticks = [round(float(tick.strip()), 2) for tick in raw_x_ticks.split(",")]
    color = input("Enter the color of the box-and-whisker plot: ")
    box = plt.boxplot(data, vert = False, patch_artist = True, widths = 0.6, medianprops = dict(color = 'black')) #Set patchartist to true to color the boxes
    box['boxes'][0].set_facecolor(color)
    box['boxes'][0].set_linewidth(2)
    plt.title(
        box_title,
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': font}
    )
    plt.xlabel(x_title, fontdict = {'fontsize': 12, 'fontweight': 'medium', 'family': font})
    plt.xticks(x_ticks, fontname = font)
    plt.yticks([]) #Hide y-ticks
    plt.grid(True)
    plt.show()

def main():
    type_of_graph = input("Which type of graph would you like to create (Scatter Plot, Bar Chart, Histogram, Pie Chart, Box and Whisker Plot)?: ").strip().lower()
    font_input = input("Which font would you like to use (Georgia, Arial, Times New Roman, Futura)?: ")
    fontmap = { #Make sure the user picks a valid font, else default to Georgia
        'Georgia': 'Georgia',
        'Arial': 'Arial',
        'Times New Roman': 'Times New Roman',
        'Futura': 'Futura'
    }
    font = fontmap.get(font_input.strip(), 'Georgia')
    match type_of_graph:
        case "histogram":
            histogram(font)
        case "scatter plot":
            scatter_plot(font)
        case "bar chart":
            bar_chart(font)
        case "pie chart":
            pie_chart(font)
        case "box and whisker plot":
            box_and_whisker(font)
        case _:
            print("Error: Please pick one of the valid options.")
            return
    return

if __name__ =="__main__":
    main()

