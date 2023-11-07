import hollywood_studios
import magic_kingdom
import epcot
import animal_kingdom
from rich import print as rprint
from rich.prompt import Prompt


def sorry() -> None:
    rprint("Sorry this is still a work in progress...")


def choose_a_park() -> str:
    choice: str = Prompt.ask(
        "Which park are you visiting today?",
        choices=["Magic Kingdom", "Epcot",
                 "Hollywood Studios", "Animal Kingdom"],
        default="Hollywood Studios"
    )
    if choice == "Magic Kingdom":
        rprint("You chose Magic Kingdom.")
        choose_land_magic_kingdom(choice)
    elif choice == "Epcot":
        rprint("You chose Epcot.")
        choose_land_epcot(choice)
    elif choice == "Hollywood Studios":
        rprint("You chose Hollywood Studios.")
        choose_land_hollywood_studios(choice)
    elif choice == "Animal Kingdom":
        rprint("You chose Animal Kingdom.")
        choose_land_animal_kingdom(choice)
    else:
        rprint("Not an option, please try again.")
        choose_a_park()
    return choice


def choose_land_hollywood_studios(park_choice: str) -> None:
    choice: str = Prompt.ask(
        f"Do you have a preferred location within {park_choice}?",
        choices=[
            "Animation Courtyard",
            "Echo Lake",
            "Hollywood Boulevard",
            "Muppet Courtyard",
            "Pixar Place",
            "Star Wars: Galaxy's Edge",
            "Sunset Boulevard",
            "Toy Story Land"
        ],
        default=f"Show all rides at {park_choice}.")
    if choice == "Animation Courtyard":
        hollywood_studios.animation_courtyard()
    elif choice == "Echo Lake":
        hollywood_studios.echo_lake()
    elif choice == "Hollywood Boulevard":
        hollywood_studios.hollywood_boulevard()
    elif choice == "Muppet Courtyard":
        hollywood_studios.muppet_courtyard()
    elif choice == "Pixar Place":
        hollywood_studios.pixar_place()
    elif choice == "Star Wars: Galaxy's Edge":
        hollywood_studios.star_wars_galaxy_edge()
    elif choice == "Sunset Boulevard":
        hollywood_studios.sunset_boulevard()
    elif choice == "Toy Story Land":
        hollywood_studios.toy_story_land()
    else:
        hollywood_studios.all_hollywood_studios_tables()


def choose_land_magic_kingdom(park_choice: str) -> None:
    choice: str = Prompt.ask(
        f"Do you have a preferred location within {park_choice}?",
        choices=[
            "Adventureland",
            "Fantasyland",
            "Frontierland",
            "Liberty Square",
            "Main Street, U.S.A.",
            "Tomorrowland"
        ],
        default=f"Show all rides at {park_choice}.")
    if choice == "Adventureland":
        magic_kingdom.adventureland()
    elif choice == "Fantasyland":
        magic_kingdom.fantasyland()
    elif choice == "Frontierland":
        magic_kingdom.frontierland()
    elif choice == "Liberty Square":
        magic_kingdom.liberty_square()
    elif choice == "Main Street U.S.A.":
        magic_kingdom.main_street_usa()
    elif choice == "Tomorrowland":
        magic_kingdom.tomorrowland()
    else:
        magic_kingdom.all_magic_kingdom_tables()


def choose_land_epcot(park_choice: str) -> None:
    choice: str = Prompt.ask(
        f"Do you have a preferred location within {park_choice}?",
        choices=[
            "World Celebration",
            "World Discovery",
            "World Nature",
            "World Showcase"
        ],
        default=f"Show all rides at {park_choice}."
    )
    if choice == "World Celebration":
        epcot.world_celebration()
    elif choice == "World Discovery":
        epcot.world_discovery()
    elif choice == "World Nature":
        epcot.world_nature()
    elif choice == "World Showcase":
        epcot.world_showcase()
    else:
        epcot.all_epcot_tables()


def choose_land_animal_kingdom(park_choice: str) -> None:
    choice: str = Prompt.ask(
        f"Do you have a preferred location within {park_choice}?",
        choices=[
            "Africa",
            "Asia",
            "Dinoland U.S.A",
            "Discovery Island",
            "Pandora - The World of Avatar",
            "Rafiki's Planet Watch"
        ],
        default=f"Show all rides at {park_choice}."
    )
    if choice == "Africa":
        animal_kingdom.africa()
    elif choice == "Asia":
        animal_kingdom.asia()
    elif choice == "Dinoland U.S.A":
        animal_kingdom.dinoland_usa()
    elif choice == "Discovery Island":
        animal_kingdom.discovery_island()
    elif choice == "Pandora - The World of Avatar":
        animal_kingdom.pandora_the_world_of_avatar()
    elif choice == "Rafiki's Planet Watch":
        animal_kingdom.rafikis_planet_watch()
    else:
        animal_kingdom.all_animal_kingdom_tables()
