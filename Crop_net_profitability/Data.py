import csv
import pandas as pd

crops = ['Banana',
         'Potato',
         'Onion',
         'Ginger',
         'Rice',
         'Wheat',
         'Maize',
         'Bajra',
         'Tobacco',
         'Groundnut',
         'Cotton',
         'Sesame']

with open('data/operation_costs.csv', 'r') as OC:
    reader = csv.reader(OC, delimiter=',')
    # Skip header
    next(reader, None)
    # Yield
    Y = [float(row[6]) for row in reader]

frame = pd.read_csv("data/operation_costs.csv")

Input_costs = frame["Input_costs"].tolist()
Tillage_Interculture_cost = frame["Tillage_Interculture_cost"].tolist()
Irrigation_cost = frame["Irrigation_cost"].tolist()
Harvesting_Cost = frame["Harvesting_Cost"].tolist()
Other_costs = frame["Other_costs"].tolist()

# Create a list of lists
list_of_lists = [Input_costs, Tillage_Interculture_cost, Irrigation_cost, Harvesting_Cost, Other_costs]

# Zip the lists together
zipped_list = zip(*list_of_lists)

# create list of lists from zipped list of tuples
crop_cost = []
for i in zipped_list:
    crop_cost.append(list(i))

# create crop wise total cost list from list of lists
total_cost_list = []
for j in crop_cost:
    total_cost_list.append(sum(j))

# creating dictionary of crops with crop name as key and its total cost as value
total_crop_wise_cost = {s: v for s, v in zip(crops, total_cost_list)}
