import random
import smtplib
import datetime as dt
import pandas

today = dt.datetime.now()
today_tuple = (today.month, today.day)

my_email = "emailmypython@gmail.com"
password = "890350455"

data = pandas.read_csv("birthdays.csv")
birthday_dic = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthday_dic:
    birthday_person = birthday_dic[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=birthday_person["email"],
                            msg=f"subject: Happy birthday\n\n{contents}"
        )

