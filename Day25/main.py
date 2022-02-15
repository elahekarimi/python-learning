# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
import pandas
data = pandas.read_csv("weather_data.csv")
data_temp = data["temp"].to_list()
tem = 0
for temperature in data_temp:
    all_tem = tem + temperature
print(all_tem)


