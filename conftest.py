import pytest
import requests
from src.todo import TodoList
from src.counter import Counter
from src.library import Library
from src.user_manager import UserManager

BASE_URL = "https://jsonplaceholder.typicode.com"

#Создание линка для запроса
@pytest.fixture()
def base_url():
    def _get(path):
        return requests.get(BASE_URL + path)
    return _get

#Логирование запросов(по умолчанию ставим GET)
@pytest.fixture()
def logger_request():
    def make_request(path, method="GET"):
        url = BASE_URL + path
        print(f"\n-> Sending request {url}")
        response = requests.request(method=method, url=url)
        print(f"<- Response status: {response.status_code}")

        return response
    return make_request

#Создание пустого списка задача(класс TodoList)
@pytest.fixture()
def todo():
    return TodoList()

#Создание списка из 3 задач(класс TodoList)
@pytest.fixture()
def todo_tasks():
    todo_tasks = TodoList()

    todo_tasks.add_task("A")
    todo_tasks.add_task("B")
    todo_tasks.add_task("C")

    return todo_tasks

#Создание пустого счетчика(класс Counter)
@pytest.fixture()
def counter():
    return Counter()

#Создание пустой библиотеки(класс Library)
@pytest.fixture()
def library():
    return Library()

#Создание библиотеки с 3 книгами(класс Library)
@pytest.fixture()
def library_with_books():
    lib = Library()

    lib.add_book("Harry Potter")
    lib.add_book("1984")
    lib.add_book("The Hobbit")

    return lib

#Пустой менеджер (класс UserManager)
@pytest.fixture()
def user_manager():
    return UserManager()

#Менеджер с данными пользователей
@pytest.fixture()
def user_manager_filled():
    um = UserManager()

    um.register_user("admin", "12345")
    um.register_user("danil", "qwerty")

    return um