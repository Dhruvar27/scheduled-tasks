import os

from smtplib import SMTP
from calendar import week, weekday

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")


import datetime as dt
import random




today = dt.datetime.now()
month = today.month
day = today.day
file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
import pandas as pd
df = pd.read_csv("birthdays.csv")
for index, row in df.iterrows():
    if row.day == day and row.month == month:
        with open(file_path, mode="r") as letter:
            letter_contents = letter.read()

    # Now .replace() will work perfectly!
            customised_letter = letter_contents.replace("[NAME]", row["name"].title())
            final_letter = customised_letter.replace("Angela", "Dhruv")

            with SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=row.email,
                    msg=f"Subject: Happy birthday! \n\n{final_letter}")
