import pytest

#Добавление задачи
@pytest.mark.parametrize("name_task", ["A", "B", "C"])
def test_add_task(todo, name_task):
    todo.add_task(name_task)

    assert name_task in todo.get_task()

#Удаление задачи
@pytest.mark.parametrize("name_task", ["A", "B", "C"])
def test_remove_task(todo_tasks, name_task):
    todo_tasks.remove_task(name_task)

    assert name_task not in todo_tasks.get_task()

#Проверка кол-во задач
def test_count_tasks(todo_tasks):
    assert todo_tasks.count_tasks() == 3

#Негатив(Удаление несуществующей задачи)
def test_remove_no_task(todo):
    with pytest.raises(ValueError, match = "Task not found"):
        todo.remove_task("TEST")
