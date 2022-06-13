from abc import ABC, abstractmethod


class Building(ABC):
    def __init__(self, floor_number: int, room_count: int, surface: float):
        self.floor_number = floor_number
        self.room_count = room_count
        self.surface = surface

    @abstractmethod
    def get_price(self, average_price_per_square_meter: float) -> float:
        ...
