import pytest

from core.building.compare import get_houses_mutual_names
from core.building.one_family import OneFamilyHouse

default_attributes = dict(zip(
    ["floor_number", "room_count", "surface", "address"],
    [1, 1, 1, ""],
))


@pytest.mark.parametrize(
    "first_building, second_building, expected",
    [
        (
            OneFamilyHouse(**default_attributes, names=["Jakub", "Kamil", "Artur", "Justyna", "Joanna"]),
            OneFamilyHouse(**default_attributes, names=["Johannes", "Kamil", "Artur", "Joanne", "Hanne"]),
            {"Kamil", "Artur"}
        )
    ]
)
def test_compare_buildings_names(first_building, second_building, expected):
    matches = get_houses_mutual_names(first_building, second_building)
    assert matches == expected
