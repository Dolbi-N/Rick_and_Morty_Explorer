from utils import format_text


class LocationController:

    def __init__(self, location_service, history_controller):
        self.location_service = location_service
        self.history_controller = history_controller

    def get_valid_id(self):

        while True:
            try:
                location_id = int(input("Enter location ID: "))

                if location_id <= 0:
                    print("ID must be a positive number.")
                    continue

                return location_id

            except ValueError:
                print("Please enter a valid integer.")

    def search_by_name(self):

        name = input("Enter location name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        name = format_text(name)

        locations = self.location_service.search_locations(
            name=name
        )

        self.history_controller.record_search(
            "Location",
            "Name",
            name
        )

        self.display_locations(locations)

    def search_by_id(self):

        location_id = self.get_valid_id()

        location = self.location_service.get_location_by_id(
            location_id
        )

        self.history_controller.record_search(
            "Location",
            "ID",
            str(location_id)
        )

        if location is None:
            print("\nLocation not found.")
            return

        self.display_location(location)

    @staticmethod
    def display_location(location):

        print("\n" + "=" * 40)
        print(f"ID: {location['id']}")
        print(f"Name: {location['name']}")
        print(f"Type: {location['type']}")
        print(f"Dimension: {location['dimension']}")
        print(f"Residents: {len(location['residents'])}")
        print("=" * 40)

    def display_locations(self, locations):

        if not locations:
            print("\nNo locations found.")
            return

        for location in locations:
            self.display_location(location)