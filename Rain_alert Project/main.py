import requests
from twilio.rest import Client

account_sid = 'b'
auth_token = 'e'

parameters = {"lat":17.9901,
              "lon":79.59055,
              "cnt":4,
              "appid":"xxxx"}
connection = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
connection.raise_for_status()
data = connection.json()
# print(data)
# print(data["list"][0]["weather"][0]["id"])
for hour_data in data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        Is_rain = True
if Is_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body= "It's going to rain today ,remember to bring an Umbrella",
        from_='xxxxxx',
        to='xxxxxx'
    )

    print(message.status)