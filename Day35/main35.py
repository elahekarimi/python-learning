import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "5f18f91b82d1774df98968eaafc3eabd"

account_sid = "ACdb6f89eb40266c9202fb6f2c6c52906f"
auth_token = "5ecd370d828224189c35ce0c70973e38"

parameters = {
    "lat": 54.895061,  # Your latitude
    "lon": -2.933550,  # Your longitude
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

recourse = requests.get(OWN_Endpoint, params=parameters)
recourse.raise_for_status()
weather_data = recourse.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition = hour_data["weather"][0]["id"]
    if int(condition) < 700:
        will_rain = True
if will_rain:
    print("rain is on")
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="rain go on",
        from_="+16073036354",
        to="+989357787252",
    )
    print(message.status)
