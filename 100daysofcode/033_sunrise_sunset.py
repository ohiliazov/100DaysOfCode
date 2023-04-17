import time
from datetime import datetime
from typing import Tuple

import pytz
import requests

MY_LAT = 50.0804924
MY_LONG = 19.9599390
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}


def get_iss_position() -> Tuple[float, float]:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    return iss_latitude, iss_longitude


def get_sunrise_sunset() -> Tuple[datetime, datetime]:
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = datetime.fromisoformat(data["results"]["sunrise"])
    sunset = datetime.fromisoformat(data["results"]["sunset"])

    return sunrise, sunset


def is_iss_close(lat, long):
    if abs(lat - MY_LAT) <= 5 and abs(long - MY_LONG) <= 5:
        return True
    print(f"ISS is {abs(lat - MY_LAT)} lat, {abs(long - MY_LONG)} long away.")


def is_currently_dark(sunrise, sunset):
    time_now = pytz.utc.localize(datetime.utcnow())

    if time_now < sunrise or time_now > sunset:
        return True

    print("It's still dark.")
    print(f"Sunset is at {sunset.timetz()}")


while True:
    iss_latitude, iss_longitude = get_iss_position()
    sunrise, sunset = get_sunrise_sunset()

    if is_iss_close(iss_latitude, iss_longitude):
        if is_currently_dark(sunrise, sunset):
            print("Look up!")

    time.sleep(60)
