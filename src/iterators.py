from io import TextIOWrapper

from src.task import Task
from src.parser import json_parser

class TaskQueue:
    """
    Итераторы задач, читающие из файла JSON Lines
    """

    filename: str
    file: TextIOWrapper | None = None

    def __init__(self, filename: str) -> None:
        """
        Инициализация фильтрующего итератора
        :param filename: Строка - имя файла
        """
        self.filename = filename

    def __iter__(self) -> "TaskQueue":
        """
        Возвращает итератор
        :return: Фильтрующий итератор
        """
        return self

    def __next__(self) -> Task:
        """
        Возвращает задачу для итератора
        :return: Задача
        """
        if not self.file:
            self.file = open(self.filename, "r", encoding="utf-8")

        data = self.file.readline()
        if not data:
            self.file.close()
            self.file = None
            raise StopIteration

        try:
            return Task.create(json_parser(data))

        except ValueError:
            if self.file:
                self.file.close()
                self.file = None
            raise ValueError(f"Incorrect data: {data}")

    def status_filter(self, status: int) -> "FilteredTaskIterator":
        """
        Фильтрация по статусу
        :param status: Число - нужное значение статуса
        :return: Итератор
        """
        return FilteredTaskIterator(self.filename, status, "status")

    def priority_filter(self, priority: int):
        """
        Фильтрация по статусу
        :param priority: Число - нужное значение приоритета
        :return: Итератор
        """
        return FilteredTaskIterator(self.filename, priority, "priority")


class FilteredTaskIterator:
    """
    Итератор с фильтрацией по полю
    """

    file: TextIOWrapper | None = None
    filename: str
    filter_value: int
    filter_elem: str

    def __init__(self, filename: str, filter_value: int, filter_elem: str) -> None:
        """
        Инициализация фильтрующего итератора
        :param filename: Строка - имя файла
        :param filter_value: Число - нужное значение
        :param filter_elem: Строка - нужное поле
        """
        self.filename = filename
        self.filter_value = filter_value
        self.filter_elem = filter_elem

    def __iter__(self) -> "FilteredTaskIterator":
        """
        Возвращает итератор
        :return: Фильтрующий итератор
        """
        return self

    def __next__(self) -> Task:
        """
        Возвращает задачу для итератора
        :return: Задача
        """
        if not self.file:
            self.file = open(self.filename, "r", encoding="utf-8")

        data = self.file.readline()

        try:
            while data and (json_form := json_parser(data)).get(self.filter_elem) != self.filter_value:
                data = self.file.readline()

            if not data:
                self.file.close()
                self.file = None
                raise StopIteration

            return Task.create(json_form)

        except ValueError:
            if self.file:
                self.file.close()
                self.file = None
            raise ValueError(f"Incorrect data: {data}")
