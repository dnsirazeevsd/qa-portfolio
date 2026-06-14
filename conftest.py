import pytest
import requests

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

