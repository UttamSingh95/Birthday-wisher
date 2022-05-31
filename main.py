##################### Normal Starting Project ######################

import datetime as dt
import pandas
import random
import smtplib

my_gmail = "u*******4@gmail.com"
password = "A********$"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
print(today)
data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]", birthday_person["name"])
    print(content)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_gmail, password=password)
        connection.sendmail(
            from_addr=my_gmail,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday\n\n{content}"
        )
