import requests
from twilio.rest import Client

account_sid = "Your twilio SID key"
auth_token ="Your authemtication key"


API_END_POINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "Your API key"

forcast = {
    "lat": 0.0000,  # Your latitude
    "lon": 0.0000,  # Your longitude
    "appid": API_KEY,
    "cnt": 4,
}

will_rain = False
response = requests.get(API_END_POINT, params=forcast)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to be raining today, don't forget to take an ☂️ with you :)",
        from_="your number in twilio",
        to="your phone number",
    )
    print(message.status)