import csv
import pandas
# with open("weather_data.csv") as file:
#     data = csv.reader(file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))


data = pandas.read_csv("weather_data.csv")
#
# #Get max value(temp)
# # temp_list = data["temp"]
# # max_temp = temp_list.max()
# # print(max_temp)
#
# #Get row where temp was max
# #print(data[data.temp == data.temp.max()])
#
# #Get data in row where it was Monday
# #print(data[data.day == "Monday"])
#
# #Convert monday temp from C to F
# monday = data[data.day == "Monday"]
# print(monday)
# monday_temp_f = (monday.temp * 9/5) + 32
# print(monday_temp_f.iloc[0]) #need iloc since it's still a series object
# #OR
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
gray_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"]
total_gray_squirrels = len(gray_squirrels)

cinnamon_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"]
total_cinnamon_squirrels = len(cinnamon_squirrels)

black_squirrels = squirrel_data[squirrel_data["Primary Fur Color"] == "Black"]
total_black_squirrels = len(black_squirrels)

squirrel_count = {
    "Fur Color": ["gray", "cinnamon", "black"],
    "Count": [total_gray_squirrels, total_cinnamon_squirrels, total_black_squirrels]
}

squirrel_count = pandas.DataFrame(squirrel_count)
squirrel_count.to_csv("squirrel_count.csv")