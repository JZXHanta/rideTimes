import requests
from typing import Dict, Union
from rich.console import Console
from rich.table import Table
import main


base_url = main.base_url
hollywood_studios_url = f'{base_url}5/queue_times.json'

request = requests.get(hollywood_studios_url)

data = request.json()

disney_and_pixar_short_film_festival: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
}

journey_into_imagination_with_figment: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][1]["id"],
    "name": data["lands"][0]["rides"][1]["name"],
    "is_open": data["lands"][0]["rides"][1]["is_open"],
    "wait_time": data["lands"][0]["rides"][1]["wait_time"],
    "last_updated": data["lands"][0]["rides"][1]["last_updated"]
}

spaceship_earth: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][2]["id"],
    "name": data["lands"][0]["rides"][2]["name"],
    "is_open": data["lands"][0]["rides"][2]["is_open"],
    "wait_time": data["lands"][0]["rides"][2]["wait_time"],
    "last_updated": data["lands"][0]["rides"][2]["last_updated"]
}

guardians_of_the_galaxy_cosmic_rewind: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][0]["id"],
    "name": data["lands"][1]["rides"][0]["name"],
    "is_open": data["lands"][1]["rides"][0]["is_open"],
    "wait_time": data["lands"][1]["rides"][0]["wait_time"],
    "last_updated": data["lands"][1]["rides"][0]["last_updated"]
}

mission_space: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][1]["id"],
    "name": data["lands"][1]["rides"][1]["name"],
    "is_open": data["lands"][1]["rides"][1]["is_open"],
    "wait_time": data["lands"][1]["rides"][1]["wait_time"],
    "last_updated": data["lands"][1]["rides"][1]["last_updated"]
}

test_track: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][2]["id"],
    "name": data["lands"][1]["rides"][2]["name"],
    "is_open": data["lands"][1]["rides"][2]["is_open"],
    "wait_time": data["lands"][1]["rides"][2]["wait_time"],
    "last_updated": data["lands"][1]["rides"][2]["last_updated"]
}

test_track_single_rider: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][3]["id"],
    "name": data["lands"][1]["rides"][3]["name"],
    "is_open": data["lands"][1]["rides"][3]["is_open"],
    "wait_time": data["lands"][1]["rides"][3]["wait_time"],
    "last_updated": data["lands"][1]["rides"][3]["last_updated"]
}

awesome_planet: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][0]["id"],
    "name": data["lands"][2]["rides"][0]["name"],
    "is_open": data["lands"][2]["rides"][0]["is_open"],
    "wait_time": data["lands"][2]["rides"][0]["wait_time"],
    "last_updated": data["lands"][2]["rides"][0]["last_updated"]
}

journey_of_water_inspired_by_moana: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][1]["id"],
    "name": data["lands"][2]["rides"][1]["name"],
    "is_open": data["lands"][2]["rides"][1]["is_open"],
    "wait_time": data["lands"][2]["rides"][1]["wait_time"],
    "last_updated": data["lands"][2]["rides"][1]["last_updated"]
}

living_with_the_land: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][2]["id"],
    "name": data["lands"][2]["rides"][2]["name"],
    "is_open": data["lands"][2]["rides"][2]["is_open"],
    "wait_time": data["lands"][2]["rides"][2]["wait_time"],
    "last_updated": data["lands"][2]["rides"][2]["last_updated"]
}

soarin_over_california: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][3]["id"],
    "name": data["lands"][2]["rides"][3]["name"],
    "is_open": data["lands"][2]["rides"][3]["is_open"],
    "wait_time": data["lands"][2]["rides"][3]["wait_time"],
    "last_updated": data["lands"][2]["rides"][3]["last_updated"]
}

the_seas_with_nemo_and_friends: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][4]["id"],
    "name": data["lands"][2]["rides"][4]["name"],
    "is_open": data["lands"][2]["rides"][4]["is_open"],
    "wait_time": data["lands"][2]["rides"][4]["wait_time"],
    "last_updated": data["lands"][2]["rides"][4]["last_updated"]
}

turtle_talk_with_crush: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][5]["id"],
    "name": data["lands"][2]["rides"][5]["name"],
    "is_open": data["lands"][2]["rides"][5]["is_open"],
    "wait_time": data["lands"][2]["rides"][5]["wait_time"],
    "last_updated": data["lands"][2]["rides"][5]["last_updated"]
}

canada_far_and_wide_in_circle_vision_360: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][0]["id"],
    "name": data["lands"][3]["rides"][0]["name"],
    "is_open": data["lands"][3]["rides"][0]["is_open"],
    "wait_time": data["lands"][3]["rides"][0]["wait_time"],
    "last_updated": data["lands"][3]["rides"][0]["last_updated"]
}

frozen_ever_after: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][1]["id"],
    "name": data["lands"][3]["rides"][1]["name"],
    "is_open": data["lands"][3]["rides"][1]["is_open"],
    "wait_time": data["lands"][3]["rides"][1]["wait_time"],
    "last_updated": data["lands"][3]["rides"][1]["last_updated"]
}

gran_fiesta_tour_starring_the_three_caballeros: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][2]["id"],
    "name": data["lands"][3]["rides"][2]["name"],
    "is_open": data["lands"][3]["rides"][2]["is_open"],
    "wait_time": data["lands"][3]["rides"][2]["wait_time"],
    "last_updated": data["lands"][3]["rides"][2]["last_updated"]
}

meet_anna_and_elsa_at_royal_sommerhus: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][3]["id"],
    "name": data["lands"][3]["rides"][3]["name"],
    "is_open": data["lands"][3]["rides"][3]["is_open"],
    "wait_time": data["lands"][3]["rides"][3]["wait_time"],
    "last_updated": data["lands"][3]["rides"][3]["last_updated"]
}

remys_ratatouille_adventure: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][4]["id"],
    "name": data["lands"][3]["rides"][4]["name"],
    "is_open": data["lands"][3]["rides"][4]["is_open"],
    "wait_time": data["lands"][3]["rides"][4]["wait_time"],
    "last_updated": data["lands"][3]["rides"][4]["last_updated"]
}

remys_ratatouille_adventure_single_rider: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][5]["id"],
    "name": data["lands"][3]["rides"][5]["name"],
    "is_open": data["lands"][3]["rides"][5]["is_open"],
    "wait_time": data["lands"][3]["rides"][5]["wait_time"],
    "last_updated": data["lands"][3]["rides"][5]["last_updated"]
}

ratio_of_name_column: int = 6
ratio_of_wait_time_column: int = 1
ratio_of_is_open_column: int = 1
ratio_of_last_updated_column: int = 3
minwidth: int = 38

world_celebration_array: list[Dict[str, Union[str, int, bool]]] = [
    disney_and_pixar_short_film_festival,
    journey_into_imagination_with_figment,
    spaceship_earth
]

world_discovery_array: list[Dict[str, Union[str, int, bool]]] = [
    guardians_of_the_galaxy_cosmic_rewind,
    mission_space,
    test_track,
    test_track_single_rider
]

world_nature_array: list[Dict[str, Union[str, int, bool]]] = [
    awesome_planet,
    journey_of_water_inspired_by_moana,
    living_with_the_land,
    soarin_over_california,
    the_seas_with_nemo_and_friends,
    turtle_talk_with_crush
]

world_showcase_array: list[Dict[str, Union[str, int, bool]]] = [
    canada_far_and_wide_in_circle_vision_360,
    frozen_ever_after,
    gran_fiesta_tour_starring_the_three_caballeros,
    meet_anna_and_elsa_at_royal_sommerhus,
    remys_ratatouille_adventure,
    remys_ratatouille_adventure_single_rider
]


def world_celebration():
    table = Table(title="World Celebration")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in world_celebration_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def world_discovery():
    table = Table(title="World Discovery")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in world_discovery_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def world_nature():
    table = Table(title="World Nature")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in world_nature_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def world_showcase():
    table = Table(title="World Showcase")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in world_showcase_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def all_epcot_tables():
    world_celebration()
    world_discovery()
    world_nature()
    world_showcase()
