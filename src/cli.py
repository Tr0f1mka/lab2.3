import typer      #type: ignore

from src.iterators import TaskQueue

app = typer.Typer()

@app.command(help="Вывести задачи из файла")
def show_tasks(
    filename: str = typer.Argument(None, help="Имя файла")
) -> None:
    tasks = TaskQueue(filename)
    for i in tasks:
        print(i)


@app.command(help="Вывести задачи из файла с определённым статусом")
def status_filter(
    filename: str = typer.Argument(None, help="Имя файла"),
    status: int = typer.Argument(None, help="Значение статуса")
) -> None:
    tasks = TaskQueue(filename).status_filter(status)
    for i in tasks:
        print(i)


@app.command(help="Вывести задачи из файла с определённым приоритетом")
def priority_filter(
    filename: str = typer.Argument(None, help="Имя файла"),
    priority: int = typer.Argument(None, help="Значение приоритета")
) -> None:
    tasks = TaskQueue(filename).priority_filter(priority)
    for i in tasks:
        print(i)
