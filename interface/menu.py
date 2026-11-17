class Menu:

    @staticmethod
    def show():

        print("\n===== RICK AND MORTY EXPLORER =====")
        print("1. Search Characters")
        print("2. Search Locations")
        print("3. Search Episodes")
        print("4. Favorites")
        print("5. View Search History")
        print("0. Exit")

    @staticmethod
    def show_character_menu():

        print("\n===== CHARACTER MENU =====")
        print("1. Search by Name")
        print("2. Search by Character ID")
        print("3. Search by Filters")
        print("4. Random Character")
        print("0. Back to Main Menu")

    @staticmethod
    def show_location_menu():

        print("\n===== LOCATION MENU =====")
        print("1. Search by Name")
        print("2. Search by ID")
        print("0. Back to Main Menu")

    @staticmethod
    def show_episode_menu():

        print("\n===== EPISODE MENU =====")
        print("1. Search by Name")
        print("2. Random Episode")
        print("3. Search by ID")
        print("0. Back to Main Menu")

    @staticmethod
    def show_favorites_menu():

        print("\n===== FAVORITES MENU =====")
        print("1. View Favorites")
        print("2. Add Character to Favorites")
        print("3. Remove Character from Favorites")
        print("0. Back to Main Menu")