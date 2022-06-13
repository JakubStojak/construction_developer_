from unittest import TestCase
from core.person_names.names_generator import generate_names


class TestNamesGenerator(TestCase):
    def test_name_generator(self):
        inhabitants = generate_names(3)
        self.assertEqual(type(inhabitants), set)
        self.assertEqual(len(inhabitants), 3)
        self.assertEqual(type(inhabitants.pop()), str)
