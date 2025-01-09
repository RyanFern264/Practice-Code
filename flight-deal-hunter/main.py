#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from sympy import false

from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager
from pprint import pprint
import pandas as pd
from datetime import date
from dateutil.relativedelta import relativedelta

flight_tracker = pd.read_excel("flight_tracker.xlsx")
seeker = FlightSearch()

for index, row in flight_tracker.iterrows():
    if flight_tracker.loc[index, "IATA Code"] == "":
        flight_search_obj = FlightSearch()
        city_data = flight_search_obj.city_search(row["City"])
        iataCode = city_data["data"][0]["iataCode"]
        flight_tracker.loc[index, "IATA Code"] = iataCode

today = date.today()
six_months_from_now = today + relativedelta(months=6)
dates = []

for i in range(1, 181):#checking the 6 months-12 months from now timeframe
    departure_date = six_months_from_now + relativedelta(days=i)
    dates.append(departure_date) #  .strftime("%Y-%m-%d")

current_iatacode = flight_tracker.loc[0, 'IATA Code']
depart_date = six_months_from_now.strftime("%Y-%m-%d")
return_date = six_months_from_now + relativedelta(days=7)
target_price = flight_tracker.loc[0, 'Target Price']
pprint(seeker.flight_search(iatacode=current_iatacode, departuredate= depart_date, returndate=return_date, targetprice=target_price))


# for index, row in flight_tracker.iterrows():
#     for date in dates:
#         current_iatacode = flight_tracker.loc[index, 'IATA Code']
#         depart_date = date.strftime("%Y-%m-%d")
#         return_date = date + relativedelta(days=14)
#         target_price = flight_tracker.loc[index, 'Target Price']
#         pprint(seeker.flight_search(iatacode=current_iatacode, departuredate= depart_date, returndate=return_date, targetprice=target_price))

flight_tracker.to_excel("flight_tracker.xlsx", index=False)