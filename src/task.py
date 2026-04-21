from dataclasses import dataclass
from typing import Any

@dataclass()
class Task:
    """
    Задача
    """
    id: str
    name: str
    body: str
    status: int
    priority: int

    def __str__(self) -> str:
        """
        Преобразует задачу в строку
        :return: Строка - результат
        """
        return f"Task( id: {self.id}, name: {self.name}, body: {self.body}, status: {self.status}, priority: {self.priority} )"

    @classmethod
    def create(cls, json_form: Any) -> "Task":
        """
        Создание задачи
        :param json_form: JSON-формат - данные задачи
        :return: Задача
        """
        return cls(
            id = json_form.get("id"),
            name = json_form.get("name"),
            body = json_form.get("body"),
            status = json_form.get("status"),
            priority = json_form.get("priority")
        )
