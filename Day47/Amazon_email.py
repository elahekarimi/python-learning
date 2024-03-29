import smtplib
import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com/USTO-Changing-Control-Bedroom-Decoration/dp/B09GTM9XTB/ref=lp_19185106011_1_2"
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())
price = soup.find(class_="a-offscreen")

price_text = price.get_text()
price_without_currency = price_text.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)
title = soup.find(id="productTitle").get_text().strip()
print(title)
MY_EMAIL = "emailmypython@gmail.com"
PASSWORD = "890350455"
BUY_PRICE = 20
if price_as_float < BUY_PRICE:
        message = f"{title} is now {price}"

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                result = connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}"
                )
