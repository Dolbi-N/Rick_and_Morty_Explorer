class HistoryController:    # ძიების ისტორიის შენახვა და ჩვენება

    def __init__(self, storage):
        self.storage = storage

    def record_search(self, category, search_type, query):
        history = self.storage.load()

        history.append({
            "category": category,
            "search_type": search_type,
            "query": query
        })

        self.storage.save(history)

    def view_history(self):

        history = self.storage.load()

        if not history:
            print("\nSearch history is empty.")
            return

        print("\n===== SEARCH HISTORY =====")

        for index, item in enumerate(history, start=1):

            if isinstance(item, dict):
                print(
                    f"{index}. "
                    f"{item['category']} | "
                    f"{item['search_type']} | "
                    f"{item['query']}"
                )

            else:
                print(f"{index}. {item}")