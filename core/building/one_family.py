from typing import List, Iterable

from core.addresses.address import Address
from core.building.building_interface import Building


class OneFamilyHouse(Building):
    def __init__(self, floor_number: int, room_count: int, surface: float, address: Address,  names: Iterable[str]):
        super().__init__(floor_number, room_count, surface)
        self.names = list(set(names))
        self.address = address

    def get_price(self, average_price_per_square_meter: float) -> float:
        house_price = average_price_per_square_meter * self.surface
        return house_price

    def is_neighbour(self, other: "OneFamilyHouse"):
        if self.address.street == other.address.street and self.address.city == other.address.city:
            neighbour = True
        else:
            neighbour = False
        return neighbour

    def dict(self):
        return {
            "floor_number": self.floor_number,
            "room_count": self.room_count,
            "surface": self.surface,
            "address": self.address.dict(),
            "names": self.names,
        }
