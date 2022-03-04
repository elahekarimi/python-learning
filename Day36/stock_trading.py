import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "V5I0H3FNGU6ZDMP7"
NEWS_API_KEY = "8e12d05c365a4cb2b6f0c00679ed052b"
TWILIO_SID = "ACdb6f89eb40266c9202fb6f2c6c52906f"
TWILIO_AUTH_TOKEN = "04f4d2a8098b5ced5088dcb5edfd4ddf"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

recurse = requests.get(STOCK_ENDPOINT, params=parameters)
recurse.raise_for_status()
data = recurse.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]["4. close"]
print(yesterday_data)

day_before_yesterday = data_list[1]["4. close"]
print(day_before_yesterday)

difference = abs(float(yesterday_data) - float (day_before_yesterday))
print(difference)

percentage_difference = (difference / float(yesterday_data)) * 100
print(percentage_difference)

if percentage_difference > 1:
    news_parameters = {
        "apiKey": NEWS_API_KEY,
        "q": COMPANY_NAME,
    }
    new_recponse = requests.get(NEWS_ENDPOINT, params=news_parameters)
    new_recponse.raise_for_status()
    articles = new_recponse.json()["articles"]
    three_article = articles[:3]
    formatted_article = [f"Headline: {articles['title']}. \nBrif: {articles['description']}" for articles in three_article]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
    for articles in formatted_article:
        message = client.messages.create(
            body=articles,
            from_="+16073036354",
            to="+98 935 778 7252"
        )