import pytest
import requests
from src.todo import TodoList

BASE_URL = "https://jsonplaceholder.typicode.com"

#Создание линка для запроса
@pytest.fixture()
def base_url():
    def _get(path):
        return requests.get(BASE_URL + path)
    return _get

#Логирование запросов
@pytest.fixture()
def logged_request():
    def _make_request(path):
        url = BASE_URL + path
        print(f"->Sending request to {url}")
        response = requests.get(url=url)
        print(f"<-Response status: {response.status_code}")
        return response
    return _make_request

#Создание пустого списка задача
@pytest.fixture()
def todo():
    return TodoList()

@pytest.fixture()
def todo_tasks():
    todo_tasks = TodoList()

    todo_tasks.add_task("A")
    todo_tasks.add_task("B")
    todo_tasks.add_task("C")

    return todo_tasks