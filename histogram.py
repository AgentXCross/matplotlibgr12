import matplotlib.pyplot as plt

gdp_per_worker = [ #data set #1 for histogram
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

workforce_in_stem = [ #data set #2 for histogram
    10.40, 9.90, 9.50, 10.70, 8.50, 7.40, 12.70, 14.60, 12.90, 10.80,
    9.50, 10.60, 10.20, 9.20, 11.90, 10.10, 9.10, 11.50, 9.60, 9.20,
    6.70, 10.60, 15.20, 16.10, 11.60, 12.70, 7.60, 10.60, 10.70, 8.40,
    7.80, 7.60, 11.00, 8.50, 14.40, 13.50, 11.20, 11.80, 11.50, 10.40,
    8.90, 10.60, 8.80, 12.40, 7.30, 12.10, 8.40, 11.10, 7.50, 9.90,
    10.50, 9.70, 10.50, 10.60, 12.10, 14.00, 14.90, 9.20, 10.70, 7.80
]

data_set = input("Which Data Set would you like to view?\n\t1. GDP Per Worker of all U.S. States and Canadian Provinces\n\t2. % Workforce in STEM of all U.S. States and Canadian Provinces\n")
match data_set:
    case "1":
        bin_edges = [75000, 90000, 105000, 120000, 135000, 150000, 165000, 180000]
        plt.hist(gdp_per_worker, bins = bin_edges, edgecolor = 'darkcyan', color = 'darkturquoise') #7 histogram bins for GDP per worker

        plt.title(  #Title name and font
            'Nominal GDP Per Worker in Canadian Provinces and U.S. States',
            fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': 'Georgia'}
            )
        plt.xlabel('GDP Per Worker ($USD)', fontsize = 12, fontweight = 'medium', family = 'Georgia') #X and Y axis
        plt.ylabel('# of States/Provinces', fontsize = 12, fontweight = 'medium', family = 'Georgia')

        plt.xticks(bin_edges, fontname = 'Georgia', fontsize = 10) #Adjust tick font and size
        plt.yticks(fontname = 'Georgia', fontsize = 10)
        
        plt.show()
    case "2":
        bin_edges = [6, 8, 10, 12, 14, 16, 18]
        plt.hist(workforce_in_stem, bins = bin_edges, edgecolor = 'mediumvioletred', color = 'deeppink') #7 histogram bins for % Workforce in STEM

        plt.title(
            '% Workforce in STEM of U.S. States and Canadian Provinces',
            fontdict = {'fontsize': 13, 'fontweight': 'bold', 'family': 'Georgia'}
            )
        plt.xlabel('% Workforce in STEM', fontsize = 12, fontweight = 'medium', family = 'Georgia')
        plt.ylabel('# of States/Provinces', fontsize = 12, fontweight = 'medium', family = 'Georgia')

        plt.xticks(bin_edges, fontname = 'Georgia', fontsize = 10)
        plt.yticks(fontname = 'Georgia', fontsize = 10)

        plt.show()
    case _:
        print("Please enter either 1 or 2\n")