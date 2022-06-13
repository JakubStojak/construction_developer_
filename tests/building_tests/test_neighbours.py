import pytest

from core.addresses.address import Address
from core.building.one_family import OneFamilyHouse

default_attributes = dict(zip(
    ["floor_number", "room_count", "surface", "names"],
    [1, 1, 1, []],
))


@pytest.mark.parametrize(
    "first_house, second_house",
    [
        (
            OneFamilyHouse(**default_attributes, address=Address(street="Makowa", number="1", city="Kraków", postcode="12-345")),
            OneFamilyHouse(**default_attributes, address=Address(street="Makowa", number="2b", city="Kraków", postcode="12-345")),
        ),
    ]
)
def test_neighbours(first_house: OneFamilyHouse, second_house: OneFamilyHouse):
    assert first_house.is_neighbour(second_house)