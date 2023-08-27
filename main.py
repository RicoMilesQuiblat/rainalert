import requests
from twilio.rest import Client
KEY = "69f04e4613056b159c2761a9d9e664d2"
MY_LAT = 9.945940
MY_LNG = 123.618990
phone = "+18147475639"
account_sid = 'AC62fb8713b31121873d414bfb3257e2db'
auth_token = '828d782b098af5e78cc9c73558247c2c'


parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": KEY,
    "exclude": "current,minutely,daily"

}


client = Client(account_sid, auth_token)
response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
weather_ids = []
hourly_data = data["hourly"][:12]
will_rain = False


for hour in hourly_data:
    condition = hour["weather"][0]["id"]
    if int(condition) < 800:
        will_rain = True
        break

if will_rain:
    message = client.messages.create(
        from_=phone,
        body="It will rain today, Please bring an ☔",
        to="+639184822197"
    )

