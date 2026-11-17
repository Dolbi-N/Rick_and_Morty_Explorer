
import random

from requests.exceptions import HTTPError

from models.character import Character
from services.api_service import APIService
from core.exceptions import CharacterNotFoundError


class CharacterService:

    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def get_character_by_id(self, character_id: int) -> Character:

        try:
            data = self.api_service.get(f"character/{character_id}")

        except HTTPError as error:

            if (
                error.response is not None
                and error.response.status_code == 404
            ):
                raise CharacterNotFoundError(
                    f"Character with ID {character_id} was not found."
                ) from error

            raise

        return Character(
            id=data["id"],
            name=data["name"],
            status=data["status"],
            species=data["species"],
            gender=data["gender"],
            origin=data["origin"]["name"],
            location=data["location"]["name"],
            image=data["image"]
        )

    def search_characters(
        self,
        name=None,
        status=None,
        species=None,
        gender=None
    ):

        params = {
            "name": name,
            "status": status,
            "species": species,
            "gender": gender
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        try:
            data = self.api_service.get(
                "character",
                params=params
            )

            return [
                Character(
                    id=item["id"],
                    name=item["name"],
                    status=item["status"],
                    species=item["species"],
                    gender=item["gender"],
                    origin=item["origin"]["name"],
                    location=item["location"]["name"],
                    image=item["image"]
                )
                for item in data["results"]
            ]

        except HTTPError as error:

            if (
                error.response is not None
                and error.response.status_code == 404
            ):
                return []

            raise

    def get_random_character(self) -> Character:

        first_page = self.api_service.get("character")

        total_pages = first_page["info"]["pages"]

        random_page = random.randint(1, total_pages)

        if random_page == 1:
            data = first_page

        else:
            data = self.api_service.get(
                "character",
                params={"page": random_page}
            )

        item = random.choice(data["results"])

        return Character(
            id=item["id"],
            name=item["name"],
            status=item["status"],
            species=item["species"],
            gender=item["gender"],
            origin=item["origin"]["name"],
            location=item["location"]["name"],
            image=item["image"]
        )
