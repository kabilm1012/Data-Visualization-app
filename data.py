import pandas as pd

df = pd.read_csv("happy.csv")


def get_data(x_option, y_option):
    x = x_option.lower()
    y = y_option.lower()
    x_data = df[x].to_list()
    y_data = df[y].to_list()
    return x_data, y_data
