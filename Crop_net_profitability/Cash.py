import pandas as pd
import Calc

# Read the CSV files into Pandas DataFrames
df_Groundnut = pd.read_csv("data/Groundnut.csv")
df_Tobacco = pd.read_csv("data/Tobacco.csv")
df_Sesame = pd.read_csv("data/Sesame.csv")
df_Cotton = pd.read_csv("data/Cotton.csv")

# Calculate the average yield for each crop
average_Groundnut_mar_p = df_Groundnut.apply(Calc.calculate_average_yield, axis=1)
average_Tobacco_mar_p = df_Tobacco.apply(Calc.calculate_average_yield, axis=1)
average_Sesame_mar_p = df_Sesame.apply(Calc.calculate_average_yield, axis=1)
average_Cotton_mar_p = df_Cotton.apply(Calc.calculate_average_yield, axis=1)

# convert data to list
Groundnut_list = average_Groundnut_mar_p.tolist()
Tobacco_list = average_Tobacco_mar_p.tolist()
Sesame_list = average_Sesame_mar_p.tolist()
Cotton_list = average_Cotton_mar_p.tolist()