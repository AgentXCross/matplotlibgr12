import matplotlib.pyplot as plt

type_of_graph = input("Which type of graph would you like to create (Scatter Plot, Box and Whisker Plot, Histogram)?: ")
font = input("Which font would you like to use (Georgia, Arial, Times New Roman, Futura)?: ")

match type_of_graph:
    case "Histogram":
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

    case "Scatter Plot":
        pass

    case "Box and Whisker Plot":
        pass
