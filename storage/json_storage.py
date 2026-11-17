
import json
import os

from core.exceptions import StorageError


class JSONStorage:

    def __init__(self, file_path: str):
        self.file_path = file_path

    def load(self):

        if not os.path.exists(self.file_path):
            return []

        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return json.load(file)

        except (json.JSONDecodeError, OSError) as error:
            raise StorageError(
                f"Could not load data from {self.file_path}."
            ) from error

    def save(self, data):

        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                json.dump(
                    data,
                    file,
                    indent=4,
                    ensure_ascii=False
                )

        except (OSError, TypeError) as error:
            raise StorageError(
                f"Could not save data to {self.file_path}."
            ) from error

    def add(self, item):

        data = self.load()
        data.append(item)
        self.save(data)

    def remove(self, item):

        data = self.load()

        if item in data:
            data.remove(item)
            self.save(data)
