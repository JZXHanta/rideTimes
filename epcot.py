import requests
from rich.console import Console
from rich.table import Table
import main


base_url = main.base_url
hollywood_studios_url = f'{base_url}5/queue_times.json'

request = requests.get(hollywood_studios_url)

data = request.json()

disney_and_pixar_short_film_festival = dict({
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
})

journey_into_imagination_with_figment = dict({
    "id": data["lands"][0]["rides"][1]["id"],
    "name": data["lands"][0]["rides"][1]["name"],
    "is_open": data["lands"][0]["rides"][1]["is_open"],
    "wait_time": data["lands"][0]["rides"][1]["wait_time"],
    "last_updated": data["lands"][0]["rides"][1]["last_updated"]
})

spaceship_earth = dict({
    "id": data["lands"][0]["rides"][2]["id"],
    "name": data["lands"][0]["rides"][2]["name"],
    "is_open": data["lands"][0]["rides"][2]["is_open"],
    "wait_time": data["lands"][0]["rides"][2]["wait_time"],
    "last_updated": data["lands"][0]["rides"][2]["last_updated"]
})

