import random
from typing import List

from core.addresses.address import generate_address
from core.person_names.names_generator import generate_names
from core.building.one_family import OneFamilyHouse


def generate_building(number: int) -> List[OneFamilyHouse]:
    buildings = []
    ready_number = 0
    while ready_number < number:
        try:
            building = OneFamilyHouse(
                floor_number=random.randint(1, 3),
                surface=random.randint(20, 1000),
                room_count=random.randint(2, 50),
                names=generate_names(),
                address=generate_address()
            )
            buildings.append(building)
            ready_number += 1
        except ValueError:
            pass

    return buildings
