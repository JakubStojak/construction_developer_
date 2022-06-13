from unittest import TestCase

from core.addresses.address import Address
from core.building.one_family import OneFamilyHouse

address = Address(street="Makowa", number="1", city="Kraków", postcode="12-345")


class TestBuildings(TestCase):
    def test_pricing(self):
        ofh = OneFamilyHouse(floor_number=1, surface=200, room_count=12, address=address, names=[])
        average_price_per_square_meter = 9000
        expected_price = 1_800_000
        self.assertEqual(expected_price, ofh.get_price(average_price_per_square_meter))
