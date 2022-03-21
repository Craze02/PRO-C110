import statistics
import csv
from numpy import mean
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("C110/PRO-C110/medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("The population mean is: ", population_mean)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index= random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    sampling_mean = statistics.mean(mean_list)
    print("The sampling mean is: ", sampling_mean)

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.show()

setup()
