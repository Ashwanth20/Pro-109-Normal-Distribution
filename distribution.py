import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import random
import statistics

df = pd.read_csv("info.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
std_deviation = statistics.stdev(data)
median = statistics.median(data)
mode = statistics.mode(data)

first_std_dev_start, first_std_dev_end = mean - std_deviation, mean + std_deviation
sec_std_dev_start, sec_std_dev_end = mean - (2*std_deviation), mean + (2*std_deviation)
third_std_dev_start, third_std_dev_end = mean - (3*std_deviation), mean + (3*std_deviation)

fig = ff.create_distplot([data], ["reading score"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.17], mode = 'lines', name = 'Mean'))
fig.add_trace(go.Scatter(x = [first_std_dev_start,first_std_dev_start], y = [0,0.17], mode = 'lines', name = 'Standard Deviation I'))
fig.add_trace(go.Scatter(x = [first_std_dev_end,first_std_dev_end], y = [0,0.17], mode = 'lines', name = 'Standard Deviation I'))
fig.add_trace(go.Scatter(x = [sec_std_dev_start,sec_std_dev_start], y = [0,0.17], mode = 'lines', name = 'Standard Deviation II'))
fig.add_trace(go.Scatter(x = [sec_std_dev_end,sec_std_dev_end], y = [0,0.17], mode = 'lines', name = 'Standard Deviation II'))
fig.show()

listofdata_first = [result for result in data if result > first_std_dev_start and result < first_std_dev_end]
listofdata_second = [result for result in data if result > sec_std_dev_start and result < sec_std_dev_end]
listofdata_third = [result for result in data if result > third_std_dev_start and result < third_std_dev_end]

print("Mean of the data is {}".format(mean))
print("Median of the data is {}".format(median))
print("Mode of the data is {}".format(mode))
print("Standard Deviation of the data is {}".format(std_deviation))

print("{}% of data lies within 1st Standard Deviation".format(len(listofdata_first)*100/len(data)))
print("{}% of data lies within 2nd Standard Deviation".format(len(listofdata_second)*100/len(data)))
print("{}% of data lies within 3rd Standard Deviation".format(len(listofdata_third)*100/len(data)))