from json import loads, JSONDecodeError
from typing import Any

def json_parser(data: str) -> Any:
    """
    Парсит строку в json
    :param data: Строка, которую нужно распарсить
    :return: JSON-формат
    """
    try:
        return loads(data)
    except JSONDecodeError:
        raise ValueError
