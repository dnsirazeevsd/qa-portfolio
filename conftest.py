import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

@pytest.fixture
def api_client():
    def _get(path):
        return requests.get(BASE_URL + path)
    return _get