##################### Extra Hard Starting Project ######################
import pandas as pd
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

now = dt.datetime.now()
data = pd.read_csv("birthdays.csv")

is_today = False
name = ""
email = ""
for index, row in data.iterrows():
    if row.day == now.day and row.month == now.month:
        is_today = True
        name = row['name']
        email = row['email']


letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]
if is_today:

    chosen_letter = random.choice(letter_list)

    with open(chosen_letter) as file:
        letter = file.read()

    letter = letter.replace("[NAME]", f"{name}")

    my_email = input("Email: ")
    password = input("Password: ")

    message = MIMEMultipart()
    message["From"] = my_email
    message["To"] = email
    message["Subject"] = "Happy Birthday!"

    body = letter
    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        # Log in to the account
        server.login(my_email, password)
        # Send the email
        server.sendmail(my_email, email, message.as_string())





