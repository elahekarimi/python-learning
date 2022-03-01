import requests

MY_LAT = 35.689198
MY_LOG = 51.388973

parameters = {
    "lat": MY_LAT,
    "log": MY_LOG
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
