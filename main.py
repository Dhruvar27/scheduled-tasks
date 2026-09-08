import os

import smtplib
from calendar import week, weekday

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")




import datetime as dt
import random




now = dt.datetime.now()
current_weekday = now.weekday()

if current_weekday == 1:

    with open("quotes.txt") as quotes:
        quotes_list = quotes.read().splitlines()
        random_quote = quotes_list[random.randint(1,100)]

    with smtplib.SMTP("smtp.gmail.com") as connection:

        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject: New Quote! \n\n{random_quote}"
    )
