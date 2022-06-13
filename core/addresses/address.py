import dataclasses
import random

from core.addresses import city_postcodes, street_names


@dataclasses.dataclass
class Address:
    street: str
    number: str
    city: str
    postcode: str

    def dict(self):
        return {
            "address": {
                "street": self.street,
                "number": self.number,
                "city": self.city,
                "postcode": self.postcode,
                        }
        }


def generate_address() -> Address:
    street_names_length = len(street_names)

    random_num = random.randint(0, len(city_postcodes)-1)

    address = Address(
        street=street_names[random.randint(0, street_names_length - 1)],
        number=str(random.randint(0, 300)),
        city=city_postcodes[random_num]["city"],
        postcode=city_postcodes[random_num]["postcode"],
    )
    return address
