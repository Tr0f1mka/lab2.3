import pytest       #type: ignore
import json

from src.iterators import Task, TaskQueue

test_case = [
    {"id": "1", "name": "Task1", "body": "Begin this lab", "status": 0, "priority": 1},
    {"id": "2", "name": "Task1", "body": "Begin this lab", "status": 1, "priority": 2},
    {"id": "3", "name": "Task1", "body": "Begin this lab", "status": 2, "priority": 3},
    {"id": "4", "name": "Task1", "body": "Begin this lab", "status": 3, "priority": 0},
    {"id": "5", "name": "Task1", "body": "Begin this lab", "status": 0, "priority": 1}
]

correct_case = [Task.create(x) for x in test_case]

@pytest.fixture
def test_file(tmp_path):
    file_path = tmp_path / "test.jsonl"
    with open(file_path, "w", encoding="utf-8") as f:
        for i in test_case:
            f.write(json.dumps(i, ensure_ascii=False) + "\n")

    yield str(file_path)

error_case = [
    "error"
]

@pytest.fixture
def test_file_with_error(tmp_path):
    file_path = tmp_path / "test.jsonl"
    with open(file_path, "w", encoding="utf-8") as f:
        for i in error_case:
            f.write(i + "\n")

    yield str(file_path)


def test_iterator(test_file):
    test = TaskQueue(filename=test_file)

    assert list(test) == correct_case

def test_repeat_iterator(test_file):
    test = TaskQueue(filename=test_file)
    a = list(test)
    b = list(test)
    assert a == b
    assert a == correct_case

def test_with_value_error(test_file_with_error):
    test = TaskQueue(test_file_with_error)
    with pytest.raises(ValueError):
        next(test)

def test_filter_status_iterator(test_file):
    test = TaskQueue(filename=test_file).status_filter(0)
    assert list(test) == [x for x in correct_case if x.status == 0]

def test_filter_priority_iterator(test_file):
    test = TaskQueue(filename=test_file).priority_filter(1)
    assert list(test) == [x for x in correct_case if x.priority == 1]

def test_filter_iterator_with_value_error(test_file_with_error):
    test = TaskQueue(filename=test_file_with_error).status_filter(0)
    with pytest.raises(ValueError):
        next(test)
