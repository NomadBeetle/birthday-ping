import pandas
import datetime
import smtplib
import random
import os
from dotenv import load_dotenv

# Load email credentials from .env file
load_dotenv()
MYEMAIL = os.getenv("EMAIL")
MYPASSWORD = os.getenv("PASSWORD")

# Constants
LETTERS = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]

# Read the birthdays CSV
data = pandas.read_csv("birthdays.csv")
dataDict = data.set_index("name").to_dict(orient="index")

# Get today's date
current = datetime.datetime.now()
currentDate = current.day
currentMonth = current.month

# Send birthday emails
try:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MYEMAIL, password=MYPASSWORD)

        for name, info in dataDict.items():
            if info["month"] == currentMonth and info["day"] == currentDate:
                with open(f"letter_templates/{random.choice(LETTERS)}") as file:
                    text = file.read()
                    personalized_text = text.replace("[NAME]", name)

                connection.sendmail(
                    from_addr=MYEMAIL,
                    to_addrs=info["email"],
                    msg=f"Subject: Happy Birthday!\n\n{personalized_text}"
                )
                print(f"✅ Email sent to {name} at {info['email']}")
except Exception as e:
    print(f"❌ Failed to send emails: {e}")
