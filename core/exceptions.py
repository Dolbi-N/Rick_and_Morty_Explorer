class ProjectException(Exception):
    """Base exception for the project."""


class CharacterNotFoundError(ProjectException):
    """Raised when a character is not found."""


class APIConnectionError(ProjectException):
    """Raised when API connection fails."""


class StorageError(ProjectException):
    """Raised when a storage operation fails."""