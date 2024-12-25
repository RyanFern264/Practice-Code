import smtplib
import datetime as dt
import random

now = dt.datetime.now()
day_of_week = now.weekday()

with open("quotes.txt") as file:
    quotes = file.readlines()
rand_quote = random.choice(quotes)

my_email = "testingpython155@gmail.com"
password = ""#removed password since this is getting put in my public git
if day_of_week == 2:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="ryanfmiami@gmail.com",
                            msg=f"Subject:inspo quote\n\n{rand_quote}")







