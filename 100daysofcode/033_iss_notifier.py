import datetime

import requests

lat = 50.0804924
lng = 19.9599390
params = {"lat": lat, "lng": lng, "formatted": 0}
response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()

results = response.json()["results"]
sunrise = datetime.datetime.fromisoformat(results["sunrise"])
sunset = datetime.datetime.fromisoformat(results["sunset"])

seconds = (sunset - sunrise).seconds
minutes, seconds = divmod(seconds, 60)
hours, minutes = divmod(minutes, 60)
day_length = datetime.time(hours, minutes, seconds)

print(
    f"Sunrise is at {sunrise.time()}. "
    f"Sunset is at {sunset.time()}. "
    f"Day length is {day_length}"
)
