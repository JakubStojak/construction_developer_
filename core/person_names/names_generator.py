import random
from typing import Set

from core.person_names import person_names


def generate_names(number: int = None) -> Set[str]:
    names_number = len(set(person_names))
    if number and number < len(person_names):
        inhabitants = set()
        ready_pearson_number = 0
        while ready_pearson_number < number:
            inhabitants.add(person_names[random.randint(0, names_number - 1)])
            ready_pearson_number = len(inhabitants)
    else:
        inhabitants = {person_names[random.randint(0, names_number - 1)] for _ in range(random.randint(2, 10))}
    return inhabitants
