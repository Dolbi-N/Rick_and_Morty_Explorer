def format_text(text: str) -> str:
    return text.strip().title()


def display_character(character):
    print("\n" + "=" * 40)
    print(f"ID: {character.id}")
    print(f"Name: {character.name}")
    print(f"Status: {character.status}")
    print(f"Species: {character.species}")
    print(f"Gender: {character.gender}")
    print(f"Origin: {character.origin}")
    print(f"Location: {character.location}")
    print("=" * 40)


def display_characters(characters):
    if not characters:
        print("\nNo characters found.")
        return

    for character in characters:
        display_character(character)