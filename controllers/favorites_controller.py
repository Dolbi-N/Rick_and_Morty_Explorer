
from utils import display_character


class FavoritesController:

    def __init__(self, storage, character_service):
        self.storage = storage
        self.character_service = character_service

    def _get_favorite_ids(self):

        favorites = self.storage.load()

        favorite_ids = []

        for item in favorites:

            if isinstance(item, dict):
                character_id = item.get("id")
            else:
                character_id = item

            if isinstance(character_id, int):
                favorite_ids.append(character_id)

        if favorites != favorite_ids:
            self.storage.save(favorite_ids)

        return favorite_ids

    def view_favorites(self):

        favorites = self._get_favorite_ids()

        if not favorites:
            print("\nNo favorite characters found.")
            return

        print("\n===== FAVORITE CHARACTERS =====")

        for character_id in favorites:

            try:
                character = self.character_service.get_character_by_id(
                    character_id
                )

                display_character(character)

            except Exception as error:
                print(
                    f"Could not load character {character_id}: {error}"
                )

    def add_favorite(self, character_id):

        favorites = self._get_favorite_ids()

        if character_id in favorites:
            print("\nCharacter is already in favorites.")
            return

        character = self.character_service.get_character_by_id(
            character_id
        )

        favorites.append(character_id)
        self.storage.save(favorites)

        print(f"\n{character.name} added to favorites.")

    def remove_favorite(self, character_id):

        favorites = self._get_favorite_ids()

        if character_id not in favorites:
            print("\nCharacter is not in favorites.")
            return

        favorites.remove(character_id)
        self.storage.save(favorites)

        print("\nCharacter removed from favorites.")
