import string
import secrets


def generate_random_string(character_length, is_upper_case, character_type):
    characters = string.digits if character_type == "numeric" else string.ascii_letters
    if character_type == "alphanumeric":
        characters += string.digits

    if is_upper_case:
        characters = characters.upper()

    if not is_upper_case:
        characters = characters.lower()

    random_string = ''.join(secrets.choice(characters) for _ in range(character_length))
    return random_string if len(random_string) == character_length else generate_random_string(character_length,
                                                                                               is_upper_case,
                                                                                               character_type)
