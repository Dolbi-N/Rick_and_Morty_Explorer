
from services.api_service import APIService
from services.character_service import CharacterService
from services.location_service import LocationService
from services.episode_service import EpisodeService

from storage.json_storage import JSONStorage

from controllers.character_controller import CharacterController
from controllers.location_controller import LocationController
from controllers.episode_controller import EpisodeController
from controllers.favorites_controller import FavoritesController
from controllers.history_controller import HistoryController

from interface.menu import Menu

from core.exceptions import (
    ProjectException,
    CharacterNotFoundError,
    StorageError
)


class RickAndMortyExplorer:

    def __init__(self):

        self.api_service = APIService()

        self.character_service = CharacterService(
            self.api_service
        )

        self.location_service = LocationService(
            self.api_service
        )

        self.episode_service = EpisodeService(
            self.api_service
        )

        self.favorites_storage = JSONStorage(
            "data/favorites.json"
        )

        self.history_storage = JSONStorage(
            "data/search_history.json"
        )

        self.history_controller = HistoryController(
            self.history_storage
        )

        self.character_controller = CharacterController(
            self.character_service,
            self.history_controller
        )

        self.location_controller = LocationController(
            self.location_service,
            self.history_controller
        )

        self.episode_controller = EpisodeController(
            self.episode_service,
            self.history_controller
        )

        self.favorites_controller = FavoritesController(
            self.favorites_storage,
            self.character_service
        )

    def character_menu(self):

        while True:

            Menu.show_character_menu()

            choice = input("Choose an option: ").strip()

            try:

                if choice == "1":
                    self.character_controller.search_by_name()

                elif choice == "2":
                    self.character_controller.search_by_id()

                elif choice == "3":
                    self.character_controller.search_by_filters()

                elif choice == "4":
                    self.character_controller.random_character()

                elif choice == "0":
                    break

                else:
                    print("\nInvalid option. Try again.")

            except CharacterNotFoundError as error:
                print(f"\n{error}")

            except ProjectException as error:
                print(f"\nProject error: {error}")

            except Exception as error:
                print(f"\nUnexpected error: {error}")

    def location_menu(self):

        while True:

            Menu.show_location_menu()

            choice = input("Choose an option: ").strip()

            try:

                if choice == "1":
                    self.location_controller.search_by_name()

                elif choice == "2":
                    self.location_controller.search_by_id()

                elif choice == "0":
                    break

                else:
                    print("\nInvalid option. Try again.")

            except ProjectException as error:
                print(f"\nProject error: {error}")

            except Exception as error:
                print(f"\nUnexpected error: {error}")

    def episode_menu(self):

        while True:

            Menu.show_episode_menu()

            choice = input("Choose an option: ").strip()

            try:

                if choice == "1":
                    self.episode_controller.search_by_name()

                elif choice == "2":
                    self.episode_controller.random_episode()

                elif choice == "3":
                    self.episode_controller.search_by_id()

                elif choice == "0":
                    break

                else:
                    print("\nInvalid option. Try again.")

            except ProjectException as error:
                print(f"\nProject error: {error}")

            except Exception as error:
                print(f"\nUnexpected error: {error}")

    def favorites_menu(self):

        while True:

            Menu.show_favorites_menu()

            choice = input("Choose an option: ").strip()

            try:

                if choice == "1":
                    self.favorites_controller.view_favorites()

                elif choice == "2":
                    character_id = (
                        self.character_controller.get_valid_id()
                    )

                    self.favorites_controller.add_favorite(
                        character_id
                    )

                elif choice == "3":
                    character_id = (
                        self.character_controller.get_valid_id()
                    )

                    self.favorites_controller.remove_favorite(
                        character_id
                    )

                elif choice == "0":
                    break

                else:
                    print("\nInvalid option. Try again.")

            except CharacterNotFoundError as error:
                print(f"\n{error}")

            except ProjectException as error:
                print(f"\nProject error: {error}")

            except Exception as error:
                print(f"\nUnexpected error: {error}")

    def run(self):

        while True:

            Menu.show()

            choice = input("Choose an option: ").strip()

            try:

                if choice == "1":
                    self.character_menu()

                elif choice == "2":
                    self.location_menu()

                elif choice == "3":
                    self.episode_menu()

                elif choice == "4":
                    self.favorites_menu()

                elif choice == "5":
                    self.history_controller.view_history()

                elif choice == "0":
                    print("\nThank you for using Rick and Morty Explorer!")
                    break

                else:
                    print("\nInvalid option. Try again.")

            except StorageError as error:
                print(f"\nStorage error: {error}")

            except ProjectException as error:
                print(f"\nProject error: {error}")

            except Exception as error:
                print(f"\nUnexpected error: {error}")
