
from typing import Dict, Union
import requests
from rich.console import Console
from rich.table import Table


base_url: str = 'https://queue-times.com/parks/'
magic_kingdom_url: str = f'{base_url}6/queue_times.json'

request = requests.get(magic_kingdom_url)

data = request.json()

a_pirates_adventure_treasures_of_the_seven_seas: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][0]["id"],
    "name": data["lands"][0]["rides"][0]["name"],
    "is_open": data["lands"][0]["rides"][0]["is_open"],
    "wait_time": data["lands"][0]["rides"][0]["wait_time"],
    "last_updated": data["lands"][0]["rides"][0]["last_updated"]
}

jungle_cruise: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][1]["id"],
    "name": data["lands"][0]["rides"][1]["name"],
    "is_open": data["lands"][0]["rides"][1]["is_open"],
    "wait_time": data["lands"][0]["rides"][1]["wait_time"],
    "last_updated": data["lands"][0]["rides"][1]["last_updated"]
}

pirates_of_the_caribbean: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][2]["id"],
    "name": data["lands"][0]["rides"][2]["name"],
    "is_open": data["lands"][0]["rides"][2]["is_open"],
    "wait_time": data["lands"][0]["rides"][2]["wait_time"],
    "last_updated": data["lands"][0]["rides"][2]["last_updated"]
}

swiss_family_treehouse: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][3]["id"],
    "name": data["lands"][0]["rides"][3]["name"],
    "is_open": data["lands"][0]["rides"][3]["is_open"],
    "wait_time": data["lands"][0]["rides"][3]["wait_time"],
    "last_updated": data["lands"][0]["rides"][3]["last_updated"]
}

the_magic_carpets_of_aladdin: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][4]["id"],
    "name": data["lands"][0]["rides"][4]["name"],
    "is_open": data["lands"][0]["rides"][4]["is_open"],
    "wait_time": data["lands"][0]["rides"][4]["wait_time"],
    "last_updated": data["lands"][0]["rides"][4]["last_updated"]
}

walt_disneys_enchanted_tiki_room: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][0]["rides"][5]["id"],
    "name": data["lands"][0]["rides"][5]["name"],
    "is_open": data["lands"][0]["rides"][5]["is_open"],
    "wait_time": data["lands"][0]["rides"][5]["wait_time"],
    "last_updated": data["lands"][0]["rides"][5]["last_updated"]
}

its_a_small_world: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][0]["id"],
    "name": data["lands"][1]["rides"][0]["name"],
    "is_open": data["lands"][1]["rides"][0]["is_open"],
    "wait_time": data["lands"][1]["rides"][0]["wait_time"],
    "last_updated": data["lands"][1]["rides"][0]["last_updated"]
}

dumbo_the_flying_elephant: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][1]["id"],
    "name": data["lands"][1]["rides"][1]["name"],
    "is_open": data["lands"][1]["rides"][1]["is_open"],
    "wait_time": data["lands"][1]["rides"][1]["wait_time"],
    "last_updated": data["lands"][1]["rides"][1]["last_updated"]
}

enchanted_tales_with_belle: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][2]["id"],
    "name": data["lands"][1]["rides"][2]["name"],
    "is_open": data["lands"][1]["rides"][2]["is_open"],
    "wait_time": data["lands"][1]["rides"][2]["wait_time"],
    "last_updated": data["lands"][1]["rides"][2]["last_updated"]
}

mad_tea_party: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][3]["id"],
    "name": data["lands"][1]["rides"][3]["name"],
    "is_open": data["lands"][1]["rides"][3]["is_open"],
    "wait_time": data["lands"][1]["rides"][3]["wait_time"],
    "last_updated": data["lands"][1]["rides"][3]["last_updated"]
}

meet_ariel_at_her_grotto: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][4]["id"],
    "name": data["lands"][1]["rides"][4]["name"],
    "is_open": data["lands"][1]["rides"][4]["is_open"],
    "wait_time": data["lands"][1]["rides"][4]["wait_time"],
    "last_updated": data["lands"][1]["rides"][4]["last_updated"]
}

meet_cinderella_and_a_visiting_princess_at_princess_fairytale_hall: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][5]["id"],
    "name": data["lands"][1]["rides"][5]["name"],
    "is_open": data["lands"][1]["rides"][5]["is_open"],
    "wait_time": data["lands"][1]["rides"][5]["wait_time"],
    "last_updated": data["lands"][1]["rides"][5]["last_updated"]
}

meet_daring_disney_pals_as_circus_stars_at_petes_silly_sideshow: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][6]["id"],
    "name": data["lands"][1]["rides"][6]["name"],
    "is_open": data["lands"][1]["rides"][6]["is_open"],
    "wait_time": data["lands"][1]["rides"][6]["wait_time"],
    "last_updated": data["lands"][1]["rides"][6]["last_updated"]
}

meet_dashing_disney_pals_as_circus_stars_at_petes_silly_sideshow: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][7]["id"],
    "name": data["lands"][1]["rides"][7]["name"],
    "is_open": data["lands"][1]["rides"][7]["is_open"],
    "wait_time": data["lands"][1]["rides"][7]["wait_time"],
    "last_updated": data["lands"][1]["rides"][7]["last_updated"]
}

meet_princess_tiana_and_a_visiting_princess_at_princess_fairytale_hall: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][8]["id"],
    "name": data["lands"][1]["rides"][8]["name"],
    "is_open": data["lands"][1]["rides"][8]["is_open"],
    "wait_time": data["lands"][1]["rides"][8]["wait_time"],
    "last_updated": data["lands"][1]["rides"][8]["last_updated"]
}

mickeys_philharmagic: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][9]["id"],
    "name": data["lands"][1]["rides"][9]["name"],
    "is_open": data["lands"][1]["rides"][9]["is_open"],
    "wait_time": data["lands"][1]["rides"][9]["wait_time"],
    "last_updated": data["lands"][1]["rides"][9]["last_updated"]
}

peter_pans_flight: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][10]["id"],
    "name": data["lands"][1]["rides"][10]["name"],
    "is_open": data["lands"][1]["rides"][10]["is_open"],
    "wait_time": data["lands"][1]["rides"][10]["wait_time"],
    "last_updated": data["lands"][1]["rides"][10]["last_updated"]
}

prince_charming_regal_carrousel: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][11]["id"],
    "name": data["lands"][1]["rides"][11]["name"],
    "is_open": data["lands"][1]["rides"][11]["is_open"],
    "wait_time": data["lands"][1]["rides"][11]["wait_time"],
    "last_updated": data["lands"][1]["rides"][11]["last_updated"]
}

seven_dwarfs_mine_train: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][12]["id"],
    "name": data["lands"][1]["rides"][12]["name"],
    "is_open": data["lands"][1]["rides"][12]["is_open"],
    "wait_time": data["lands"][1]["rides"][12]["wait_time"],
    "last_updated": data["lands"][1]["rides"][12]["last_updated"]
}

the_barnstormer: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][13]["id"],
    "name": data["lands"][1]["rides"][13]["name"],
    "is_open": data["lands"][1]["rides"][13]["is_open"],
    "wait_time": data["lands"][1]["rides"][13]["wait_time"],
    "last_updated": data["lands"][1]["rides"][13]["last_updated"]
}

the_many_adventures_of_winnie_the_pooh: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][14]["id"],
    "name": data["lands"][1]["rides"][14]["name"],
    "is_open": data["lands"][1]["rides"][14]["is_open"],
    "wait_time": data["lands"][1]["rides"][14]["wait_time"],
    "last_updated": data["lands"][1]["rides"][14]["last_updated"]
}

under_the_sea_journey_of_the_little_mermaid: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][15]["id"],
    "name": data["lands"][1]["rides"][15]["name"],
    "is_open": data["lands"][1]["rides"][15]["is_open"],
    "wait_time": data["lands"][1]["rides"][15]["wait_time"],
    "last_updated": data["lands"][1]["rides"][15]["last_updated"]}

walt_disney_world_railroad_fantasyland: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][1]["rides"][16]["id"],
    "name": data["lands"][1]["rides"][16]["name"],
    "is_open": data["lands"][1]["rides"][16]["is_open"],
    "wait_time": data["lands"][1]["rides"][16]["wait_time"],
    "last_updated": data["lands"][1]["rides"][16]["last_updated"]
}

big_thunder_mountain: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][0]["id"],
    "name": data["lands"][2]["rides"][0]["name"],
    "is_open": data["lands"][2]["rides"][0]["is_open"],
    "wait_time": data["lands"][2]["rides"][0]["wait_time"],
    "last_updated": data["lands"][2]["rides"][0]["last_updated"]
}

country_bear_jamboree: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][1]["id"],
    "name": data["lands"][2]["rides"][1]["name"],
    "is_open": data["lands"][2]["rides"][1]["is_open"],
    "wait_time": data["lands"][2]["rides"][1]["wait_time"],
    "last_updated": data["lands"][2]["rides"][1]["last_updated"]
}

splash_mountain: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][2]["id"],
    "name": data["lands"][2]["rides"][2]["name"],
    "is_open": data["lands"][2]["rides"][2]["is_open"],
    "wait_time": data["lands"][2]["rides"][2]["wait_time"],
    "last_updated": data["lands"][2]["rides"][2]["last_updated"]
}

tom_sawyer_island: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][3]["id"],
    "name": data["lands"][2]["rides"][3]["name"],
    "is_open": data["lands"][2]["rides"][3]["is_open"],
    "wait_time": data["lands"][2]["rides"][3]["wait_time"],
    "last_updated": data["lands"][2]["rides"][3]["last_updated"]
}

walt_disney_world_railroad_frontierland: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][2]["rides"][4]["id"],
    "name": data["lands"][2]["rides"][4]["name"],
    "is_open": data["lands"][2]["rides"][4]["is_open"],
    "wait_time": data["lands"][2]["rides"][4]["wait_time"],
    "last_updated": data["lands"][2]["rides"][4]["last_updated"]
}

haunted_mansion: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][0]["id"],
    "name": data["lands"][3]["rides"][0]["name"],
    "is_open": data["lands"][3]["rides"][0]["is_open"],
    "wait_time": data["lands"][3]["rides"][0]["wait_time"],
    "last_updated": data["lands"][3]["rides"][0]["last_updated"]
}

liberty_square_riverboat: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][1]["id"],
    "name": data["lands"][3]["rides"][1]["name"],
    "is_open": data["lands"][3]["rides"][1]["is_open"],
    "wait_time": data["lands"][3]["rides"][1]["wait_time"],
    "last_updated": data["lands"][3]["rides"][1]["last_updated"]
}

the_hall_of_presidents: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][3]["rides"][2]["id"],
    "name": data["lands"][3]["rides"][2]["name"],
    "is_open": data["lands"][3]["rides"][2]["is_open"],
    "wait_time": data["lands"][3]["rides"][2]["wait_time"],
    "last_updated": data["lands"][3]["rides"][2]["last_updated"]
}

disney_festival_of_fantasy_parade: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][0]["id"],
    "name": data["lands"][4]["rides"][0]["name"],
    "is_open": data["lands"][4]["rides"][0]["is_open"],
    "wait_time": data["lands"][4]["rides"][0]["wait_time"],
    "last_updated": data["lands"][4]["rides"][0]["last_updated"]
}

meet_mickey_at_town_square_theater: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][1]["id"],
    "name": data["lands"][4]["rides"][1]["name"],
    "is_open": data["lands"][4]["rides"][1]["is_open"],
    "wait_time": data["lands"][4]["rides"][1]["wait_time"],
    "last_updated": data["lands"][4]["rides"][1]["last_updated"]
}

walt_disney_world_railroad_main_street_usa: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][4]["rides"][2]["id"],
    "name": data["lands"][4]["rides"][2]["name"],
    "is_open": data["lands"][4]["rides"][2]["is_open"],
    "wait_time": data["lands"][4]["rides"][2]["wait_time"],
    "last_updated": data["lands"][4]["rides"][2]["last_updated"]
}

astro_orbiter: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][0]["id"],
    "name": data["lands"][5]["rides"][0]["name"],
    "is_open": data["lands"][5]["rides"][0]["is_open"],
    "wait_time": data["lands"][5]["rides"][0]["wait_time"],
    "last_updated": data["lands"][5]["rides"][0]["last_updated"]
}

buzz_lightyear_space_ranger_spin: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][1]["id"],
    "name": data["lands"][5]["rides"][1]["name"],
    "is_open": data["lands"][5]["rides"][1]["is_open"],
    "wait_time": data["lands"][5]["rides"][1]["wait_time"],
    "last_updated": data["lands"][5]["rides"][1]["last_updated"]
}

monster_inc_laugh_floor: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][2]["id"],
    "name": data["lands"][5]["rides"][2]["name"],
    "is_open": data["lands"][5]["rides"][2]["is_open"],
    "wait_time": data["lands"][5]["rides"][2]["wait_time"],
    "last_updated": data["lands"][5]["rides"][2]["last_updated"]
}

space_mountain: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][3]["id"],
    "name": data["lands"][5]["rides"][3]["name"],
    "is_open": data["lands"][5]["rides"][3]["is_open"],
    "wait_time": data["lands"][5]["rides"][3]["wait_time"],
    "last_updated": data["lands"][5]["rides"][3]["last_updated"]
}

tomorrowland_speedway: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][4]["id"],
    "name": data["lands"][5]["rides"][4]["name"],
    "is_open": data["lands"][5]["rides"][4]["is_open"],
    "wait_time": data["lands"][5]["rides"][4]["wait_time"],
    "last_updated": data["lands"][5]["rides"][4]["last_updated"]
}

tomorrowland_transit_authority_peoplemover: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][5]["id"],
    "name": data["lands"][5]["rides"][5]["name"],
    "is_open": data["lands"][5]["rides"][5]["is_open"],
    "wait_time": data["lands"][5]["rides"][5]["wait_time"],
    "last_updated": data["lands"][5]["rides"][5]["last_updated"]
}

tron_lightcycle_run: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][6]["id"],
    "name": data["lands"][5]["rides"][6]["name"],
    "is_open": data["lands"][5]["rides"][6]["is_open"],
    "wait_time": data["lands"][5]["rides"][6]["wait_time"],
    "last_updated": data["lands"][5]["rides"][6]["last_updated"]
}

walt_disneys_carousel_of_progress: Dict[str, Union[str, int, bool]] = {
    "id": data["lands"][5]["rides"][7]["id"],
    "name": data["lands"][5]["rides"][7]["name"],
    "is_open": data["lands"][5]["rides"][7]["is_open"],
    "wait_time": data["lands"][5]["rides"][7]["wait_time"],
    "last_updated": data["lands"][5]["rides"][7]["last_updated"]
}

ratio_of_name_column: int = 6
ratio_of_wait_time_column: int = 1
ratio_of_is_open_column: int = 1
ratio_of_last_updated_column: int = 3
minwidth: int = 38

adventureland_array: list[Dict[str, Union[str, int, bool]]] = [
    a_pirates_adventure_treasures_of_the_seven_seas,
    jungle_cruise,
    pirates_of_the_caribbean,
    swiss_family_treehouse,
    the_magic_carpets_of_aladdin,
    walt_disneys_enchanted_tiki_room
]

fantasyland_array: list[Dict[str, Union[str, int, bool]]] = [
    its_a_small_world,
    dumbo_the_flying_elephant,
    enchanted_tales_with_belle,
    mad_tea_party,
    meet_ariel_at_her_grotto,
    meet_cinderella_and_a_visiting_princess_at_princess_fairytale_hall,
    meet_daring_disney_pals_as_circus_stars_at_petes_silly_sideshow,
    meet_dashing_disney_pals_as_circus_stars_at_petes_silly_sideshow,
    meet_princess_tiana_and_a_visiting_princess_at_princess_fairytale_hall,
    mickeys_philharmagic,
    peter_pans_flight,
    prince_charming_regal_carrousel,
    seven_dwarfs_mine_train,
    the_barnstormer,
    the_many_adventures_of_winnie_the_pooh,
    under_the_sea_journey_of_the_little_mermaid,
    walt_disney_world_railroad_fantasyland
]

frontierland_array: list[Dict[str, Union[str, int, bool]]] = [
    big_thunder_mountain,
    country_bear_jamboree,
    splash_mountain,
    tom_sawyer_island,
    walt_disney_world_railroad_frontierland
]

liberty_square_array: list[Dict[str, Union[str, int, bool]]] = [
    haunted_mansion,
    liberty_square_riverboat,
    the_hall_of_presidents
]

main_street_usa_array: list[Dict[str, Union[str, int, bool]]] = [
    disney_festival_of_fantasy_parade,
    meet_mickey_at_town_square_theater,
    walt_disney_world_railroad_main_street_usa
]

tomorrowland_array: list[Dict[str, Union[str, int, bool]]] = [
    astro_orbiter,
    buzz_lightyear_space_ranger_spin,
    monster_inc_laugh_floor,
    space_mountain,
    tomorrowland_speedway,
    tomorrowland_transit_authority_peoplemover,
    tron_lightcycle_run,
    walt_disneys_carousel_of_progress
]


def adventureland() -> None:
    table = Table(title="Adventureland")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in adventureland_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def fantasyland() -> None:
    table = Table(title="Fantasyland")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in fantasyland_array:
        name: str = str(ride["name"])
        wait: str = str(ride["wait_time"])
        is_open: str = str(ride["is_open"])
        updated: str = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def frontierland():
    table = Table(title="Frontierland")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in frontierland_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def liberty_square() -> None:
    table = Table(title="Liberty Square")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in liberty_square_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def main_street_usa() -> None:
    table = Table(title="Main Street, U.S.A.")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in main_street_usa_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def tomorrowland() -> None:
    table = Table(title="Tomorrowland")
    table.add_column("Name", justify="right", style="cyan", no_wrap=True,
                     ratio=ratio_of_name_column, min_width=minwidth, max_width=minwidth)
    table.add_column("Wait Time", justify="center",
                     style="magenta", ratio=ratio_of_wait_time_column)
    table.add_column("Is Open", justify="center",
                     style="green", ratio=ratio_of_is_open_column)
    table.add_column("Last Updated", justify="center",
                     style="red", ratio=ratio_of_last_updated_column)
    for ride in tomorrowland_array:
        name = str(ride["name"])
        wait = str(ride["wait_time"])
        is_open = str(ride["is_open"])
        updated = str(ride["last_updated"])

        table.add_row(name, wait, is_open, updated)
    console = Console()
    console.print(table)


def all_magic_kingdom_tables() -> None:
    adventureland()
    fantasyland()
    frontierland()
    liberty_square()
    main_street_usa()
    tomorrowland()
