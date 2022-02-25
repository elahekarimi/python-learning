import smtplib
my_email = "emailmypython@gmail.com"
password = "890350455"
with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="m.reza.golbaba@gmail.com",
        msg="subject:Elahe karimi\n\n this is my first email that sent to my love with python code"
    )