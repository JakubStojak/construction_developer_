import pytest

from core.building.compare import get_one_family_houses_similarity
from core.building.one_family import OneFamilyHouse

default_attributes = dict(zip(
    ["floor_number", "room_count", "surface", "address"],
    [1, 1, 1, ""],
))


@pytest.mark.parametrize(
    "first_house, second_house, expected_similarity",
    [
        (
            OneFamilyHouse(**default_attributes, names={"Kamil"}),
            OneFamilyHouse(**default_attributes, names={"Kamil"}),
            1.0,
        ),
        (
            OneFamilyHouse(**default_attributes, names={"Kamil"}),
            OneFamilyHouse(**default_attributes, names=set()),
            0,
        ),
        (
            OneFamilyHouse(**default_attributes, names={"Kamil", "Jakub"}),
            OneFamilyHouse(**default_attributes, names={"Kamil"}),
            0.5,
        ),
        (
            OneFamilyHouse(**default_attributes, names={"Kamil", "Jakub"}),
            OneFamilyHouse(**default_attributes, names={"Kamil", "Artur"}),
            1/3,
        ),
        (
            OneFamilyHouse(**default_attributes, names={"Kamil", "Jakub", "Artur"}),
            OneFamilyHouse(**default_attributes, names={"Kamil", "Artur", "Osama"}),
            0.5,
        ),
        (
            OneFamilyHouse(**default_attributes, names={"Kamil", "Jakub", "Artur", "Aladeen"}),
            OneFamilyHouse(**default_attributes, names={"Kamil", "Artur", "Osama"}),
            2/5,
        ),
    ]
)
def test_similarity(first_house, second_house, expected_similarity):
    assert get_one_family_houses_similarity(first_house, second_house) == expected_similarity
