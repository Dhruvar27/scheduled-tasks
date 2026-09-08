import datetime as dt
import os
import random
from smtplib import SMTP
import pandas as pd

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

today = dt.datetime.now()
month = today.month
day = today.day

# DEBUG PRINT: Check what day GitHub thinks it is (Remember: GitHub runs on UTC!)
print(f"Today's UTC Date from GitHub -> Month: {month}, Day: {day}")

df = pd.read_csv("birthdays.csv")

for index, row in df.iterrows():
  # DEBUG PRINT: See every row being scanned
  print(
      f"Checking row: {row['name']} (Birthday: {row['month']}/{row['day']})"
  )

  if row.day == day and row.month == month:
    print(f"MATCH FOUND! Sending birthday email to {row['name']}...")

    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path, mode="r") as letter:
      letter_contents = letter.read()

    customised_letter = letter_contents.replace("[NAME]", row["name"].title())
    final_letter = customised_letter.replace("Angela", "Dhruv")

    with SMTP("smtp.gmail.com", port=587) as connection:
      connection.starttls()
      connection.login(user=MY_EMAIL, password=MY_PASSWORD)
      connection.sendmail(
          from_addr=MY_EMAIL,
          to_addrs=row.email,
          msg=f"Subject: Happy Birthday!\n\n{final_letter}",
      )
    print(f"Email successfully sent to {row['name']}!")
