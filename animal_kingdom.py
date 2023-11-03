import requests
from rich.console import Console
from rich.table import Table

base_url = 'https://queue-times.com/parks/'
animal_kingdom_url = f'{base_url}8/queue_times.json'

request = requests.get(animal_kingdom_url)

data = request.json()

festival_of_the_lion_king = dict({
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
})