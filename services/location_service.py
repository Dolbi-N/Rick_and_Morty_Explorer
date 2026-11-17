
from requests.exceptions import HTTPError

from services.api_service import APIService


class LocationService:

    def __init__(self, api_service: APIService):
        self.api_service = api_service

    def search_locations(
        self,
        name=None,
        location_type=None,
        dimension=None
    ):

        params = {
            "name": name,
            "type": location_type,
            "dimension": dimension
        }

        params = {
            key: value
            for key, value in params.items()
            if value is not None
        }

        try:
            data = self.api_service.get(
                "location",
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

    def get_location_by_id(self, location_id: int):

        try:
            return self.api_service.get(
                f"location/{location_id}"
            )

        except HTTPError as error:

            if (
                error.response is not None
                and error.response.status_code == 404
            ):
                return None

            raise
