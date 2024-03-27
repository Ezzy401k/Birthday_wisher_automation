Day 32 of 100-day Python coding challenge
# Birthday_wisher_automation
This Python program serves as a birthday reminder and email sender. It checks a CSV file for any birthdays matching the current date and sends customized birthday emails to the respective individuals. The email content can be personalized using different letter templates.

## Features

- Checks a CSV file for birthdays matching the current date.
- Sends customized birthday emails to individuals with personalized content.
- Supports multiple letter templates for varied email messages.
- Utilizes SMTP protocol for sending emails securely.

## Requirements

- Python 3
- pandas
- smtplib (Standard Library)
- email (Standard Library)

## Usage

1. Clone the repository:

```bash
git clone https://github.com/Ezzy401k/Birthday_wisher_automation.git
```

2. Navigate to the project directory:

```bash
cd Birthday_wisher_automation
```

3. Make sure you have a CSV file named `birthdays.csv` containing the birthdays and email addresses of individuals in the following format:

```csv
name,email,day,month
John Doe,johndoe@example.com,12,3
Jane Smith,janesmith@example.com,25,5
```

4. Prepare your letter templates in separate text files inside a folder named `letter_templates`.

5. Run the program:

```bash
python Birthday_wisher_automation.py
```

6. If it's someone's birthday today, you will be prompted to enter your email and password for authentication.

7. The program will select a random letter template, personalize it with the recipient's name, and send it via email to the respective individual.

## Author

[Esrael Mekdem](https://github.com/Ezzy401k)
