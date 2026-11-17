from core.exceptions import CharacterNotFoundError
from utils import display_character, display_characters, format_text


class CharacterController:

    def __init__(self, character_service, history_controller):
        self.character_service = character_service
        self.history_controller = history_controller

    def get_valid_id(self):

        while True:
            try:
                character_id = int(input("Enter character ID: "))

                if character_id <= 0:
                    print("ID must be a positive number.")
                    continue

                return character_id

            except ValueError:
                print("Please enter a valid integer.")

    def search_by_name(self):

        name = input("Enter character name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        name = format_text(name)

        characters = self.character_service.search_characters(
            name=name
        )

        self.history_controller.record_search(
            "Character",
            "Name",
            name
        )

        display_characters(characters)

    def search_by_id(self):

        character_id = self.get_valid_id()

        character = self.character_service.get_character_by_id(
            character_id
        )

        self.history_controller.record_search(
            "Character",
            "ID",
            str(character_id)
        )

        display_character(character)

    def search_by_filters(self):

        print("\nAvailable statuses:")
        print("1. Alive")
        print("2. Dead")
        print("3. Unknown")
        print("0. Skip")

        status_options = {
            "1": "Alive",
            "2": "Dead",
            "3": "Unknown"
        }

        status_choice = input("Choose status: ").strip()
        status = status_options.get(status_choice)

        if status_choice not in ["0", "1", "2", "3"]:
            print("Invalid status choice.")
            return

        species = input(
            "Enter species or press Enter to skip: "
        ).strip()

        if not species:
            species = None

        print("\nAvailable genders:")
        print("1. Female")
        print("2. Male")
        print("3. Genderless")
        print("4. Unknown")
        print("0. Skip")

        gender_options = {
            "1": "Female",
            "2": "Male",
            "3": "Genderless",
            "4": "Unknown"
        }

        gender_choice = input("Choose gender: ").strip()
        gender = gender_options.get(gender_choice)

        if gender_choice not in ["0", "1", "2", "3", "4"]:
            print("Invalid gender choice.")
            return

        filters = {
            "status": status,
            "species": species,
            "gender": gender
        }

        filters = {
            key: value
            for key, value in filters.items()
            if value is not None
        }

        if not filters:
            print("\nPlease select at least one filter.")
            return

        characters = self.character_service.search_characters(
            **filters
        )

        self.history_controller.record_search(
            "Character",
            "Filters",
            str(filters)
        )

        display_characters(characters)

    def random_character(self):

        character = self.character_service.get_random_character()

        display_character(character)