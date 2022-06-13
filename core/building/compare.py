from typing import Set

from core.building.one_family import OneFamilyHouse


def get_houses_mutual_names(first_house: OneFamilyHouse, second_house: OneFamilyHouse) -> Set[str]:
    mutual_names = set(first_house.names).intersection(second_house.names)
    return mutual_names


def get_one_family_houses_similarity(first_house: OneFamilyHouse, second_house: OneFamilyHouse) -> float:
    mutual_names = get_houses_mutual_names(first_house, second_house)
    all_unique_names = set(first_house.names).union(second_house.names)
    return len(mutual_names) / len(all_unique_names)
