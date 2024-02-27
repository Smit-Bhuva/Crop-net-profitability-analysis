import pandas as pd
import csv


# Rice

with open('data/Rice.csv', 'r') as Rice:
    reader = csv.reader(Rice, delimiter=',')
    # Skip header
    next(reader, None)
    sept = [float(row[1]) for row in reader]

df = pd.read_csv("data/Rice.csv")
octo = df['Month2'].tolist()
nov = df['Month3'].tolist()

y1 = (sept[0]+octo[0]+nov[0])/3
y2 = (sept[1]+octo[1]+nov[1])/3
y3 = (sept[2]+octo[2]+nov[2])/3
y4 = (sept[3]+octo[3]+nov[3])/3
y5 = (sept[4]+octo[4]+nov[4])/3

year1 = [y1, y2, y3, y4, y5]

# Wheat
with open('data/Wheat.csv', 'r') as Wheat:
    reader = csv.reader(Wheat, delimiter=',')
    # Skip header
    next(reader, None)
    feb = [float(row[1]) for row in reader]

df2 = pd.read_csv("data/Wheat.csv")
mar = df2['Month2'].tolist()
apr = df2['Month3'].tolist()

y6 = (feb[0]+mar[0]+apr[0])/3
y7 = (feb[1]+mar[1]+apr[1])/3
y8 = (feb[2]+mar[2]+apr[2])/3
y9 = (feb[3]+mar[3]+apr[3])/3
y10 = (feb[4]+mar[4]+apr[4])/3

year2 = [y6, y7, y8, y9, y10]

# Maize

with open('data/Maize.csv', 'r') as Maize:
    reader = csv.reader(Maize, delimiter=',')
    # Skip header
    next(reader, None)
    augu = [float(row[1]) for row in reader]

df3 = pd.read_csv("data/Maize.csv")
sep = df3['Month2'].tolist()
oct = df3['Month3'].tolist()

y11 = (augu[0]+sep[0]+oct[0])/3
y12 = (augu[1]+sep[1]+oct[1])/3
y13 = (augu[2]+sep[2]+oct[2])/3
y14 = (augu[3]+sep[3]+oct[3])/3
y15 = (augu[4]+sep[4]+oct[4])/3

year3 = [y11, y12, y13, y14, y15]

# Bajra

with open('data/Bajra.csv', 'r') as Bajra:
    reader = csv.reader(Bajra, delimiter=',')
    # Skip header
    next(reader, None)
    april = [float(row[1]) for row in reader]

df4 = pd.read_csv("data/Bajra.csv")
may = df4['Month2'].tolist()
june = df4['Month3'].tolist()

y16 = (april[0]+may[0]+june[0])/3
y17 = (april[1]+may[1]+june[1])/3
y18 = (april[2]+may[2]+june[2])/3
y19 = (april[3]+may[3]+june[3])/3
y20 = (april[4]+may[4]+june[4])/3

year4 = [y16, y17, y18, y19, y20]