from unittest import TestCase

from core.addresses.address import generate_address, Address


class TestAddressGenerator(TestCase):
    def test_address_generator(self):
        address = generate_address()
        self.assertEqual(type(address), Address)
