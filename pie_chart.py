import matplotlib.pyplot as plt

labels_ = [ #For categories of data
    "Apples", "Bananas", "Cherries", "Blueberries", "Blackberries",
    "Raspberries", "Grapes", "Honeydew", "Watermelon", "Mango"
]
values = [12, 19, 7, 5, 14, 10, 8, 11, 6, 8] #Corresponding values (y-data)
pie_title = "Favourite Fruit Among BCSS Students"
colors_ = ['crimson', 'yellow', 'firebrick', 'midnightblue', 'indigo', 'deeppink',
          'rebeccapurple', 'khaki', 'forestgreen', 'gold'] #Color list for each pie chart area

plt.pie(values, labels = labels_, colors = colors_, autopct = '%1.1f%%', textprops = {'fontsize': 12, 'fontfamily': 'Georgia'}) #Create pie chart while restricting to one decimal
plt.title(
        pie_title,
        fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': 'Georgia'}
        ) #Create a title

plt.show()