# TODO: with the array created from all csvs, check if any of those are normals for the alarms that are on active_alarms.csv
# TODO: pair the ALARM and NORMAL to each other, and delete the line from active_alarms.csv
# TODO: now, if the time delta between alarm and normal was greater than 5 mins, send out the special thing

from os import listdir, getcwd, remove
from time import sleep
import datetime as dt
import csv


only_files = [f for f in listdir(getcwd()) if "00.csv" in f]
all_alarms = []
active_alarms = []

# TODO: create active_alarms.csv if it does not already exist
try:
    active_alarms_csv = open("active_alarms.csv")
    active_alarms_csv.close()
except FileNotFoundError:
    active_alarms_csv = open("active_alarms.csv", mode="a")
    active_alarms_csv.close()

# TODO: read active_alarms.csv into an array, where each item is the full line of an alarm
with open("active_alarms.csv", mode="r") as active_alarm_memory:
    reader = csv.reader(active_alarm_memory)
    for line in reader:
        active_alarms.append(line)

# TODO: iterate through all csvs in the current directory, and read each alarm. Then create an alarm object for each alarm
for file in only_files:
    with open(file, mode="r") as fac011_file:
        reader = csv.reader(fac011_file)
        for line in reader:
            print(line)
            # date = line[0][:10]
            # time = line[0][11:19]
            # location = [line[1], line[2], line[3], line[4]]
            # status = line[5]
            all_alarms.append(line)

# TODO: compare that to active alarms, and add any alarms that are not already on the active_alarms.csv
for alarm in all_alarms:
    if alarm not in active_alarms and alarm[5] == "ALARM":
        active_alarms.append(alarm)

# TODO: with the array created from all csvs, check if any of those are normals for the alarms that are on active_alarms.csv
for alarm in all_alarms:
    if alarm[5] == "NORMAL":
        for active_alarm in active_alarms:
            alarm_location = f"{alarm[1], alarm[2], alarm[3], alarm[4]}"
            active_alarm_location = f"{active_alarm[1], active_alarm[2], active_alarm[3], active_alarm[4]}"
            if alarm_location == active_alarm_location:
                active_alarms.remove(active_alarm)
                alarm_time = dt.datetime.strptime(active_alarm[0], "%m/%d/%Y %H:%M:%S")
                normal_time = dt.datetime.strptime(alarm[0], "%m/%d/%Y %H:%M:%S")
                time_difference = (normal_time - alarm_time).total_seconds()
                print(f"alarm started at {alarm_time} and ended at {normal_time}, total duration {time_difference}")
                if time_difference > 300:
                    timestamp = dt.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
                    file_name = f"paired_alarms_{timestamp}.csv"
                    with open(file_name, mode="a", newline="") as paired_alarms:
                        writer = csv.writer(paired_alarms)
                        writer.writerow(active_alarm)
                        writer.writerow(alarm)
                        sleep(1)

remove("active_alarms.csv")
with open("active_alarms.csv", mode="a", newline="") as active_alarm_memory_new:
    writer = csv.writer(active_alarm_memory_new)
    writer.writerows(active_alarms)
