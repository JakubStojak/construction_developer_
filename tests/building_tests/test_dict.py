import pytest

from core.addresses.address import Address


@pytest.mark.parametrize(
    "address_example", "expected",
    [
        (
                Address(street="Przydworska", number="3", city="Libertów", postcode="32-433"),
                {"address": {"street": "Przydworska", "number": "3", "city": "Libertów", "postcode": "32-433"}}
        )
    ]
)
def test_compare_buildings_names(address_example, expected):
    matches = address_example.dict()
    assert matches == expected
