
import random

from requests.exceptions import HTTPError

from services.api_service import APIService


class EpisodeService:

    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def search_episodes(self, name=None, episode=None):

        params = {
            "name": name,
            "episode": episode
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        try:
            data = self.api_service.get(
                "episode",
                params=params
            )

            return data["results"]

        except HTTPError as error:

            if (
                error.response is not None
                and error.response.status_code == 404
            ):
                return []

            raise

    def get_episode_by_id(self, episode_id: int) -> dict:

        return self.api_service.get(
            f"episode/{episode_id}"
        )

    def get_random_episode(self) -> dict:

        first_page = self.api_service.get("episode")

        total_pages = first_page["info"]["pages"]

        random_page = random.randint(1, total_pages)

        if random_page == 1:
            data = first_page

        else:
            data = self.api_service.get(
                "episode",
                params={"page": random_page}
            )

        return random.choice(data["results"])
