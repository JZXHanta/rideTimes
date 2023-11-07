import requests
from typing import Dict, Union
from rich.console import Console
from rich.table import Table

base_url = 'https://queue-times.com/parks/'
hollywood_studios_url = f'{base_url}7/queue_times.json'

request = requests.get(hollywood_studios_url)

data = request.json()

disney_jr_play_and_dance: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
}

meet_sully_at_walt_disney_presents: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][1]["id"],
    "name": data["lands"][0]["rides"][1]["name"],
    "is_open": data["lands"][0]["rides"][1]["is_open"],
    "wait_time": data["lands"][0]["rides"][1]["wait_time"],
    "last_updated": data["lands"][0]["rides"][1]["last_updated"]
}

walt_disney_presents: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][2]["id"],
    "name": data["lands"][0]["rides"][2]["name"],
    "is_open": data["lands"][0]["rides"][2]["is_open"],
    "wait_time": data["lands"][0]["rides"][2]["wait_time"],
    "last_updated": data["lands"][0]["rides"][2]["last_updated"]
}

meet_disney_stars_at_red_carpet_dreams: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][0]["id"],
    "name": data["lands"][1]["rides"][0]["name"],
    "is_open": data["lands"][1]["rides"][0]["is_open"],
    "wait_time": data["lands"][1]["rides"][0]["wait_time"],
    "last_updated": data["lands"][1]["rides"][0]["last_updated"]
}

frozen_sing_along: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][0]["id"],
    "name": data["lands"][2]["rides"][0]["name"],
    "is_open": data["lands"][2]["rides"][0]["is_open"],
    "wait_time": data["lands"][2]["rides"][0]["wait_time"],
    "last_updated": data["lands"][2]["rides"][0]["last_updated"]
}

indiana_jones_epic_stunt_spectacular: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][1]["id"],
    "name": data["lands"][2]["rides"][1]["name"],
    "is_open": data["lands"][2]["rides"][1]["is_open"],
    "wait_time": data["lands"][2]["rides"][1]["wait_time"],
    "last_updated": data["lands"][2]["rides"][1]["last_updated"]
}

meet_olaf_at_celebrity_spotlight: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][2]["id"],
    "name": data["lands"][2]["rides"][2]["name"],
    "is_open": data["lands"][2]["rides"][2]["is_open"],
    "wait_time": data["lands"][2]["rides"][2]["wait_time"],
    "last_updated": data["lands"][2]["rides"][2]["last_updated"]
}

star_tours: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][3]["id"],
    "name": data["lands"][2]["rides"][3]["name"],
    "is_open": data["lands"][2]["rides"][3]["is_open"],
    "wait_time": data["lands"][2]["rides"][3]["wait_time"],
    "last_updated": data["lands"][2]["rides"][3]["last_updated"]
}

vacation_fun: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][4]["id"],
    "name": data["lands"][2]["rides"][4]["name"],
    "is_open": data["lands"][2]["rides"][4]["is_open"],
    "wait_time": data["lands"][2]["rides"][4]["wait_time"],
    "last_updated": data["lands"][2]["rides"][4]["last_updated"]
}

mickey_and_minnies_runaway_railway: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][0]["id"],
    "name": data["lands"][3]["rides"][0]["name"],
    "is_open": data["lands"][3]["rides"][0]["is_open"],
    "wait_time": data["lands"][3]["rides"][0]["wait_time"],
    "last_updated": data["lands"][3]["rides"][0]["last_updated"]
}

muppet_vision_3d: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][0]["id"],
    "name": data["lands"][4]["rides"][0]["name"],
    "is_open": data["lands"][4]["rides"][0]["is_open"],
    "wait_time": data["lands"][4]["rides"][0]["wait_time"],
    "last_updated": data["lands"][4]["rides"][0]["last_updated"]
}

toy_story_mania: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][0]["id"],
    "name": data["lands"][5]["rides"][0]["name"],
    "is_open": data["lands"][5]["rides"][0]["is_open"],
    "wait_time": data["lands"][5]["rides"][0]["wait_time"],
    "last_updated": data["lands"][5]["rides"][0]["last_updated"]
}

millennium_falcon_smugglers_run: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][6]["rides"][0]["id"],
    "name": data["lands"][6]["rides"][0]["name"],
    "is_open": data["lands"][6]["rides"][0]["is_open"],
    "wait_time": data["lands"][6]["rides"][0]["wait_time"],
    "last_updated": data["lands"][6]["rides"][0]["last_updated"]
}

millennium_falcon_smugglers_run_single_rider: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][6]["rides"][1]["id"],
    "name": data["lands"][6]["rides"][1]["name"],
    "is_open": data["lands"][6]["rides"][1]["is_open"],
    "wait_time": data["lands"][6]["rides"][1]["wait_time"],
    "last_updated": data["lands"][6]["rides"][1]["last_updated"]
}

star_wars_rise_of_the_resistance: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][6]["rides"][0]["id"],
    "name": data["lands"][6]["rides"][0]["name"],
    "is_open": data["lands"][6]["rides"][0]["is_open"],
    "wait_time": data["lands"][6]["rides"][0]["wait_time"],
    "last_updated": data["lands"][6]["rides"][0]["last_updated"]
}

beauty_and_the_beast_live_on_stage: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][7]["rides"][0]["id"],
    "name": data["lands"][7]["rides"][0]["name"],
    "is_open": data["lands"][7]["rides"][0]["is_open"],
    "wait_time": data["lands"][7]["rides"][0]["wait_time"],
    "last_updated": data["lands"][7]["rides"][0]["last_updated"]
}

lightning_mcqueens_racing_academy: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][7]["rides"][1]["id"],
    "name": data["lands"][7]["rides"][1]["name"],
    "is_open": data["lands"][7]["rides"][1]["is_open"],
    "wait_time": data["lands"][7]["rides"][1]["wait_time"],
    "last_updated": data["lands"][7]["rides"][1]["last_updated"]
}

rock_n_roller_coaster_starring_aerosmith: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][7]["rides"][2]["id"],
    "name": data["lands"][7]["rides"][2]["name"],
    "is_open": data["lands"][7]["rides"][2]["is_open"],
    "wait_time": data["lands"][7]["rides"][2]["wait_time"],
    "last_updated": data["lands"][7]["rides"][2]["last_updated"]
}

rock_n_roller_coaster_starring_aerosmith_single_rider: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][7]["rides"][3]["id"],
    "name": data["lands"][7]["rides"][3]["name"],
    "is_open": data["lands"][7]["rides"][3]["is_open"],
    "wait_time": data["lands"][7]["rides"][3]["wait_time"],
    "last_updated": data["lands"][7]["rides"][3]["last_updated"]
}

twilight_zone_tower_of_terror: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][7]["rides"][4]["id"],
    "name": data["lands"][7]["rides"][4]["name"],
    "is_open": data["lands"][7]["rides"][4]["is_open"],
    "wait_time": data["lands"][7]["rides"][4]["wait_time"],
    "last_updated": data["lands"][7]["rides"][4]["last_updated"]
}

alien_swirling_saucers: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][8]["rides"][0]["id"],
    "name": data["lands"][8]["rides"][0]["name"],
    "is_open": data["lands"][8]["rides"][0]["is_open"],
    "wait_time": data["lands"][8]["rides"][0]["wait_time"],
    "last_updated": data["lands"][8]["rides"][0]["last_updated"]
}

slinky_dog_dash: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][8]["rides"][1]["id"],
    "name": data["lands"][8]["rides"][1]["name"],
    "is_open": data["lands"][8]["rides"][1]["is_open"],
    "wait_time": data["lands"][8]["rides"][1]["wait_time"],
    "last_updated": data["lands"][8]["rides"][1]["last_updated"]
}

ratio_of_name_column: int = 6
ratio_of_wait_time_column: int = 1
ratio_of_is_open_column: int = 1
ratio_of_last_updated_column: int = 3
minwidth: int = 38

animation_courtyard_array: list[Dict[str, Union[str, int, bool]]] = [
    disney_jr_play_and_dance,
    meet_sully_at_walt_disney_presents,
    walt_disney_presents
]

commissary_lane_array: list[Dict[str, Union[str, int, bool]]] = [
    meet_disney_stars_at_red_carpet_dreams
]

echo_lake_array: list[Dict[str, Union[str, int, bool]]] = [
    frozen_sing_along,
    indiana_jones_epic_stunt_spectacular,
    meet_olaf_at_celebrity_spotlight,
    star_tours,
    vacation_fun
]

hollywood_boulevard_array: list[Dict[str, Union[str, int, bool]]] = [
    mickey_and_minnies_runaway_railway
]

muppet_courtyard_array: list[Dict[str, Union[str, int, bool]]] = [
    muppet_vision_3d
]

pixar_place_array: list[Dict[str, Union[str, int, bool]]] = [
    toy_story_mania
]

star_wars_galaxy_edge_array: list[Dict[str, Union[str, int, bool]]] = [
    millennium_falcon_smugglers_run,
    millennium_falcon_smugglers_run_single_rider,
    star_wars_rise_of_the_resistance
]

sunset_boulevard_array: list[Dict[str, Union[str, int, bool]]] = [
    beauty_and_the_beast_live_on_stage,
    lightning_mcqueens_racing_academy,
    rock_n_roller_coaster_starring_aerosmith,
    rock_n_roller_coaster_starring_aerosmith_single_rider,
    twilight_zone_tower_of_terror
]

toy_story_land_array: list[Dict[str, Union[str, int, bool]]] = [
    alien_swirling_saucers,
    slinky_dog_dash
]


def animation_courtyard() -> None:
    table = Table(title="Animation Courtyard")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in animation_courtyard_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def commissary_lane() -> None:
    table = Table(title="Commissary Lane")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in commissary_lane_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def echo_lake() -> None:
    table = Table(title="Echo Lake")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in echo_lake_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def hollywood_boulevard() -> None:
    table = Table(title="Hollywood Boulevard")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in hollywood_boulevard_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def muppet_courtyard() -> None:
    table = Table(title="Muppet Courtyard")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in muppet_courtyard_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def pixar_place() -> None:
    table = Table(title="Pixar Place")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in pixar_place_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def star_wars_galaxy_edge() -> None:
    table = Table(title="Star Wars: Galaxy's Edge")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in star_wars_galaxy_edge_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def sunset_boulevard() -> None:
    table = Table(title="Sunset Boulevard")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in sunset_boulevard_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def toy_story_land() -> None:
    table = Table(title="Toy Story Land")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True, ratio=ratio_of_name_column,
                     min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in toy_story_land_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    print("\n")
    console = Console()
    console.print(table)


def all_hollywood_studios_tables() -> None:
    animation_courtyard()
    commissary_lane()
    echo_lake()
    hollywood_boulevard()
    muppet_courtyard()
    pixar_place()
    star_wars_galaxy_edge()
    sunset_boulevard()
    toy_story_land()


# all_hollywood_studios_tables()
