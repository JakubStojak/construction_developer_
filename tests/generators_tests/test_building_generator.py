from unittest import TestCase
from core.building.building_generator import generate_building
from core.building.one_family import OneFamilyHouse


class TestPeopleGenerator(TestCase):
    def test_generator(self):
        buildings = generate_building(2)
        self.assertEqual(2, len(buildings))
        self.assertEqual(type(buildings[0]), OneFamilyHouse)
        self.assertEqual(type(buildings[1]), OneFamilyHouse)
