import pandas as pd

def avg_return(crop):
    df52 = pd.read_csv("data/{}.csv".format(crop))
    c1 = df52["Month1"].tolist()
    c2 = df52["Month2"].tolist()
    c3 = df52["Month3"].tolist()

    avg_ret = (c3[4]+c2[4]+c1[4])/3
    r = "{:.2f}".format(avg_ret)
    return r

# Define a function to calculate the average yield for a crop
def calculate_average_yield(row_data):
    # Exclude the first column and calculate the average
    average_yield = sum(row_data[1:]) / (len(row_data) - 1)
    return average_yield

def return_per_acre(Yield, market_pr):
    return Yield*market_pr
