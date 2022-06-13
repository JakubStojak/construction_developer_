import json
from typing import Dict, List


with open("core/addresses/address_resources/streets_names.txt", "r") as file:
    street_names: List[str] = file.read().split()

with open("core/addresses/address_resources/city_postcodes.json") as file:
    city_postcodes: List[Dict[str, str]] = json.load(file)
