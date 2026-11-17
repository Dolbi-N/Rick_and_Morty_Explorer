from utils import format_text


class EpisodeController:

    def __init__(self, episode_service, history_controller):
        self.episode_service = episode_service
        self.history_controller = history_controller

    def get_valid_id(self):

        while True:
            try:
                episode_id = int(input("Enter episode ID: "))

                if episode_id <= 0:
                    print("ID must be a positive number.")
                    continue

                return episode_id

            except ValueError:
                print("Please enter a valid integer.")

    def search_by_name(self):

        name = input("Enter episode name: ").strip()

        if not name:
            print("Name cannot be empty.")
            return

        name = format_text(name)

        episodes = self.episode_service.search_episodes(
            name=name
        )

        self.history_controller.record_search(
            "Episode",
            "Name",
            name
        )

        self.display_episodes(episodes)

    def search_by_id(self):

        episode_id = self.get_valid_id()

        episode = self.episode_service.get_episode_by_id(
            episode_id
        )

        self.history_controller.record_search(
            "Episode",
            "ID",
            str(episode_id)
        )

        self.display_episode(episode)

    def random_episode(self):

        episode = self.episode_service.get_random_episode()

        self.display_episode(episode)

    @staticmethod
    def display_episode(episode):

        print("\n" + "=" * 40)
        print(f"ID: {episode['id']}")
        print(f"Name: {episode['name']}")
        print(f"Episode: {episode['episode']}")
        print(f"Air Date: {episode['air_date']}")
        print(f"Characters: {len(episode['characters'])}")
        print("=" * 40)

    def display_episodes(self, episodes):

        if not episodes:
            print("\nNo episodes found.")
            return

        for episode in episodes:
            self.display_episode(episode)