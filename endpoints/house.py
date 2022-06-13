import json
from typing import Set

import uuid
from fastapi import APIRouter, Form, HTTPException, Path

from core.addresses.address import Address
from core.building.one_family import OneFamilyHouse

router = APIRouter()
TAG = "Generators"


@router.get("/house/list_ids", tags=[TAG])
async def list_houses_ids_endpoint():
    with open("database.json", "r") as file:
        houses = json.load(file)
    return [house["id"] for house in houses]


@router.get("/house/list", tags=[TAG])
async def list_houses_endpoint():
    with open("database.json", "r") as file:
        houses = json.load(file)
    return houses


@router.get("/house/list_from_surface/{minimum_surface}-{maximum_surface}", tags=[TAG])
async def list_houses_from_surface_endpoint(minimum_surface: float = Path(...),
                                            maximum_surface: float = Path(...)):
    new_houses_list = []
    with open("database.json", "r") as file:
        houses = json.load(file)
    for house in houses:
        if minimum_surface <= house["house"]["surface"] <= maximum_surface:
            new_houses_list.append(house["house"])
    return new_houses_list


@router.post("/house/create", tags=[TAG])
async def create_house_endpoint(
        floor_number: int = Form(default=1),
        room_count: int = Form(default=3),
        surface: float = Form(default=20.0),
        street: str = Form(default=""),
        number: str = Form(default=""),
        city: str = Form(default=""),
        postcode: str = Form(default=""),
        names: Set[str] = Form(default=set()),
):
    with open("database.json", "r") as file:
        houses = json.load(file)
    new_house_id = str(uuid.uuid1())
    new_house = OneFamilyHouse(
        floor_number=floor_number,
        room_count=room_count,
        surface=surface,
        address=Address(
            street=street,
            number=number,
            city=city,
            postcode=postcode,
        ),
        names=names,
    )
    houses.append({"id": new_house_id, "house": new_house.dict()})
    with open("database.json", "w") as file:
        json.dump(houses, file)
    return {"new_house_id": new_house_id}


@router.delete("/house/remove/{house_id}", tags=[TAG])
async def delete_house_endpoint(house_id: str = Path(...)):
    with open("database.json", "r") as file:
        houses = json.load(file)

    for house in houses:
        if str(house["id"]) == str(house_id):
            houses.remove(house)
    return f"house of id {house_id} was removed"


@router.get("/house/get/{house_id}", tags=[TAG])
async def get_house_from_id(house_id: str = Path(...)) -> OneFamilyHouse:
    with open("database.json", "r") as file:
        houses = json.load(file)

    for house in houses:
        if str(house["id"]) == str(house_id):
            return house
    raise HTTPException(404, "House of given id not found")
