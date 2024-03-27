import pandas as pd
import datetime as dt
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Get current date and time
now = dt.datetime.now()

try:
    # Read birthday data from the CSV file
    data = pd.read_csv("birthdays.csv")

    # Initialize variables to store birthday person's name and email
    is_today = False
    name = ""
    email = ""

    # Iterate over each row in the data
    for index, row in data.iterrows():
        # Check if today's date matches the birthday
        if row.day == now.day and row.month == now.month:
            is_today = True
            name = row['name']
            email = row['email']

    # List of letter templates
    letter_list = ["letter_templates/letter_1.txt", "letter_templates/letter_2.txt", "letter_templates/letter_3.txt"]

    # If today is someone's birthday
    if is_today:
        chosen_letter = ''
        try:
            # Choose a random letter template
            chosen_letter = random.choice(letter_list)

            # Read the content of the chosen letter template
            with open(chosen_letter) as file:
                letter = file.read()

            # Replace placeholder with the birthday person's name
            letter = letter.replace("[NAME]", f"{name}")

            # Input sender's email and password
            my_email = input("Email: ")
            password = input("Password: ")

            # Create a MIME multipart message
            message = MIMEMultipart()
            message["From"] = my_email
            message["To"] = email
            message["Subject"] = "Happy Birthday!"

            # Set the body of the email to be the content of the letter
            body = letter
            message.attach(MIMEText(body, "plain"))

            # Connect to SMTP server and send the email
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                # Log in to the sender's email account
                server.login(my_email, password)
                # Send the email
                server.sendmail(my_email, email, message.as_string())
        except FileNotFoundError:
            print(f"{chosen_letter} not found")

except FileNotFoundError:
    print("Please check if the file 'birthday.csv' exists.")
