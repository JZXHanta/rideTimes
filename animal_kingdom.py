import requests
from rich.console import Console
from rich.table import Table
from typing import Union, Dict

base_url: str = 'https://queue-times.com/parks/'
animal_kingdom_url: str = f'{base_url}8/queue_times.json'

request = requests.get(animal_kingdom_url)

data = request.json()

festival_of_the_lion_king: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
}

gorilla_falls_exploration_trail: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][1]["id"],
    "name": data["lands"][0]["rides"][1]["name"],
    "is_open": data["lands"][0]["rides"][1]["is_open"],
    "wait_time": data["lands"][0]["rides"][1]["wait_time"],
    "last_updated": data["lands"][0]["rides"][1]["last_updated"]
}

kilimanjaro_safaris: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][2]["id"],
    "name": data["lands"][0]["rides"][2]["name"],
    "is_open": data["lands"][0]["rides"][2]["is_open"],
    "wait_time": data["lands"][0]["rides"][2]["wait_time"],
    "last_updated": data["lands"][0]["rides"][2]["last_updated"]
}

wildlife_express_train: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][3]["id"],
    "name": data["lands"][0]["rides"][3]["name"],
    "is_open": data["lands"][0]["rides"][3]["is_open"],
    "wait_time": data["lands"][0]["rides"][3]["wait_time"],
    "last_updated": data["lands"][0]["rides"][3]["last_updated"]
}

expedition_everest_legend_of_the_forbidden_mountain: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][0]["id"],
    "name": data["lands"][1]["rides"][0]["name"],
    "is_open": data["lands"][1]["rides"][0]["is_open"],
    "wait_time": data["lands"][1]["rides"][0]["wait_time"],
    "last_updated": data["lands"][1]["rides"][0]["last_updated"]
}

feathered_friends_in_flight: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][1]["id"],
    "name": data["lands"][1]["rides"][1]["name"],
    "is_open": data["lands"][1]["rides"][1]["is_open"],
    "wait_time": data["lands"][1]["rides"][1]["wait_time"],
    "last_updated": data["lands"][1]["rides"][1]["last_updated"]
}

kali_river_rapids: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][2]["id"],
    "name": data["lands"][1]["rides"][2]["name"],
    "is_open": data["lands"][1]["rides"][2]["is_open"],
    "wait_time": data["lands"][1]["rides"][2]["wait_time"],
    "last_updated": data["lands"][1]["rides"][2]["last_updated"]
}

dinosaur: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][0]["id"],
    "name": data["lands"][2]["rides"][0]["name"],
    "is_open": data["lands"][2]["rides"][0]["is_open"],
    "wait_time": data["lands"][2]["rides"][0]["wait_time"],
    "last_updated": data["lands"][2]["rides"][0]["last_updated"]
}

finding_nemo_the_big_blue_and_beyond: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][1]["id"],
    "name": data["lands"][2]["rides"][1]["name"],
    "is_open": data["lands"][2]["rides"][1]["is_open"],
    "wait_time": data["lands"][2]["rides"][1]["wait_time"],
    "last_updated": data["lands"][2]["rides"][1]["last_updated"]
}

the_boneyard: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][2]["id"],
    "name": data["lands"][2]["rides"][2]["name"],
    "is_open": data["lands"][2]["rides"][2]["is_open"],
    "wait_time": data["lands"][2]["rides"][2]["wait_time"],
    "last_updated": data["lands"][2]["rides"][2]["last_updated"]
}

triceratop_spin: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][3]["id"],
    "name": data["lands"][2]["rides"][3]["name"],
    "is_open": data["lands"][2]["rides"][3]["is_open"],
    "wait_time": data["lands"][2]["rides"][3]["wait_time"],
    "last_updated": data["lands"][2]["rides"][3]["last_updated"]
}

its_tough_to_be_a_bug: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][0]["id"],
    "name": data["lands"][3]["rides"][0]["name"],
    "is_open": data["lands"][3]["rides"][0]["is_open"],
    "wait_time": data["lands"][3]["rides"][0]["wait_time"],
    "last_updated": data["lands"][3]["rides"][0]["last_updated"]
}

meet_favorite_disney_pals_at_adventurers_outpost: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][1]["id"],
    "name": data["lands"][3]["rides"][1]["name"],
    "is_open": data["lands"][3]["rides"][1]["is_open"],
    "wait_time": data["lands"][3]["rides"][1]["wait_time"],
    "last_updated": data["lands"][3]["rides"][1]["last_updated"]
}

avatar_flight_of_passage: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][0]["id"],
    "name": data["lands"][4]["rides"][0]["name"],
    "is_open": data["lands"][4]["rides"][0]["is_open"],
    "wait_time": data["lands"][4]["rides"][0]["wait_time"],
    "last_updated": data["lands"][4]["rides"][0]["last_updated"]
}

navi_river_journey: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][1]["id"],
    "name": data["lands"][4]["rides"][1]["name"],
    "is_open": data["lands"][4]["rides"][1]["is_open"],
    "wait_time": data["lands"][4]["rides"][1]["wait_time"],
    "last_updated": data["lands"][4]["rides"][1]["last_updated"]
}

the_animation_experience_at_conservation_station: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][0]["id"],
    "name": data["lands"][5]["rides"][0]["name"],
    "is_open": data["lands"][5]["rides"][0]["is_open"],
    "wait_time": data["lands"][5]["rides"][0]["wait_time"],
    "last_updated": data["lands"][5]["rides"][0]["last_updated"]
}

ratio_of_name_column: int = 6
ratio_of_wait_time_column: int = 1
ratio_of_is_open_column: int = 1
ratio_of_last_updated_column: int = 3
minwidth: int = 38

africa_array: list[Dict[str, Union[str, int, bool]]] = [
    festival_of_the_lion_king,
    gorilla_falls_exploration_trail,
    kilimanjaro_safaris,
    wildlife_express_train
]

asia_array: list[Dict[str, Union[str, int, bool]]] = [
    expedition_everest_legend_of_the_forbidden_mountain,
    feathered_friends_in_flight,
    kali_river_rapids
]

dinoland_usa_array: list[Dict[str, Union[str, int, bool]]] = [
    dinosaur,
    finding_nemo_the_big_blue_and_beyond,
    the_boneyard,
    triceratop_spin
]

discovery_island_array: list[Dict[str, Union[str, int, bool]]] = [
    its_tough_to_be_a_bug,
    meet_favorite_disney_pals_at_adventurers_outpost
]

pandora_the_world_of_avatar_array: list[Dict[str, Union[str, int, bool]]] = [
    avatar_flight_of_passage,
    navi_river_journey
]

rafikis_planet_watch_array: list[Dict[str, Union[str, int, bool]]] = [
    the_animation_experience_at_conservation_station]


def africa() -> None:
    table = Table(title="Africa")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in africa_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def asia() -> None:
    table = Table(title="Asia")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in asia_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def dinoland_usa() -> None:
    table = Table(title="Dinoland U.S.A")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in dinoland_usa_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def discovery_island() -> None:
    table = Table(title="Discovery Island")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in discovery_island_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def pandora_the_world_of_avatar() -> None:
    table = Table(title="Pandora - The World of Avatar")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in pandora_the_world_of_avatar_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def rafikis_planet_watch() -> None:
    table = Table(title="Rafiki's Planet Watch")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in rafikis_planet_watch_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def all_animal_kingdom_tables() -> None:
    africa()
    asia()
    dinoland_usa()
    discovery_island()
    pandora_the_world_of_avatar()
    rafikis_planet_watch()
