import pytest
import requests
from faker import Faker 

def test_posts(logged_request):
    fake = Faker()
    
    obj = {
        "title" : fake.sentence(),
        "body": fake.text(),
        "userId": 1
    }

    response = requests.post("https://jsonplaceholder.typicode.com/posts", json=obj)
    assert response.status_code == 201
    response_json = response.json()
    assert response_json["title"] == obj["title"]
    assert response_json["body"] == obj["body"]
    assert response_json["userId"] == obj["userId"]
