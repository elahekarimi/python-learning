# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
#     print(temperature)
# import pandas
# data = pandas.read_csv("weather_data.csv")
# data_temp = data["temp"].to_list()
# # avg = sum(data_temp) / len(data_temp)
# # print(avg)
# meana = data["temp"].mean()
# maxi = data["temp"].max()
# # print(data[data.temp == data.temp.max()])
# monday = data[data.day == "monday"]
# can = int(monday.temp)
# print(can)
# far = can * 9/5 + 32
# print(far)
import pandas
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
fur_gray = len(data[data["Primary Fur Color"] == "Gray"])
fur_black = len(data[data["Primary Fur Color"] == "Black"])
fur_Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(fur_gray)
print(fur_black)
print(fur_Cinnamon)
data_dict = {
    "fur_color": ["Gray", "Black", "Cinnamon"],
    "len_color": [fur_gray, fur_black, fur_Cinnamon]
}
df = pandas.DataFrame(data_dict)
df.to_csv("squirrels count.csv  ")

