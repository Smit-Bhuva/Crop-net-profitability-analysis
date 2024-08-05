import pandas as pd
import Calc

# Read the CSV files into Pandas DataFrames
df_banana = pd.read_csv("data/Banana.csv")
df_potato = pd.read_csv("data/Potato.csv")
df_ginger = pd.read_csv("data/Ginger.csv")
df_onion = pd.read_csv("data/Onion.csv")

# Calculate the average yield for each crop
average_banana_mar_p = df_banana.apply(Calc.calculate_average_yield, axis=1)
average_potato_mar_p = df_potato.apply(Calc.calculate_average_yield, axis=1)
average_ginger_mar_p = df_ginger.apply(Calc.calculate_average_yield, axis=1)
average_onion_mar_p = df_onion.apply(Calc.calculate_average_yield, axis=1)

# convert data to list
banana_list = average_banana_mar_p.tolist()
potato_list = average_potato_mar_p.tolist()
ginger_list = average_ginger_mar_p.tolist()
onion_list = average_onion_mar_p.tolist()
