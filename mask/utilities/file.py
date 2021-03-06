import json


def generate_dict_from_json(file_path: str) -> dict:
    """
    Returns a dictionary filled with JSON data loaded from the file provided.

    :param file_path: Path to file containing JSON to load
    :return: Dictionary with JSON retrieved from file
    """
    with open(file_path) as file:
        data = json.load(file)
    return data


def load_file_contents(file_path: str) -> str:
    """
    Returns the contents of a file

    :param file_path: Path to the file to load
    :return: String of file's contents
    """
    with open(file_path) as file:
        contents = file.read()
    return contents
