import pytest
import requests
from src.todo import TodoList
from src.counter import Counter
from src.library import Library
from src.user_manager import UserManager

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def my_fixture():
    print("CREATE")
    return 100

#Возврат base_url линка
@pytest.fixture(scope="function")
def base_url():
    return BASE_URL

#Создание линка для request
@pytest.fixture(scope="session")
def posts_client():
    def make_request(path):
        url = BASE_URL + path
        response = requests.get(url=url)
        return response
    return make_request

#Возврат первого элемента в списке -> posts[0]
@pytest.fixture(scope="session")
def first_post(posts_client):
    resp = posts_client("/posts")
    return resp.json()[0]

#Создание линка для запроса + логирование
@pytest.fixture()
def logger_request():
    def make_link(path, method="GET"):
        url = BASE_URL + path
        print(f"-> Sending request {url}")
        response = requests.request(method=method, url=url)
        print(f"<- Response status {response.status_code}")
        return response
    return make_link

#Возврат .json() у обьекта users/1
@pytest.fixture()
def return_json(logger_request):
    response = logger_request("/users/1", "GET")
    return response.json()

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