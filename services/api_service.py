
import requests

from requests.exceptions import ConnectionError, Timeout

from core.decorators import retry
from core.exceptions import APIConnectionError


class APIService:

    BASE_URL = "https://rickandmortyapi.com/api"

    def __init__(self):
        self.session = requests.Session()

    @retry(max_attempts=3, delay=1)
    def get(self, endpoint: str, params: dict = None):

        url = f"{self.BASE_URL}/{endpoint}"

        try:
            response = self.session.get(
                url,
                params=params,
                timeout=10
            )

            response.raise_for_status()

            return response.json()

        except (ConnectionError, Timeout) as error:
            raise APIConnectionError(
                "Could not connect to Rick and Morty API."
            ) from error
