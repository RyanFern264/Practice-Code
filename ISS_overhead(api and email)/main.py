import requests
from datetime import datetime
import smtplib

MY_LAT = 25.761681 # Your latitude
MY_LONG = -80.191788 # Your longitude
my_email = "testingpython155@gmail.com"
password = ""#removed password since this is getting put in my public git

def is_iss_overhead():
    sunset_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    sunset_response.raise_for_status()
    data = sunset_response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 2 <= iss_latitude <= MY_LAT + 2 and MY_LONG - 2 <= iss_longitude <= MY_LONG + 2:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    time_now = datetime.now()
    sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    sunset_response.raise_for_status()
    data = sunset_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    if 22 <= time_now.hour or time_now.hour <= 12:
        return True


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

if is_iss_overhead() and is_night():
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ryanfmiami@gmail.com",
                            msg=f"Subject:ISS overhead!\n\nISS is overhead and visible!")


