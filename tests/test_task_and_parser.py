import pytest       #type: ignore

from src.task import Task
from src.parser import json_parser

def test_parser_with_error():
    with pytest.raises(ValueError):
        json_parser('{AZAZA:12}')

def test_task_str():
    test = Task(
        "1",
        "name",
        "body",
        1,
        1
    )

    assert str(test) == "Task( id: 1, name: name, body: body, status: 1, priority: 1 )"
