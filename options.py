import hollywood_studios

from rich import print as rprint
from rich.prompt import Prompt


def sorry():
    rprint("Sorry this is still a work in progress...")


def choose_a_park():
    choice = Prompt.ask(
        "Which park are you visiting today?",
        choices=["Magic Kingdom", "Epcot", "Hollywood Studios", "Animal Kingdom"],
        default="Hollywood Studios"
    )
    if choice == "Magic Kingdom":
        rprint("You chose Magic Kingdom.")
    elif choice == "Epcot":
        rprint("You chose Epcot.")
    elif choice == "Hollywood Studios":
        rprint("You chose Hollywood Studios.")
        choose_land_hollywood_studios(choice)
    elif choice == "Animal Kingdom":
        rprint("You chose Animal Kingdom.")
    else:
        rprint("Not an option, please try again.")
        choose_a_park()
    return choice


def choose_land_hollywood_studios(park_choice):
    choice = Prompt.ask(
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
