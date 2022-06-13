from typing import List

with open("core/person_names/names.txt", "r") as file:
    person_names: List[str] = file.read().split()
